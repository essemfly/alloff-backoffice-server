from datetime import datetime
from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from tagger.core.mongo.models.order import Order, OrderStatus
from tagger.models.order_action_log import (
    OrderActionLog,
    OrderActionType,
    OrderAlimtalkLog,
    OrderAlimtalkType,
    OrderStatusChangeLog,
)
from tagger.serializers.order import OrderRetrieveSerializer
from tagger.core.alimtalk.delivery_started import DeliveryStartedAlimtalk


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


def get_timestamp_field_with_status(status: OrderStatus):
    if status == OrderStatus.DELIVERY_STARTED:
        return "deliveryStartedAt"
    elif status == OrderStatus.DELIVERY_FINISHED:
        return "deliveryFinishedAt"
    elif status == OrderStatus.CANCEL_FINISHED:
        return "cancelFinishedAt"
    return None


def is_allowed_transition(status_from: OrderStatus, status_to: OrderStatus):
    if status_from == OrderStatus.PAYMENT_FINISHED:
        return status_to in [
            OrderStatus.PRODUCT_PREPARING,
            OrderStatus.DELIVERY_PREPARING,
            OrderStatus.DELIVERY_STARTED,
            OrderStatus.CANCEL_PENDING,
        ]

    elif status_from == OrderStatus.PRODUCT_PREPARING:
        return status_to in [
            OrderStatus.DELIVERY_PREPARING,
            OrderStatus.DELIVERY_STARTED,
            OrderStatus.CANCEL_PENDING,
        ]

    elif status_from == OrderStatus.DELIVERY_PREPARING:
        return status_to in [OrderStatus.DELIVERY_STARTED, OrderStatus.CANCEL_PENDING]

    elif status_from == OrderStatus.DELIVERY_STARTED:
        return status_to in [OrderStatus.DELIVERY_FINISHED, OrderStatus.CANCEL_PENDING]

    elif status_from == OrderStatus.DELIVERY_FINISHED:
        return status_to in [OrderStatus.CONFIRM_PAYMENT, OrderStatus.CANCEL_PENDING]

    elif status_from == OrderStatus.CONFIRM_PAYMENT:
        return status_to == OrderStatus.CANCEL_PENDING

    elif status_from == OrderStatus.CANCEL_REQUESTED:
        return status_to == OrderStatus.CANCEL_PENDING

    elif status_from == OrderStatus.CANCEL_FINISHED:
        return False

    return False


def change_status(self, request: Request, id: str = None):
    order = self.get_object()  # type: Order
    payment = order.get_payment()
    serializer = self.get_serializer(
        data=request.data, instance=order
    )  # type: ChangeStatusSerializer
    serializer.is_valid(raise_exception=True)

    # Change status
    status_from = order.orderstatus
    status_to = serializer.validated_data.get("status")
    if not is_allowed_transition(status_from, status_to):
        return Response(
            {
                "message": "transition from {} to {} is not allowed!".format(
                    status_from, status_to
                )
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    timestamp_to_update = get_timestamp_field_with_status(status_to)
    timestamp_set = (
        {}
        if timestamp_to_update is None
        else {"set__{}".format(timestamp_to_update): datetime.utcnow()}
    )
    Order.objects(id=id).update_one(set__orderstatus=status_to, **timestamp_set)

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
        delivery_tracking_url_to=serializer.validated_data.get("delivery_tracking_url"),
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
