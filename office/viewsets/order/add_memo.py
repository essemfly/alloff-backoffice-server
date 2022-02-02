from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from tagger.models.order_action_log import OrderActionLog, OrderActionType
from tagger.models.order_memo import OrderMemo
from tagger.serializers.order_memo import OrderMemoSerializer


class AddOrderMemoSerializer(serializers.Serializer):
    body = serializers.CharField(required=True)


def add_memo(self, request: Request, id: str = None):
    serializer = self.get_serializer(data=request.data)  # type: AddOrderMemoSerializer
    serializer.is_valid(raise_exception=True)
    body = serializer.validated_data.get("body")
    memo = OrderMemo.objects.create(admin=request.user, body=body, order_id=id)

    # Log
    OrderActionLog.objects.create(
        order_id=id,
        admin=request.user,
        action_type=OrderActionType.MEMO_ADD,
        detail=body,
    )

    return Response(
        OrderMemoSerializer(memo).data,
        status=status.HTTP_200_OK,
    )
