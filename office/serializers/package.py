from django.db import models
from django_grpc_framework import proto_serializers
from office.serializers.courier import CourierSerializer
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

class PackageRemarkRecordType(models.TextChoices):
    CANCELED = "CANCELED"  # 취소
    PARTIALLY_CANCELED = "PARTIALLY_CANCELED"  # 부분취소
    PARTIALLY_SHIPMENT = "PARTIALLY_SHIPMENT"  # 분리 배송
    COMBINE_SHIPMENT = "COMBINE_SHIPMENT"  # 합배송

class PackageRemarkRecordProtoSerializer(proto_serializers.ProtoSerializer):
    record_type = serializers.ChoiceField(
        choices=PackageRemarkRecordType.choices,
    )
    description = serializers.CharField(max_length=50)
    reference = serializers.CharField(max_length=50, null=True, blank=True)
    created_at = serializers.DateTimeField(auto_now_add=True)


class PackageLogProtoSerializer(proto_serializers.ProtoSerializer):
    class Meta:
        model = PackageLog
        proto_class = package_log_pb2.PackageLog
        fields = "__all__"

class PackageSerializer(proto_serializers.ProtoSerializer):
    id = serializers.IntegerField()
    key = serializers.CharField()
    status = serializers.ChoiceField(
        PackageStatus.choices,
    )
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
    tracking_courier = CourierSerializer()
