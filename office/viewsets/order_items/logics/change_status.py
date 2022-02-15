from office.serializers.order_item import OrderItemStatus
from rest_framework import fields, serializers


class ChangeStatusSerializer(serializers.Serializer):
    status = fields.ChoiceField(OrderItemStatus.choices, required=True)
    tracking_number = fields.CharField(required=False, allow_null=True)
    tracking_url = fields.CharField(required=False, allow_null=True)
    courier_id = fields.IntegerField(required=False, allow_null=True)


class ApiTrackingInfoSerializer(serializers.Serializer):
    tracking_number = fields.CharField()
    tracking_url = fields.CharField(required=False, allow_null=True)
    courier_id = fields.IntegerField()
