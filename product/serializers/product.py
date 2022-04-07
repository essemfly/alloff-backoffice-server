from alloff_backoffice_server.settings import (IMAGE_CACHING_SETTINGS,
                                               THUMBNAIL_SETTINGS)
from django.db import models
from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_field, extend_schema_serializer
from gen.pyalloff.product_pb2 import (CreateProductRequest, EditProductRequest,
                                      ListProductsRequest,
                                      ListProductsResponse,
                                      ProductInventoryMessage, ProductMessage,
                                      ProductQuery)
from rest_framework import serializers


class SortingOptions(models.TextChoices):
    PRICE_ASCENDING = "PRICE_ASCENDING"
    PRICE_DESCENDING = "PRICE_DESCENDING"
    DISCOUNT_0_30 = "DISCOUNT_0_30"
    DISCOUNT_30_50 = "DISCOUNT_30_50"
    DISCOUNT_50_70 = "DISCOUNT_50_70"
    DISCOUNT_70_100 = "DISCOUNT_70_100"
    DISCOUNTRATE_ASCENDING = "DISCOUNTRATE_ASCENDING"
    DISCOUNTRATE_DESCENDING = "DISCOUNTRATE_DESCENDING"


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
    alloff_category_id = serializers.CharField(allow_null=True, required=False)
    product_url = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
    is_classified_done = serializers.BooleanField()
    is_classified_touched = serializers.BooleanField()
    description_infos = serializers.DictField()
    product_infos = serializers.DictField()
    thumbnail_image = serializers.CharField(allow_null=True, required=False)

    # Backoffice-only field (non-grpc)
    main_image_url = serializers.SerializerMethodField()

    @extend_schema_field(serializers.CharField)
    def get_main_image_url(self, obj):
        try:
            if obj.thumbnail_image == "" or obj.thumbnail_image is None:
                try:
                    return obj.images[0]
                except IndexError:
                    return None

            def __get_filename_only(__url: str):
                __file = __url.split("/")[-1]
                __filename = __file.split("?")[0].split(".")[0]
                return (
                    __filename.replace(IMAGE_CACHING_SETTINGS["SUFFIX"], "")
                    .replace(THUMBNAIL_SETTINGS["SUFFIX"], "")
                    .replace(f"-mw{THUMBNAIL_SETTINGS['SIZE']}", "")
                    .replace(f"-mw{IMAGE_CACHING_SETTINGS['SIZE']}", "")
                )

            image_names = {__get_filename_only(__image): __image for __image in obj.images}
            thumbnail_image_name = __get_filename_only(obj.thumbnail_image)
            for name, url in image_names.items():
                if thumbnail_image_name == name:
                    return url
            return obj.images[0]
        except AttributeError:
            return obj.images[0]

    class Meta:
        proto_class = ProductMessage


class ProductQuerySerializer(proto_serializers.ProtoSerializer):
    search_query = serializers.CharField()
    brand_id = serializers.CharField()
    category_id = serializers.CharField()
    alloff_category_id = serializers.CharField()
    options = serializers.ListField(
        child=serializers.ChoiceField(SortingOptions.choices)
    )
    is_classified_done = serializers.BooleanField()

    class Meta:
        proto_class = ProductQuery


class ListProductSerializer(proto_serializers.ProtoSerializer):
    search_query = serializers.CharField(allow_null=True, required=False)
    brand_id = serializers.CharField(allow_null=True, required=False)
    category_id = serializers.CharField(allow_null=True, required=False)
    alloff_category_id = serializers.CharField(allow_null=True, required=False)
    offset = serializers.IntegerField(allow_null=True, required=False)
    limit = serializers.IntegerField(allow_null=True, required=False)
    is_classified_done = serializers.BooleanField(allow_null=True, required=False)

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
    product_id = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
    product_url = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
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
    alloff_category_id = serializers.CharField(allow_null=True, required=False)
    description_infos = serializers.DictField(allow_null=True, required=False)
    product_infos = serializers.DictField(allow_null=True, required=False)
    thumbnail_image = serializers.CharField(allow_null=True, required=False)

    class Meta:
        proto_class = CreateProductRequest


class CreateProductRequestApiSerializer(_CreateProductRequestSerializer):
    raw_html = serializers.CharField(allow_null=True, required=False)


class CreateProductRequestGrpcSerializer(_CreateProductRequestSerializer):
    module_name = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )


class _EditProductRequestSerializer(proto_serializers.ProtoSerializer):
    alloff_name = serializers.CharField(allow_null=True, required=False)
    is_foreign_delivery = serializers.BooleanField(allow_null=True, required=False)
    product_id = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
    product_url = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
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
    is_soldout = serializers.BooleanField(allow_null=True, required=False)
    alloff_category_id = serializers.CharField(allow_null=True, required=False)
    description_infos = serializers.DictField(allow_null=True, required=False)
    product_infos = serializers.DictField(allow_null=True, required=False)
    thumbnail_image = serializers.CharField(allow_null=True, required=False)

    class Meta:
        proto_class = EditProductRequest


class EditProductRequestApiSerializer(_EditProductRequestSerializer):
    raw_html = serializers.CharField(allow_null=True, required=False)

    class Meta:
        proto_class = EditProductRequest


class EditProductRequestGrpcSerializer(_EditProductRequestSerializer):
    alloff_product_id = serializers.CharField()
    module_name = serializers.CharField(
        allow_null=True, allow_blank=True, required=False
    )
