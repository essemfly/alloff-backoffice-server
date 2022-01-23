from rest_framework import serializers
from django_grpc_framework import proto_serializers

from protos.product.productGroup_pb2 import ProductGroupMessage, ProductInGroupMessage
from protos.product.product_pb2 import ProductMessage
from product.serializers.product import ProductSerializer


class ProductInGroupSerializer(proto_serializers.ProtoSerializer):
    priority = serializers.IntegerField()
    product = ProductSerializer()

    class Meta:
        proto_class = ProductInGroupMessage


class ProductGroupSerializer(proto_serializers.ProtoSerializer):
    title = serializers.CharField(max_length=50)
    short_title = serializers.CharField(max_length=20)
    instruction = serializers.ListField(serializers.CharField())
    image_url = serializers.URLField()
    start_time = serializers.DateTimeField
    finish_time = serializers.DateTimeField
    products = ProductInGroupSerializer(many=True)
    product_group_id = serializers.CharField()

    class Meta:
        proto_class = ProductGroupMessage
