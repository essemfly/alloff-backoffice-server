from datetime import datetime
from typing import List

from iamport.client import Iamport
from rest_framework import mixins, serializers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from tagger.core.alimtalk.cancel_finished import CancelFinishedAlimtalk
from tagger.core.drf.search_filter import CustomSearchFilter, OrdersSearchFilter
from tagger.core.iamport import IMP
from tagger.core.mongo.models.order import Order, OrderStatus, Payment, Refund
from tagger.models.order_action_log import (
    OrderActionLog,
    OrderActionType,
    OrderAlimtalkLog,
    OrderAlimtalkType,
    OrderStatusChangeLog,
)
from tagger.models.order_memo import OrderMemo
from tagger.models.order_payment_adjustment import (
    OrderPaymentAdjustementType,
    OrderPaymentAdjustment,
)
from tagger.serializers.order import OrderListSerializer, OrderRetrieveSerializer
from tagger.serializers.order_memo import OrderMemoSerializer
from tagger.serializers.order_payment_adjustment import OrderPaymentAdjustmentSerializer
from tagger.serializers.refund import RefundSerializer
from tagger.core.alimtalk.delivery_started import DeliveryStartedAlimtalk


class AddPaymentAdjustmentSerializer(serializers.Serializer):
    method = serializers.ChoiceField(
        choices=OrderPaymentAdjustementType.choices,
    )
    reason = serializers.CharField(default="ALLOFF: Payment Adjustment")
    amount = serializers.IntegerField(min_value=0)
    bank_account_info = serializers.CharField(required=False)

    previous_balance = None
    previous_card_balance = None
    resulting_balance = None

    def validate(self, attrs):
        order = self.instance  # type: Order
        payment = Payment.objects.filter(
            merchantuid=str(order.id)
        ).first()  # type: Payment
        adjustments = OrderPaymentAdjustment.objects.filter(
            order_id=str(order.id)
        ).all()
        card_adjustments = adjustments.filter(
            method=OrderPaymentAdjustementType.CARD_CANCEL
        )
        self.previous_balance = payment.amount - sum([x.amount for x in adjustments])
        self.previous_card_balance = payment.amount - sum(
            [x.amount for x in card_adjustments]
        )
        self.resulting_balance = self.previous_balance - attrs.get("amount")

        if self.resulting_balance < 0:
            raise serializers.ValidationError(
                "Not enough balance (previous: {}, amount: {}, resulting: {})".format(
                    self.previous_balance, attrs.get("amount"), self.resulting_balance
                )
            )

        return super().validate(attrs)


class UpdateRefundSerializer(serializers.Serializer):
    refund_amount = serializers.IntegerField(min_value=0)  # refundamount
    refund_delivery_price = serializers.IntegerField(min_value=0)  # refunddeliveryprice
    refund_price = serializers.IntegerField(min_value=0)  # refundprice

    def validate(self, attrs):
        order = self.instance  # type: Order
        refund_fee = attrs.get("refund_price") + attrs.get("refund_delivery_price")

        if refund_fee + attrs.get("refund_amount") != order.totalprice:
            raise serializers.ValidationError(
                "Refund amount and fee does not match (order total: {}, fee + amount: {})".format(
                    order.totalprice, refund_fee + attrs.get("refund_amount")
                )
            )

        return super().validate(attrs)


class ChangeStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(OrderStatus.choices, required=True)
    delivery_tracking_number = serializers.CharField(required=False)
    delivery_tracking_url = serializers.CharField(required=False)

    tracking_info_given = None
    tracking_info_exists = None

    def validate(self, attrs):
        order = self.instance  # type: Order
        if attrs.get("status") == OrderStatus.DELIVERY_STARTED:
            self.tracking_info_given = (
                "delivery_tracking_number" in attrs and "delivery_tracking_url" in attrs
            )
            self.tracking_info_exists = (
                order.deliverytrackingnumber is not None
                and order.deliverytrackingurl is not None
            )

            if not self.tracking_info_given and not self.tracking_info_exists:
                raise serializers.ValidationError(
                    "Tracking info should be present when changing status to DELIVERY_STARTED"
                )
        return super().validate(attrs)


