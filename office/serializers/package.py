from django.db import models
from rest_framework import serializers


class PackageStatus(models.TextChoices):
    DELIVERY_PREPARING = "DELIVERY_PREPARING"
    DELIVERY_STARTED = "DELIVERY_STARTED"
    DELIVERY_FINISHED = "DELIVERY_FINISHED"
    OVERSEA_SHIPMENT_PREPARING = "OVERSEA_SHIPMENT_PREPARING"
    OVERSEA_SHIPMENT_STARTED = "OVERSEA_SHIPMENT_STARTED"
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    CANCEL_PENDING = "CANCEL_PENDING"
    CANCEL_FINISHED = "CANCEL_FINISHED"


class PackageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    key = serializers.CharField()
    status = serializers.ChoiceField(PackageStatus.choices, )
    related_order_item_ids = serializers.ListField(serializers.CharField())
    customer_name = serializers.CharField()
    customer_contact = serializers.CharField()
    base_address = serializers.CharField()
    detail_address = serializers.CharField(allow_null=True)
    postal_code = serializers.CharField()
    delivery_note = serializers.CharField(allow_null=True)
    tracking_number = serializers.CharField(allow_null=True)
    created_at = serializers.CharField()
    updated_at = serializers.CharField()
    deleted_at = serializers.CharField(allow_null=True)
    remark_records = serializers.IntegerField(allow_null=True)
    inventories = serializers.IntegerField(allow_null=True)
    tracking_courier = serializers.IntegerField(allow_null=True)
