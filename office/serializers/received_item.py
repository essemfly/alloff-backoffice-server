from django.db import models
from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_field
from office.serializers.inventory import InventorySerializer
from office.serializers.order_item import OrderItemRetrieveSerializer
from office.serializers.pagination import PaginationSerializer
from rest_framework import fields


class ReceivedItemStatus(models.TextChoices):
    ON_RECEIVING = "ON_RECEIVING"  # 입고 중
    RECEIVED = "RECEIVED"  # 입고 완료
    OUT_OF_STOCK = "OUT_OF_STOCK"  # 취소됨 (재고부족)
    CANCELED = "CANCELED"  # 취소됨 (고객/관리자 취소)
    REVERTED = "REVERTED"  # 취소됨 (입고처리 원복)


class ReceivedItemSerializer(proto_serializers.Serializer):
    id = fields.IntegerField()
    order_id = fields.IntegerField()
    code = fields.CharField()
    status = fields.ChoiceField(ReceivedItemStatus.choices)
    product_id = fields.CharField()
    product_name = fields.CharField()
    product_img = fields.CharField()
    brand_keyname = fields.CharField()
    brand_korname = fields.CharField()
    size = fields.CharField()
    color = fields.CharField(allow_null=True)
    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()
    deleted_at = fields.DateTimeField(allow_null=True)

    inventory = fields.SerializerMethodField()

    @extend_schema_field(InventorySerializer(allow_null=True))
    def get_inventory(self, obj):
        if obj.inventory.id == 0:
            return None
        return InventorySerializer(obj.inventory).data

    order_item = OrderItemRetrieveSerializer()


class PaginatedReceivedItemSerializer(PaginationSerializer):
    results = ReceivedItemSerializer(many=True)
