from office.serializers.daos.delivery_description import (
    DeliveryDescriptionDAOSerializer,
    DeliveryType,
)
from office.serializers.order import OrderSerializer
from office.serializers.order_item_action_log import OrderItemActionLogSerializer
from office.serializers.order_memo import OrderItemMemoSerializer
from rest_framework import fields, serializers
from drf_spectacular.utils import extend_schema_field
from order.models.order_item import OrderItem
from drf_spectacular.types import OpenApiTypes


class _OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product_option = fields.CharField()
    total_amount = fields.IntegerField()
    delivery_description = DeliveryDescriptionDAOSerializer()
    is_foreign = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.BOOL)
    def get_is_foreign(self, obj: OrderItem):
        return obj.delivery_description["DeliveryType"] == DeliveryType.FOREIGN.value

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemListSerializer(_OrderItemSerializer):
    pass


class OrderItemRetrieveSerializer(_OrderItemSerializer):
    logs = OrderItemActionLogSerializer(many=True)
    memos = serializers.SerializerMethodField()

    @extend_schema_field(OrderItemMemoSerializer(many=True))
    def get_memos(self, obj: OrderItem):
        return OrderItemMemoSerializer(
            obj.memos.filter(deleted_at__isnull=True), many=True
        ).data
