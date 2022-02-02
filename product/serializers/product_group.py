from rest_framework import serializers
from django_grpc_framework import proto_serializers

from protos.product.productGroup_pb2 import (
    CreateProductGroupRequest,
    EditProductGroupRequest,
    ProductGroupMessage,
    ProductInGroupMessage,
    ProductPriorityMessage,
    PushProductsInPgRequest,
    RemoveProductInPgRequest,
)
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
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    products = ProductInGroupSerializer(many=True)
    product_group_id = serializers.CharField()

    class Meta:
        proto_class = ProductGroupMessage


class CreateProductGroupSeriazlier(proto_serializers.ProtoSerializer):
    title = serializers.CharField(max_length=50)
    short_title = serializers.CharField(max_length=20)
    instruction = serializers.ListField(child=serializers.CharField())
    image_url = serializers.URLField()
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()

    class Meta:
        proto_class = CreateProductGroupRequest


class EditProductGroupSerializer(proto_serializers.ProtoSerializer):
    title = serializers.CharField(max_length=50, allow_null=True, required=False)
    short_title = serializers.CharField(max_length=20, allow_null=True, required=False)
    instruction = serializers.ListField(child=serializers.CharField(), required=False)
    image_url = serializers.URLField(allow_null=True, required=False)
    start_time = serializers.DateTimeField(allow_null=True, required=False)
    finish_time = serializers.DateTimeField(allow_null=True, required=False)
    products = ProductInGroupSerializer(many=True, allow_null=True, required=False)
    product_group_id = serializers.CharField()

    class Meta:
        proto_class = EditProductGroupRequest


class ProductPrioritySerializer(proto_serializers.ProtoSerializer):
    product_id = serializers.CharField()
    priority = serializers.IntegerField()

    class Meta:
        proto_class = ProductPriorityMessage


class PushProductsSerializer(proto_serializers.ProtoSerializer):
    product_group_id = serializers.CharField()
    product_priority = ProductPrioritySerializer(many=True)

    class Meta:
        proto_class = PushProductsInPgRequest


class RemoveProductInProductGroupSerializer(proto_serializers.ProtoSerializer):
    product_id = serializers.CharField()
    product_group_id = serializers.CharField()

    class Meta:
        proto_class = RemoveProductInPgRequest
