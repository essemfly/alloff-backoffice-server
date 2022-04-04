from gen.pyalloff import order_item_memo_pb2
from office.serializers.user_recorded_model import WithUserSerializer
from rest_framework import fields


class OrderItemMemoSerializer(WithUserSerializer):
    id = fields.IntegerField()
    body = fields.CharField(allow_null=False)
    created_at = fields.DateTimeField()
    deleted_at = fields.DateTimeField(allow_null=True)

    class Meta:
        proto_class = order_item_memo_pb2.OrderItemMemo