class AddOrderMemoSerializer(serializers.Serializer):
    body = serializers.CharField(required=True)


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Order.objects(orderstatus__nin=["CREATED", "RECREATED"]).order_by("-id")
    filter_backends = [OrdersSearchFilter]
    search_fields = [
        "user__mobile",
        "orders__product__name",
        "orders__alloffproduct__name",
    ]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderRetrieveSerializer
        elif self.action == "add_payment_adjustment":
            return AddPaymentAdjustmentSerializer
        elif self.action == "update_refund":
            return UpdateRefundSerializer
        elif self.action == "change_status":
            return ChangeStatusSerializer
        elif self.action == "add_memo":
            return AddOrderMemoSerializer
        return OrderListSerializer

    @action(detail=True, methods=["POST"])
    def add_memo(self, request: Request, id=None):
        serializer = self.get_serializer(
            data=request.data
        )  # type: AddOrderMemoSerializer
        serializer.is_valid(raise_exception=True)
        memo = OrderMemo.objects.create(
            admin=request.user, body=serializer.validated_data.get("body"), order_id=id
        )
        return Response(
            OrderMemoSerializer(memo).data,
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["POST"])
    def change_status(self, request: Request, id=None):
        order = self.get_object()  # type: Order
        payment = order.get_payment()
        serializer = self.get_serializer(
            data=request.data, instance=order
        )  # type: ChangeStatusSerializer
        serializer.is_valid(raise_exception=True)

        # Change status
        status_from = order.orderstatus
        status_to = serializer.validated_data.get("status")
        Order.objects(id=id).update_one(set__orderstatus=status_to)

        # Log
        log = OrderActionLog.objects.create(
            order_id=id,
            admin=request.user,
            action_type=OrderActionType.STATUS_CHANGE,
        )

        OrderStatusChangeLog.objects.create(
            order_id=id,
            action_log=log,
            status_from=status_from,
            status_to=status_to,
            delivery_tracking_number_from=order.deliverytrackingnumber,
            delivery_tracking_url_from=order.deliverytrackingurl,
            delivery_tracking_number_to=serializer.validated_data.get(
                "delivery_tracking_number"
            ),
            delivery_tracking_url_to=serializer.validated_data.get(
                "delivery_tracking_url"
            ),
        )

        # Update tracking info if needed
        if status_to == OrderStatus.DELIVERY_STARTED:
            if serializer.tracking_info_given:
                Order.objects(id=id).update_one(
                    set__deliverytrackingnumber=serializer.validated_data.get(
                        "delivery_tracking_number"
                    ),
                    set__deliverytrackingurl=serializer.validated_data.get(
                        "delivery_tracking_url"
                    ),
                )

                request_id = (
                    DeliveryStartedAlimtalk(str(order.id))
                    .add(
                        mobile=order.user.mobile,
                        grouping_key=order.user._id,
                        productName="" if payment is None else payment.name,
                        trackingNumber=serializer.validated_data.get(
                            "delivery_tracking_number"
                        ),
                    )
                    .send()
                )

                OrderAlimtalkLog.objects.create(
                    order_id=id,
                    action_log=log,
                    request_id=request_id,
                    alimtalk_type=OrderAlimtalkType.DELIVERY_STARTED,
                )

        return Response(
            OrderRetrieveSerializer(self.get_object().reload()).data,
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["POST"])
    def add_payment_adjustment(self, request: Request, id=None):
        order = self.get_object()  # type: Order
        serializer = self.get_serializer(
            data=request.data, instance=order
        )  # type: AddPaymentAdjustmentSerializer
        serializer.is_valid(raise_exception=True)

        payment = order.get_payment()
        if payment is None:
            return Response(
                {"message": "Payment does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        res = None
        if (
            serializer.validated_data["method"]
            == OrderPaymentAdjustementType.CARD_CANCEL
        ):
            try:
                res = IMP.instance().cancel_payment(
                    payment.impuid,
                    serializer.validated_data["amount"],
                    serializer.previous_card_balance,
                    serializer.validated_data["reason"],
                )
            except Iamport.ResponseError as e:
                return Response(
                    {"message": e.message, "success": False},
                    status=status.HTTP_200_OK,
                )

        new_adjustment = OrderPaymentAdjustment.objects.create(
            order_id=id,
            method=serializer.validated_data.get("method"),
            admin=request.user,
            previous_balance=serializer.previous_balance,
            amount=serializer.validated_data.get("amount"),
            resulting_balance=serializer.resulting_balance,
            pg_response=res,
            bank_account_info=serializer.validated_data.get("bank_account_info"),
            reason=serializer.validated_data.get("reason"),
        )

        request_id = (
            CancelFinishedAlimtalk(str(order.id))
            .add(
                mobile=order.user.mobile,
                grouping_key=order.user._id,
                productName=payment.name,
                amount=serializer.validated_data.get("amount"),
            )
            .send()
        )

        # Log
        log = OrderActionLog.objects.create(
            order_id=id,
            admin=request.user,
            action_type=OrderActionType.PAYMENT_ADJUSTMENT,
        )

        # Send alimtalk
        OrderAlimtalkLog.objects.create(
            order_id=id,
            action_log=log,
            request_id=request_id,
            alimtalk_type=OrderAlimtalkType.CANCEL_FINISHED,
        )

        return Response(
            OrderPaymentAdjustmentSerializer(new_adjustment).data,
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["POST"])
    def update_refund(self, request: Request, id=None):
        serializer = self.get_serializer(
            data=request.data, instance=self.get_object()
        )  # type: AddPaymentAdjustmentSerializer
        serializer.is_valid(raise_exception=True)

        query = Refund.objects.filter(orderid=id)
        if len(query) == 0:
            refund = Refund.objects.create(
                orderid=id,
                refunddeliveryprice=serializer.validated_data.get(
                    "refund_delivery_price"
                ),
                refundprice=serializer.validated_data.get("refund_price"),
                refundamount=serializer.validated_data.get("refund_amount"),
                created=datetime.now(),
                updated=datetime.now(),
            )
        else:
            refund = query.first()  # type: Refund
            refund.refunddeliveryprice = serializer.validated_data.get(
                "refund_delivery_price"
            )
            refund.refundprice = serializer.validated_data.get("refund_price")
            refund.refundamount = serializer.validated_data.get("refund_amount")
            refund.updated = datetime.now()
            refund.save()

        return Response(RefundSerializer(refund).data, status=status.HTTP_200_OK)
