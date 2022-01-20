from rest_framework import serializers
from django_grpc_framework import proto_serializers

from logistics.models import Inventory, InventoryStatus
from logistics.protos.inventory_proto import inventory_pb2


class InventoryProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Inventory
        proto_class = inventory_pb2.Inventory
        fields = "__all__"


class InventorySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=30)
    status = serializers.ChoiceField(
        choices=InventoryStatus.choices, default=InventoryStatus.CREATED
    )

    # product
    product_id = serializers.CharField(max_length=50)
    product_name = serializers.CharField(max_length=50)
    product_brand_id = serializers.CharField(max_length=50)
    product_brand_name = serializers.CharField(max_length=50)
    product_size = serializers.CharField(max_length=20)
    product_color = serializers.CharField(max_length=20)

    # package = serializers.ForeignKey(
    #     Package,
    #     on_delete=serializers.DO_NOTHING,
    #     allow_null=True,
    #     allow_blank=True,
    #     related_name="inventory",
    # )

    location = serializers.CharField(max_length=50, allow_null=False, allow_blank=True)
    memo = serializers.CharField(allow_null=False, allow_blank=True)

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    deleted_at = serializers.DateTimeField()
