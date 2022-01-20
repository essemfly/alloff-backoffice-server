from django.db import models
from office.serializers.inventory import InventorySerializer
from rest_framework import serializers


class ReceivedItemStatus(models.TextChoices):
    SOURCING_REQUIRED = "SOURCING_REQUIRED"
    ON_RECEIVING = "ON_RECEIVING"
    RECEIVED = "RECEIVED"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    CANCELED = "CANCELED"


class ReceivedItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    status = serializers.ChoiceField(ReceivedItemStatus.choices)
    product_id = serializers.CharField()
    product_name = serializers.CharField()
    product_brand_id = serializers.CharField()
    product_brand_name = serializers.CharField()
    product_size = serializers.CharField()
    product_color = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    deleted_at = serializers.DateTimeField(allow_null=True)
    inventory = InventorySerializer(allow_null=True)
