from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_serializer
from protos.product.product_pb2 import (CreateProductRequest,
                                        EditProductRequest,
                                        ListProductsRequest,
                                        ListProductsResponse,
                                        ProductInventoryMessage,
                                        ProductMessage, ProductQuery)
from rest_framework import serializers


class ProductInventorySerializer(proto_serializers.ProtoSerializer):
    size = serializers.CharField()
    quantity = serializers.IntegerField()

    class Meta:
        proto_class = ProductInventoryMessage


class ProductSerializer(proto_serializers.ProtoSerializer):
    alloff_product_id = serializers.CharField()
    alloff_name = serializers.CharField()
    product_id = serializers.CharField()
    brand_kor_name = serializers.CharField()
    category_name = serializers.CharField()
    alloff_category_name = serializers.CharField()
    is_foreign_delivery = serializers.BooleanField()
    is_refund_possible = serializers.BooleanField()
    is_removed = serializers.BooleanField()
    is_soldout = serializers.BooleanField()
    original_price = serializers.IntegerField()
    discounted_price = serializers.IntegerField()
    special_price = serializers.IntegerField()
    earliest_delivery_days = serializers.IntegerField()
    latest_delivery_days = serializers.IntegerField()
    refund_fee = serializers.IntegerField()
    total_score = serializers.IntegerField()
    description = serializers.ListField(child=serializers.CharField())
    images = serializers.ListField(child=serializers.CharField())
    description_images = serializers.ListField(child=serializers.URLField())
    inventory = ProductInventorySerializer(many=True)
    module_name = serializers.CharField()
    raw_html = serializers.CharField(allow_null=True, required=False)

    class Meta:
        proto_class = ProductMessage


class ProductQuerySerializer(proto_serializers.ProtoSerializer):
    search_query = serializers.CharField()
    brand_id = serializers.CharField()
    category_id = serializers.CharField()
    alloff_category_id = serializers.CharField()

    class Meta:
        proto_class = ProductQuery


class ListProductSerializer(proto_serializers.ProtoSerializer):
    search_query = serializers.CharField(allow_null=True, required=False)
    brand_id = serializers.CharField(allow_null=True, required=False)
    category_id = serializers.CharField(allow_null=True, required=False)
    alloff_category_id = serializers.CharField(allow_null=True, required=False)
    offset = serializers.IntegerField(allow_null=True, required=False)
    limit = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        proto_class = ListProductsRequest


@extend_schema_serializer(many=False)
class ListProductResultSerializer(proto_serializers.ProtoSerializer):
    products = ProductSerializer(many=True)
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    total_counts = serializers.IntegerField()
    list_query = ProductQuerySerializer()
    module_name = serializers.CharField()

    class Meta:
        proto_class = ListProductsResponse


class _CreateProductRequestSerializer(proto_serializers.ProtoSerializer):
    alloff_name = serializers.CharField()
    is_foreign_delivery = serializers.BooleanField()
    product_id = serializers.CharField(allow_null=True, required=False)
    original_price = serializers.IntegerField(allow_null=True, required=False)
    discounted_price = serializers.IntegerField()
    special_price = serializers.IntegerField(allow_null=True, required=False)
    brand_key_name = serializers.CharField()
    inventory = ProductInventorySerializer(many=True)
    description = serializers.ListField(child=serializers.CharField())
    is_refund_possible = serializers.BooleanField()
    images = serializers.ListField(child=serializers.CharField())
    description_images = serializers.ListField(child=serializers.CharField())
    earliest_delivery_days = serializers.IntegerField()
    latest_delivery_days = serializers.IntegerField()
    refund_fee = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        proto_class = CreateProductRequest


class CreateProductRequestApiSerializer(_CreateProductRequestSerializer):
    raw_html = serializers.CharField(allow_null=True, required=False)


class CreateProductRequestGrpcSerializer(_CreateProductRequestSerializer):
    module_name = serializers.CharField(allow_null=True, required=False)


class _EditProductRequestSerializer(proto_serializers.ProtoSerializer):
    alloff_name = serializers.CharField(allow_null=True, required=False)
    is_foreign_delivery = serializers.BooleanField(allow_null=True, required=False)
    product_id = serializers.CharField(allow_null=True, required=False)
    original_price = serializers.IntegerField(allow_null=True, required=False)
    discounted_price = serializers.IntegerField(allow_null=True, required=False)
    special_price = serializers.IntegerField(allow_null=True, required=False)
    brand_key_name = serializers.CharField(allow_null=True, required=False)
    inventory = ProductInventorySerializer(many=True, allow_null=True, required=False)
    description = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    is_refund_possible = serializers.BooleanField(allow_null=True, required=False)
    images = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    description_images = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    earliest_delivery_days = serializers.IntegerField(allow_null=True, required=False)
    latest_delivery_days = serializers.IntegerField(allow_null=True, required=False)
    refund_fee = serializers.IntegerField(allow_null=True, required=False)
    is_removed = serializers.BooleanField(allow_null=True, required=False)
    alloff_product_id = serializers.CharField()

    class Meta:
        proto_class = EditProductRequest


class EditProductRequestApiSerializer(_EditProductRequestSerializer):
    raw_html = serializers.CharField(allow_null=True, required=False)

    class Meta:
        proto_class = EditProductRequest


class EditProductRequestGrpcSerializer(_EditProductRequestSerializer):
    module_name = serializers.CharField(
        allow_null=True, allow_blank=True, required=False
    )
