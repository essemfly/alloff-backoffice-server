from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from tagger.serializers.admin import AdminSerializer
from tagger.models.order_action_log import (
    OrderActionLog,
    OrderStatusChangeLog,
    OrderAlimtalkLog,
)


class OrderAlimtalkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAlimtalkLog
        exclude = ["action_log", "created_at"]


class OrderStatusChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusChangeLog
        exclude = ["action_log", "created_at"]


class OrderActionLogSerializer(serializers.ModelSerializer):
    admin = AdminSerializer()
    alimtalk = serializers.SerializerMethodField()
    status_change = serializers.SerializerMethodField()

    @swagger_serializer_method(serializer_or_field=OrderAlimtalkLogSerializer)
    def get_alimtalk(self, obj: OrderActionLog):
        try:
            return OrderAlimtalkLogSerializer(obj.orderalimtalklog).data
        except:
            return None

    @swagger_serializer_method(serializer_or_field=OrderStatusChangeLogSerializer)
    def get_status_change(self, obj: OrderActionLog):
        try:
            return OrderStatusChangeLogSerializer(obj.orderstatuschangelog).data
        except:
            return None

    class Meta:
        model = OrderActionLog
        fields = "__all__"
