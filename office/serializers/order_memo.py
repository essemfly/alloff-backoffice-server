from django_grpc_framework import proto_serializers
from protos.order.order_item_memo import order_item_memo_pb2
from rest_framework import fields


class OrderItemMemoSerializer(proto_serializers.ProtoSerializer):
    body = fields.CharField(allow_null=False)
    user_uuid = fields.CharField()
    user_username = fields.CharField()
    created_at = fields.DateTimeField()
    deleted_at = fields.DateTimeField(allow_null=True)

    class Meta:
        proto_class = order_item_memo_pb2.OrderItemMemo
