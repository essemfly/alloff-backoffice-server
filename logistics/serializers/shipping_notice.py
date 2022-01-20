from rest_framework import serializers
from django_grpc_framework import proto_serializers

from logistics.models import ShippingNotice, ShippingNoticeStatus
from logistics.protos.shipping_notice_proto import shipping_notice_pb2


class ShippingNoticeProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = ShippingNotice
        proto_class = shipping_notice_pb2.ShippingNotice
        fields = "__all__"


class ShippingNoticeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=13, allow_null=False)
    status = serializers.ChoiceField(
        choices=ShippingNoticeStatus.choices,
        default=ShippingNoticeStatus.CREATED,
    )
    template_url = serializers.URLField(allow_null=True, allow_blank=True)

    # dates
    locked_at = serializers.DateTimeField(allow_null=True)
    sealed_at = serializers.DateTimeField(allow_null=True)
    shipped_at = serializers.DateTimeField(allow_null=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
