from tkinter import image_names
from rest_framework import serializers
from django_grpc_framework import proto_serializers
from protos.product.product_pb2 import (
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
    description = serializers.ListField(serializers.CharField())
    images = serializers.ListField(serializers.URLField())
    description_images = serializers.ListField(serializers.URLField())
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
