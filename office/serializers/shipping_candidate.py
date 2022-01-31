from django_grpc_framework import proto_serializers
from office.serializers.inventory import InventorySerializer
from office.serializers.order_item import OrderItemRetrieveSerializer
from protos.logistics.shipping_candidate import shipping_candidate_pb2
from protos.logistics.shipping_notice import shipping_notice_pb2
from rest_framework import fields


class ShippingCandidateProtoSerializer(proto_serializers.ProtoSerializer):
    item = OrderItemRetrieveSerializer()
    inventories = InventorySerializer(many=True)
    is_fulfilled = fields.BooleanField()

    class Meta:
        proto_class = shipping_candidate_pb2.ShippingCandidate


class ShippingCandidateSubmitItemProtoSerializer(proto_serializers.ProtoSerializer):
    order_item_id = fields.IntegerField()
    inventory_ids = fields.ListField(child=fields.IntegerField())

    class Meta:
        proto_class = shipping_notice_pb2.ShippingNoticeCandidateSubmitItem
