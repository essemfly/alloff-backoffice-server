from office.serializers.order_memo import OrderItemMemoSerializer
from order.models.order_item_action_log import OrderItemActionLog, OrderItemActionType
from order.models.order_item_memo import OrderItemMemo
from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response


class AddOrderItemMemoSerializer(serializers.Serializer):
    body = serializers.CharField(required=True)


def add_memo(self, request: Request, id: str = None):
    serializer = self.get_serializer(
        data=request.data
    )  # type: AddOrderItemMemoSerializer
    item = self.get_object()
    serializer.is_valid(raise_exception=True)
    body = serializer.validated_data.get("body")
    memo = OrderItemMemo.objects.create(
        admin=request.user,
        body=body,
        order_item=item,
    )

    # Log
    OrderItemActionLog.objects.create(
        order_item=item,
        admin=request.user,
        action_type=OrderItemActionType.MEMO_ADD,
        detail=body,
    )

    return Response(
        OrderItemMemoSerializer(memo).data,
        status=status.HTTP_200_OK,
    )
