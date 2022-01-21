from datetime import datetime
from rest_framework import serializers, status
from rest_framework.fields import IntegerField
from rest_framework.request import Request
from rest_framework.response import Response
from tagger.models.order_action_log import OrderActionLog, OrderActionType
from tagger.models.order_memo import OrderMemo
from tagger.serializers.order_memo import OrderMemoSerializer


class DeleteOrderMemoSerializer(serializers.Serializer):
    memo_id = IntegerField(required=True)


def delete_memo(self, request: Request, id: str = None):
    serializer = self.get_serializer(
        data=request.data
    )  # type: DeleteOrderMemoSerializer
    serializer.is_valid(raise_exception=True)
    memo_id = serializer.validated_data.get("memo_id")

    try:
        memo = OrderMemo.objects.get(id=memo_id)

        if memo.admin != request.user:
            Response(
                {"message": "Cannot delete other people's memos!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        memo.deleted_at = datetime.now()
        memo.save()

        # Log
        OrderActionLog.objects.create(
            order_id=id,
            admin=request.user,
            action_type=OrderActionType.MEMO_DELETE,
            detail=memo.body,
        )

        return Response(
            OrderMemoSerializer(memo).data,
            status=status.HTTP_200_OK,
        )
    except:
        return Response(
            {"message": "Cannot find memo with memo_id of {}".format(memo_id)},
            status=status.HTTP_400_BAD_REQUEST,
        )
