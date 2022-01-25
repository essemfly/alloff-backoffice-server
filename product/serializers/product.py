from rest_framework import serializers
from django_grpc_framework import proto_serializers
from protos.product.product_pb2 import (
    EditProductRequest,
    InventoryMessage,
    ListProductsRequest,
    ProductMessage,
    CreateProductRequest,
    ProductQuery,
)


class InventorySerializer(proto_serializers.ProtoSerializer):
    size = serializers.CharField()
    quantity = serializers.IntegerField()

    class Meta:
        proto_class = InventoryMessage


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
    inventory = InventorySerializer(many=True)

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


class CreateProductRequestSerializer(proto_serializers.ProtoSerializer):
    alloff_name = serializers.CharField()
    is_foreign_delivery = serializers.BooleanField()
    product_id = serializers.CharField(allow_null=True, required=False)
    original_price = serializers.IntegerField(allow_null=True, required=False)
    discounted_price = serializers.IntegerField()
    special_price = serializers.IntegerField(allow_null=True, required=False)
    brand_key_name = serializers.CharField()
    inventory = InventorySerializer(many=True)
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
    alloff_name = serializers.CharField(allow_null=True)
    is_foreign_delivery = serializers.BooleanField(allow_null=True)
    product_id = serializers.CharField(allow_null=True)
    original_price = serializers.IntegerField(allow_null=True)
    discounted_price = serializers.IntegerField(allow_null=True)
    special_price = serializers.IntegerField(allow_null=True)
    brand_key_name = serializers.CharField(allow_null=True)
    inventory = InventorySerializer(many=True, allow_null=True)
    description = serializers.ListField(child=serializers.CharField(), allow_null=True)
    is_refund_possible = serializers.BooleanField(allow_null=True)
    images = serializers.ListField(child=serializers.CharField(), allow_null=True)
    description_images = serializers.ListField(
        child=serializers.CharField(), allow_null=True
    )
    earliest_delivery_days = serializers.IntegerField(allow_null=True)
    latest_delivery_days = serializers.IntegerField(allow_null=True)
    refund_fee = serializers.IntegerField(allow_null=True)
    is_removed = serializers.BooleanField(allow_null=True)
    alloff_product_id = serializers.CharField()

    class Meta:
        proto_class = EditProductRequest
