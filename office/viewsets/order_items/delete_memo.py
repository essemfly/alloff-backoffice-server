from datetime import datetime

from office.serializers.order_memo import OrderItemMemoSerializer
from order.models.order_item import OrderItem
from order.models.order_item_action_log import OrderItemActionLog, OrderItemActionType
from order.models.order_item_memo import OrderItemMemo
from rest_framework import serializers, status
from rest_framework.fields import IntegerField
from rest_framework.request import Request
from rest_framework.response import Response


class DeleteItemOrderMemoSerializer(serializers.Serializer):
    memo_id = IntegerField(required=True)


def delete_memo(self, request: Request, id: str = None):
    serializer = self.get_serializer(
        data=request.data
    )  # type: DeleteItemOrderMemoSerializer
    item = self.get_object()  # type: OrderItem
    serializer.is_valid(raise_exception=True)
    memo_id = serializer.validated_data.get("memo_id")

    try:
        memo = OrderItemMemo.objects.get(id=memo_id)

        if memo.admin != request.user:
            Response(
                {"message": "Cannot delete other people's memos!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        memo.deleted_at = datetime.now()
        memo.save()

        # Log
        OrderItemActionLog.objects.create(
            order_item=item,
            admin=request.user,
            action_type=OrderItemActionType.MEMO_DELETE,
            detail=memo.body,
        )

        return Response(
            OrderItemMemoSerializer(memo).data,
            status=status.HTTP_200_OK,
        )
    except Exception:
        return Response(
            {"message": "Cannot find memo with memo_id of {}".format(memo_id)},
            status=status.HTTP_400_BAD_REQUEST,
        )
