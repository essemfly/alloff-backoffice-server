from django.db import models
from django_grpc_framework import proto_serializers
from office.serializers.package import PackageSerializer
from office.serializers.pagination import PaginationSerializer
from office.serializers.shipping_notice_item import ShippingNoticeItemSerializer
from protos.logistics.shipping_notice import shipping_notice_pb2
from rest_framework import serializers


class ShippingNoticeStatus(models.TextChoices):
    CREATED = "CREATED"
    LOCKED = "LOCKED"  # inventory 등 모든 상태변경을 여기서 변경하도록 수정 (현재 sealed에서 변경됨)
    PARTIALLY_SHIPPED = "PARTIALLY_SHIPPED"
    SHIPPED = "SHIPPED"


class ShippingNoticeListSerializer(proto_serializers.ProtoSerializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    status = serializers.ChoiceField(ShippingNoticeStatus.choices)
    template_url = serializers.CharField(allow_null=True)
    locked_at = serializers.DateTimeField(allow_null=True)
    sealed_at = serializers.DateTimeField(allow_null=True)
    shipped_at = serializers.DateTimeField(allow_null=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    items = ShippingNoticeItemSerializer(many=True)

    class Meta:
        proto_class = shipping_notice_pb2.ShippingNotice


class ShippingNoticeRetrieveSerializer(ShippingNoticeListSerializer):
    packages = PackageSerializer(many=True)

    class Meta:
        proto_class = shipping_notice_pb2.ShippingNotice


class PaginatedShippingNoticeSerializer(PaginationSerializer):
    results = ShippingNoticeListSerializer(many=True)

    class Meta:
        proto_class = shipping_notice_pb2.ShippingNoticeListResponse
