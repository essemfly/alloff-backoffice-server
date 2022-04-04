from django.db import models
from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_serializer
from gen.pyalloff.hometab_pb2 import (CreateHomeTabItemRequest,
                                      EditHomeTabItemRequest,
                                      HomeTabItemMessage,
                                      HomeTabItemReferenceMessage,
                                      ItemRequester, ListHomeTabItemsRequest,
                                      ListHomeTabItemsResponse)
from rest_framework import serializers

from product.serializers.brand import BrandSerializer
from product.serializers.exhibition import ExhibitionSerializer
from product.serializers.product import ProductSerializer, SortingOptions


class ItemTypes(models.TextChoices):
    HOMETAB_ITEM_BRANDS = "HOMETAB_ITEM_BRANDS"
    HOMETAB_ITEM_EXHIBITION_A = "HOMETAB_ITEM_EXHIBITION_A"
    HOMETAB_ITEM_EXHIBITIONS = "HOMETAB_ITEM_EXHIBITIONS"
    HOMETAB_ITEM_EXHIBITION = "HOMETAB_ITEM_EXHIBITION"
    HOMETAB_ITEM_PRODUCTS_BRANDS = "HOMETAB_ITEM_PRODUCTS_BRANDS"
    HOMETAB_ITEM_PRODUCTS_CATEGORIES = "HOMETAB_ITEM_PRODUCTS_CATEGORIES"


class ItemRequesterSerializer(proto_serializers.ProtoSerializer):
    item_type = serializers.ChoiceField(ItemTypes.choices)
    brand_keynames = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    exhibition_ids = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    alloffcategory_id = serializers.CharField(allow_null=True, required=False)
    options = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    product_ids = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )

    class Meta:
        proto_class = ItemRequester


class HomeTabItemReferenceSerializer(proto_serializers.ProtoSerializer):
    path = serializers.CharField()
    params = serializers.CharField()
    options = serializers.MultipleChoiceField(choices=SortingOptions.choices)

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
    is_live = serializers.BooleanField()

    class Meta:
        proto_class = HomeTabItemMessage


class CreateHomeTabSerializer(proto_serializers.ProtoSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    tags = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    back_image_url = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    contents = ItemRequesterSerializer()
    weight = serializers.IntegerField()

    class Meta:
        proto_class = CreateHomeTabItemRequest


class EditHomeTabSerializer(proto_serializers.ProtoSerializer):
    hometab_id = serializers.CharField()
    title = serializers.CharField(allow_null=True, required=False, allow_blank=True)
    description = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
    tags = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    back_image_url = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
    start_time = serializers.DateTimeField(allow_null=True, required=False)
    finish_time = serializers.DateTimeField(allow_null=True, required=False)
    contents = ItemRequesterSerializer(allow_null=True, required=False)
    weight = serializers.IntegerField(allow_null=True, required=False)
    is_live = serializers.BooleanField(allow_null=True, required=False)

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
