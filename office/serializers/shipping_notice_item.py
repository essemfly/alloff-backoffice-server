from office.serializers.inventory import InventorySerializer
from rest_framework import serializers


class ShippingNoticeItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    inventory = InventorySerializer()
