from office.serializers.admin import AdminSerializer
from rest_framework import serializers

from order.models.order_item_memo import OrderItemMemo


class OrderItemMemoSerializer(serializers.ModelSerializer):
    admin = AdminSerializer()

    class Meta:
        model = OrderItemMemo
        fields = "__all__"
