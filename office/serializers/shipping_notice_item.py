from office.serializers.inventory import InventorySerializer
from rest_framework import fields
from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_field
from office.serializers.order_item import OrderItemListSerializer
from office.serializers.package import PackageSerializer
from protos.logistics.shipping_notice_item import shipping_notice_item_pb2

class ShippingNoticeItemSerializer(proto_serializers.ProtoSerializer):
    id = fields.IntegerField()
    notice_id = fields.IntegerField()
    inventory = InventorySerializer()
    order_item = OrderItemListSerializer()


    package = fields.SerializerMethodField(allow_null=True)
    
    @extend_schema_field(PackageSerializer(allow_null=True))
    def get_package(self, obj):
        if obj.package and obj.package.status != "":
            return PackageSerializer(obj.package).data
        return None

    class Meta:
        proto_class = shipping_notice_item_pb2.ShippingNoticeItem