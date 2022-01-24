from rest_framework import serializers
from django_grpc_framework import proto_serializers

from logistics.models import ReceivedItem, ReceivedItemStatus
from logistics.protos.received_item_proto import received_item_pb2
from logistics.serializers.inventory import InventorySerializer


class ReceivedItemProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = ReceivedItem
        proto_class = received_item_pb2.ReceivedItem
        fields = "__all__"


class ReceivedItemSerializer(serializers.Serializer):
    order_id = serializers.CharField(max_length=50)
    order_item_id = serializers.CharField(max_length=50)
    code = serializers.CharField(max_length=30)
    status = serializers.ChoiceField(
        choices=ReceivedItemStatus.choices,
        default=ReceivedItemStatus.SOURCING_REQUIRED,
    )

    # product
    product_id = serializers.CharField(max_length=50)
    product_name = serializers.CharField(max_length=50)
    product_brand_id = serializers.CharField(max_length=50)
    product_brand_name = serializers.CharField(max_length=50)
    product_size = serializers.CharField(max_length=20)
    product_color = serializers.CharField(max_length=20)

    # inventory
    inventory = InventorySerializer()

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    deleted_at = serializers.DateTimeField(allow_null=True)
