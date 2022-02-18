from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from django.db import models
from django_grpc_framework import proto_serializers
from product.serializers.brand import BrandSerializer
from product.serializers.exhibition import ExhibitionSerializer
from product.serializers.product import ProductSerializer
from protos.product.hometab_pb2 import (
    HomeTabItemReferenceMessage,
    HomeTabItemMessage,
    CreateHomeTabItemRequest,
    EditHomeTabItemRequest,
    ItemRequester,
    ListHomeTabItemsRequest,
    ListHomeTabItemsResponse,
)


class ItemTypes(models.TextChoices):
    HOMETAB_ITEM_BRANDS = "HOMETAB_ITEM_BRANDS"
    HOMETAB_ITEM_BRAND_EXHIBITION = "HOMETAB_ITEM_BRAND_EXHIBITION"
    HOMETAB_ITEM_EXHIBITIONS = "HOMETAB_ITEM_EXHIBITIONS"
    HOMETAB_ITEM_EXHIBITION = "HOMETAB_ITEM_EXHIBITION"
    HOMETAB_ITEM_PRODUCTS_A = "HOMETAB_ITEM_PRODUCTS_A"
    HOMETAB_ITEM_PRODUCTS_B = "HOMETAB_ITEM_PRODUCTS_B"


class SortingOptions(models.TextChoices):
    PRICE_ASCENDING = "PRICE_ASCENDING"
    PRICE_DESCENDING = "PRICE_DESCENDING"
    DISCOUNT_0_30 = "DISCOUNT_0_30"
    DISCOUNT_30_50 = "DISCOUNT_30_50"
    DISCOUNT_50_70 = "DISCOUNT_50_70"
    DISCOUNT_70_100 = "DISCOUNT_70_100"
    DISCOUNTRATE_ASCENDING = "DISCOUNTRATE_ASCENDING"
    DISCOUNTRATE_DESCENDING = "DISCOUNTRATE_DESCENDING"


class ItemRequesterSerializer(proto_serializers.ProtoSerializer):
    item_type = serializers.ChoiceField(ItemTypes.choices)
    brand_keynames = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    exhibition_ids = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    alloffcategory_id = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    options = serializers.MultipleChoiceField(
        SortingOptions.choices, allow_null=True, required=False)

    class Meta:
        proto_class = ItemRequester


class HomeTabItemReferenceSerializer(proto_serializers.ProtoSerializer):
    path = serializers.CharField()
    params = serializers.CharField()
    options = serializers.MultipleChoiceField(SortingOptions.choices)

    class Meta:
        proto_class = HomeTabItemReferenceMessage


class HomeTabSerializer(proto_serializers.ProtoSerializer):
    item_id = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    tags = serializers.ListField(child=serializers.CharField())
    back_image_url = serializers.CharField()
    item_type = serializers.ChoiceField(ItemTypes.choices)
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    products = ProductSerializer(many=True)
    brands = BrandSerializer(many=True)
    exhibitions = ExhibitionSerializer(many=True)
    reference = HomeTabItemReferenceSerializer()
    weight = serializers.IntegerField()

    class Meta:
        proto_class = HomeTabItemMessage


class CreateHomeTabSerializer(proto_serializers.ProtoSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    tags = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False)
    back_image_url = serializers.CharField(allow_null=True, required=False)
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    contents = ItemRequesterSerializer()
    weight = serializers.IntegerField()

    class Meta:
        proto_class = CreateHomeTabItemRequest


class EditHomeTabSerializer(proto_serializers.ProtoSerializer):
    hometab_id = serializers.CharField()
    title = serializers.CharField(allow_null=True, required=False)
    description = serializers.CharField(allow_null=True, required=False)
    tags = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    back_image_url = serializers.CharField(allow_null=True, required=False)
    start_time = serializers.DateTimeField(allow_null=True, required=False)
    finish_time = serializers.DateTimeField(allow_null=True, required=False)
    contents = ItemRequesterSerializer(allow_null=True, required=False)
    weight = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        proto_class = EditHomeTabItemRequest


class ListHomeTabsRequestSerializer(proto_serializers.ProtoSerializer):
    offset = serializers.IntegerField(allow_null=True, required=False)
    limit = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        proto_class = ListHomeTabItemsRequest


@extend_schema_serializer(many=False)
class ListHomeTabsResponseSerializer(proto_serializers.ProtoSerializer):
    items = HomeTabSerializer(many=True)
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    total_counts = serializers.IntegerField()

    class Meta:
        proto_class = ListHomeTabItemsResponse
