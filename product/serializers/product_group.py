from drf_spectacular.utils import extend_schema_serializer
from django.db import models
from rest_framework import serializers
from django_grpc_framework import proto_serializers

from gen.pyalloff.productGroup_pb2 import (
    CreateProductGroupRequest,
    EditProductGroupRequest,
    ListProductGroupsRequest,
    ListProductGroupsResponse,
    ProductGroupMessage,
    ProductInGroupMessage,
    ProductPriorityMessage,
    ProductsInPgRequest,
    RemoveProductInPgRequest,
)
from product.serializers.product import ProductSerializer
from product.serializers.brand import BrandSerializer


class ProductGroupType(models.TextChoices):
    PRODUCT_GROUP_TIMEDEAL = "PRODUCT_GROUP_TIMEDEAL"
    PRODUCT_GROUP_EXHIBITION = "PRODUCT_GROUP_EXHIBITION"
    PRODUCT_GROUP_BRAND_TIMEDEAL = "PRODUCT_GROUP_BRAND_TIMEDEAL"
    PRODUCT_GROUP_GROUPDEAL = "PRODUCT_GROUP_GROUPDEAL"


class ProductInGroupSerializer(proto_serializers.ProtoSerializer):
    priority = serializers.IntegerField()
    product = ProductSerializer()

    class Meta:
        proto_class = ProductInGroupMessage


class ProductGroupSerializer(proto_serializers.ProtoSerializer):
    title = serializers.CharField(max_length=50)
    short_title = serializers.CharField(max_length=20)
    instruction = serializers.ListField(child=serializers.CharField())
    image_url = serializers.CharField()
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    products = ProductInGroupSerializer(many=True)
    group_type = serializers.ChoiceField(ProductGroupType.choices)
    product_group_id = serializers.CharField()
    brand = BrandSerializer()

    class Meta:
        proto_class = ProductGroupMessage


class CreateProductGroupSeriazlier(proto_serializers.ProtoSerializer):
    title = serializers.CharField(max_length=50)
    short_title = serializers.CharField(
        max_length=20, allow_blank=True, allow_null=True, required=False
    )
    instruction = serializers.ListField(child=serializers.CharField())
    image_url = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    group_type = serializers.ChoiceField(ProductGroupType.choices)
    brand_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        proto_class = CreateProductGroupRequest


class EditProductGroupSerializer(proto_serializers.ProtoSerializer):
    title = serializers.CharField(max_length=50, allow_null=True, required=False)
    short_title = serializers.CharField(
        max_length=20, allow_blank=True, allow_null=True, required=False
    )
    instruction = serializers.ListField(child=serializers.CharField(), required=False)
    image_url = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    start_time = serializers.DateTimeField(allow_null=True, required=False)
    finish_time = serializers.DateTimeField(allow_null=True, required=False)
    group_type = serializers.ChoiceField(
        ProductGroupType.choices, allow_null=True, required=False
    )
    brand_id = serializers.CharField(allow_null=True, required=False)
    product_group_id = serializers.CharField()

    class Meta:
        proto_class = EditProductGroupRequest


class ListProductGroupRequestSerializer(proto_serializers.ProtoSerializer):
    offset = serializers.IntegerField(allow_null=True, required=False)
    limit = serializers.IntegerField(allow_null=True, required=False)
    search_query = serializers.CharField(required=False)
    group_type = serializers.ChoiceField(ProductGroupType.choices, required=False)

    class Meta:
        proto_class = ListProductGroupsRequest


@extend_schema_serializer(many=False)
class ListProductGroupResponseSerializer(proto_serializers.ProtoSerializer):
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    total_counts = serializers.IntegerField()
    pgs = ProductGroupSerializer(many=True)

    class Meta:
        proto_class = ListProductGroupsResponse


class ProductPrioritySerializer(proto_serializers.ProtoSerializer):
    product_id = serializers.CharField()
    priority = serializers.IntegerField()

    class Meta:
        proto_class = ProductPriorityMessage


class ProductsInPgSerializer(proto_serializers.ProtoSerializer):
    product_group_id = serializers.CharField()
    product_priorities = ProductPrioritySerializer(many=True)

    class Meta:
        proto_class = ProductsInPgRequest


class RemoveProductInPgSerializer(proto_serializers.ProtoSerializer):
    product_id = serializers.CharField()
    product_group_id = serializers.CharField()

    class Meta:
        proto_class = RemoveProductInPgRequest
