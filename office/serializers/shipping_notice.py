from django.db import models
from rest_framework import serializers

from office.serializers.shipping_notice_item import ShippingNoticeItemSerializer


class ShippingNoticeStatus(models.TextChoices):
    CREATED = "CREATED"
    LOCKED = "LOCKED"
    SEALED = "SEALED"
    SHIPPED = "SHIPPED"


class ShippingNoticeSerializer(serializers.Serializer):
    items = ShippingNoticeItemSerializer(many=True)

    id = serializers.IntegerField()
    code = serializers.CharField()
    status = serializers.ChoiceField(ShippingNoticeStatus.choices)
    template_url = serializers.CharField(allow_null=True)
    locked_at = serializers.CharField(allow_null=True)
    sealed_at = serializers.CharField(allow_null=True)
    shipped_at = serializers.CharField(allow_null=True)
    created_at = serializers.CharField()
    updated_at = serializers.CharField()
