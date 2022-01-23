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
    alimtalk = OrderItemAlimtalkLogSerializer(allow_null=True)
    status_change = OrderItemStatusChangeLogSerializer(allow_null=True)
    refund_update = OrderItemRefundUpdateLogSerializer(allow_null=True)

    class Meta:
        model = OrderItemActionLog
        fields = "__all__"
