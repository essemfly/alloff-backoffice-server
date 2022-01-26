from office.serializers.inventory import InventorySerializer
from rest_framework import serializers
from django_grpc_framework import proto_serializers


class ShippingNoticeItemSerializer(proto_serializers.ProtoSerializer):
    id = serializers.IntegerField()
    inventory = InventorySerializer()
    order_item_id = serializers.IntegerField()
