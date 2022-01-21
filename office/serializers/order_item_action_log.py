from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from office.serializers.admin import AdminSerializer
from order.models.order_item_action_log import (
    OrderItemActionLog,
    OrderItemRefundUpdateLog,
    OrderItemStatusChangeLog,
    OrderItemAlimtalkLog,
)


class OrderItemAlimtalkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemAlimtalkLog
        exclude = ["action_log", "created_at"]


class OrderItemRefundUpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemRefundUpdateLog
        exclude = ["action_log", "created_at"]


class OrderItemStatusChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemStatusChangeLog
        exclude = ["action_log", "created_at"]


class OrderItemActionLogSerializer(serializers.ModelSerializer):
    admin = AdminSerializer()
    alimtalk = serializers.SerializerMethodField()
    status_change = serializers.SerializerMethodField()
    refund_update = serializers.SerializerMethodField()

    @extend_schema_field(OrderItemRefundUpdateLogSerializer)
    def get_refund_update(self, obj: OrderItemActionLog):
        try:
            return OrderItemRefundUpdateLogSerializer(obj.OrderItemrefundupdatelog).data
        except:
            return None

    @extend_schema_field(OrderItemAlimtalkLogSerializer)
    def get_alimtalk(self, obj: OrderItemActionLog):
        try:
            return OrderItemAlimtalkLogSerializer(obj.OrderItemalimtalklog).data
        except:
            return None

    @extend_schema_field(OrderItemStatusChangeLogSerializer)
    def get_status_change(self, obj: OrderItemActionLog):
        try:
            return OrderItemStatusChangeLogSerializer(obj.OrderItemstatuschangelog).data
        except:
            return None

    class Meta:
        model = OrderItemActionLog
        fields = "__all__"
