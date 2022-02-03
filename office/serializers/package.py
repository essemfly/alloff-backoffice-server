from django.db import models
from django_grpc_framework import proto_serializers
from office.serializers.courier import CourierSerializer
from rest_framework import serializers
from office.serializers.inventory import InventorySerializer
from protos.logistics.package import package_pb2


class PackageStatus(models.TextChoices):
    CREATED = "CREATED"
    OVERSEAS_DELIVERY_STARTED = "OVERSEAS_SHIPMENT_PREPARING"
    DOMESTIC_DELIVERY_STARTED = "DOMESTIC_DELIVERY_STARTED"
    DELIVERED = "DELIVERY_FINISHED"
    CANCELED = "CANCELED"


class PackageSerializer(proto_serializers.ProtoSerializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    status = serializers.ChoiceField(
        PackageStatus.choices,
    )
    customer_name = serializers.CharField()
    customer_mobile = serializers.CharField()
    address = serializers.CharField()
    base_address = serializers.CharField()
    detail_address = serializers.CharField(allow_null=True)
    post_code = serializers.CharField()
    delivery_note = serializers.CharField(allow_null=True)
    overseas_tracking_number = serializers.CharField(allow_null=True)
    domestic_tracking_number = serializers.CharField(allow_null=True)

    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    overseas_shipped_at = serializers.DateTimeField(allow_null=True)
    domestic_shipped_at = serializers.DateTimeField(allow_null=True)
    delivered_at = serializers.DateTimeField(allow_null=True)
    canceled_at = serializers.DateTimeField(allow_null=True)
    deleted_at = serializers.DateTimeField(allow_null=True)

    domestic_courier = CourierSerializer(allow_null=True)
    overseas_courier = CourierSerializer(allow_null=True)

    inventories = InventorySerializer(many=True)

    class Meta:
        proto_class = package_pb2.Package
