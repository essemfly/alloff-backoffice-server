from rest_framework import serializers
from django_grpc_framework import proto_serializers
from protos.product.product_pb2 import (
    EditProductRequest,
    ProductInventoryMessage,
    ListProductsRequest,
    ProductMessage,
    CreateProductRequest,
    ProductQuery,
)


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
    query = ProductQuerySerializer()
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()

    class Meta:
        proto_class = ListProductsRequest


class ListProductResultSerializer(proto_serializers.ProtoSerializer):
    products = ProductSerializer(many=True)
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    total_counts = serializers.IntegerField()
    list_query = ProductQuerySerializer()


class CreateProductRequestSerializer(proto_serializers.ProtoSerializer):
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


class EditProductRequestSerializer(proto_serializers.ProtoSerializer):
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