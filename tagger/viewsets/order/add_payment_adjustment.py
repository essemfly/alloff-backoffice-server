from iamport.client import Iamport
from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from tagger.core.iamport import IMP
from tagger.core.mongo.models.order import Order, Payment
from tagger.models.order_action_log import (
    OrderActionLog,
    OrderActionType,
)
from tagger.models.order_payment_adjustment import (
    OrderPaymentAdjustementType,
    OrderPaymentAdjustment,
)
from tagger.serializers.order_payment_adjustment import OrderPaymentAdjustmentSerializer


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
    if serializer.validated_data["method"] == OrderPaymentAdjustementType.CARD_CANCEL:
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
                status=status.HTTP_400_BAD_REQUEST,
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

    # Log
    OrderActionLog.objects.create(
        order_id=id,
        admin=request.user,
        action_type=OrderActionType.PAYMENT_ADJUSTMENT,
    )

    return Response(
        OrderPaymentAdjustmentSerializer(new_adjustment).data,
        status=status.HTTP_200_OK,
    )
