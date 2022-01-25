from django.contrib.auth.models import User
from office.alimtalk.cancel_finished import CancelFinishedAlimtalk
from office.alimtalk.delivery_started import DeliveryStartedAlimtalk
from office.serializers.order_item import OrderItemRetrieveSerializer
from order.models.order_item import OrderItem, OrderItemStatus
from order.models.order_item_action_log import (
    OrderItemActionLog,
    OrderItemActionType,
    OrderItemAlimtalkLog,
    OrderItemAlimtalkType,
    OrderItemStatusChangeLog,
)
from order.models.refund_item import RefundItem
from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response


class ChangeStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(OrderItemStatus.choices, required=True)
    tracking_number = serializers.CharField(required=False)
    tracking_url = serializers.CharField(required=False)

    tracking_info_given = None
    tracking_info_exists = None

    def validate(self, attrs):
        item = self.instance  # type: OrderItem
        if attrs.get("status") == OrderItemStatus.ORDER_ITEM_DELIVERY_STARTED:
            self.tracking_info_given = (
                "tracking_number" in attrs and "tracking_url" in attrs
            )
            self.tracking_info_exists = (
                item.tracking_number is not None and item.tracking_url is not None
            )

            if not self.tracking_info_given and not self.tracking_info_exists:
                raise serializers.ValidationError(
                    "Tracking info should be present when changing status to DELIVERY_STARTED"
                )
        return super().validate(attrs)


def change_status(self, request: Request, id: str = None):
    item = self.get_object()  # type: OrderItem
    serializer = self.get_serializer(
        data=request.data, instance=item
    )  # type: ChangeStatusSerializer
    serializer.is_valid(raise_exception=True)

    return Response(
        OrderItemRetrieveSerializer(
            _change_status(serializer, item, request.user, id)
        ).data,
        status=status.HTTP_200_OK,
    )


def _change_status(
    serializer: ChangeStatusSerializer, item: OrderItem, user: User, id: str = None
) -> OrderItem:
    # Change status
    status_from = item.order_item_status
    status_to = serializer.validated_data.get("status")

    item.order_item_status = status_to

    # Log
    log = OrderItemActionLog.objects.create(
        order_item=item,
        admin=user,
        action_type=OrderItemActionType.STATUS_CHANGE,
        detail=f"{status_from} -> {status_to}",
    )

    tracking_number = serializer.validated_data.get("tracking_number")
    tracking_url = serializer.validated_data.get("tracking_url")

    change_log = OrderItemStatusChangeLog.objects.create(
        order_item=item,
        action_log=log,
        status_from=status_from,
        status_to=status_to,
    )

    # Update tracking info if needed
    if status_to == OrderItemStatus.ORDER_ITEM_DELIVERY_STARTED:
        if serializer.tracking_info_given:
            change_log.tracking_number_from = item.tracking_number
            change_log.tracking_url_from = item.tracking_url
            change_log.tracking_number_to = tracking_number
            change_log.tracking_url_to = tracking_url
            change_log.save()

            item.tracking_number = tracking_number
            item.tracking_url = tracking_url

            request_id = (
                DeliveryStartedAlimtalk(item.order_item_code)
                .add(
                    mobile=item.order.user["mobile"],
                    grouping_key=item.order.user_id,
                    productName=item.product_name,
                    trackingNumber=tracking_number,
                )
                .send()
            )

            OrderItemAlimtalkLog.objects.create(
                order_item=item,
                action_log=log,
                request_id=request_id,
                alimtalk_type=OrderItemAlimtalkType.DELIVERY_STARTED,
            )

    elif status_to in [
        OrderItemStatus.ORDER_ITEM_CANCEL_FINISHED,
        OrderItemStatus.ORDER_ITEM_RETURN_FINISHED,
    ]:
        refund = RefundItem.objects.get(order_item=item)  # type: RefundItem
        # Send alimtalk
        request_id = (
            CancelFinishedAlimtalk(str(item.id))
            .add(
                mobile=item.order.user["mobile"],
                grouping_key=item.order.user_id,
                productName=item.product_name,
                amount=refund.refund_amount,
            )
            .send()
        )
        OrderItemAlimtalkLog.objects.create(
            order_item=item,
            action_log=log,
            request_id=request_id,
            alimtalk_type=OrderItemAlimtalkType.CANCEL_FINISHED,
        )

    item.save()
    return item
