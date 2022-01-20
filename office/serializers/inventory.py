from django.db import models
from rest_framework import serializers


class InventoryStatus(models.TextChoices):
    CREATED = "CREATED"
    IN_STOCK = "IN_STOCK"
    PROCESSING_NEEDED = "PROCESSING_NEEDED"
    SHIPPED = "SHIPPED"
    SHIPPING_PENDING = "SHIPPING_PENDING"


class InventorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    status = serializers.ChoiceField(InventoryStatus.choices)
    product_id = serializers.CharField()
    product_name = serializers.CharField()
    product_brand_id = serializers.CharField()
    product_brand_name = serializers.CharField()
    product_size = serializers.CharField()
    product_color = serializers.CharField()
    location = serializers.CharField(allow_null=True, allow_blank=True)
    memo = serializers.CharField(allow_null=True, allow_blank=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    deleted_at = serializers.DateTimeField(allow_null=True)
