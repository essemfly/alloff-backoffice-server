from office.serializers.order import OrderSerializer
from office.serializers.order_item_action_log import OrderItemActionLogSerializer
from office.serializers.order_memo import OrderItemMemoSerializer
from rest_framework import fields, serializers

from order.models.order_item import OrderItem


class _OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product_option = fields.CharField()
    total_amount = fields.IntegerField()

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemListSerializer(_OrderItemSerializer):
    pass


class OrderItemRetrieveSerializer(_OrderItemSerializer):
    logs = OrderItemActionLogSerializer(many=True)
    memos = OrderItemMemoSerializer(many=True)
