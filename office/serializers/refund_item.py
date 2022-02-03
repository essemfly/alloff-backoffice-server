from django_grpc_framework import proto_serializers
from rest_framework import fields


class RefundItemSerializer(proto_serializers.Serializer):
    id = fields.IntegerField()
    refund_fee = fields.IntegerField(allow_null=True)
    refund_amount = fields.IntegerField()
    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()
