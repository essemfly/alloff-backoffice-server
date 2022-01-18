from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from tagger.serializers.admin import AdminSerializer
from tagger.models.order_action_log import (
    OrderActionLog,
    OrderRefundUpdateLog,
    OrderStatusChangeLog,
    OrderAlimtalkLog,
)


class OrderAlimtalkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAlimtalkLog
        exclude = ["action_log", "created_at"]


class OrderRefundUpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRefundUpdateLog
        exclude = ["action_log", "created_at"]


class OrderStatusChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusChangeLog
        exclude = ["action_log", "created_at"]


class OrderActionLogSerializer(serializers.ModelSerializer):
    admin = AdminSerializer()
    alimtalk = serializers.SerializerMethodField()
    status_change = serializers.SerializerMethodField()
    refund_update = serializers.SerializerMethodField()

    @extend_schema_field(OrderRefundUpdateLogSerializer)
    def get_refund_update(self, obj: OrderActionLog):
        try:
            return OrderRefundUpdateLogSerializer(obj.orderrefundupdatelog).data
        except:
            return None

    @extend_schema_field(OrderAlimtalkLogSerializer)
    def get_alimtalk(self, obj: OrderActionLog):
        try:
            return OrderAlimtalkLogSerializer(obj.orderalimtalklog).data
        except:
            return None

    @extend_schema_field(OrderStatusChangeLogSerializer)
    def get_status_change(self, obj: OrderActionLog):
        try:
            return OrderStatusChangeLogSerializer(obj.orderstatuschangelog).data
        except:
            return None

    class Meta:
        model = OrderActionLog
        fields = "__all__"
