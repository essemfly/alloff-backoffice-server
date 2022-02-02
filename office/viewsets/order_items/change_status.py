from rest_framework import fields, serializers

from office.serializers.order_item import OrderItemStatus

class ChangeStatusSerializer(serializers.Serializer):
    status = fields.ChoiceField(OrderItemStatus.choices, required=True)
    tracking_number = fields.CharField(required=False, allow_null=True)
    tracking_url = fields.CharField(required=False, allow_null=True)
