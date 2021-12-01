from datetime import datetime
from rest_framework_mongoengine.serializers import (
    DynamicDocumentSerializer,
)
from rest_framework import serializers

from tagger.core.mongo.models.brand import Brand
from tagger.core.mongo.models.alloff_product import AlloffProduct, AlloffProductTemplate


class TimedealProductTemplateSerializer(DynamicDocumentSerializer):
    class Meta:
        model = AlloffProductTemplate
        fields = "__all__"


class TimedealProductSerializer(DynamicDocumentSerializer):
    class Meta:
        model = AlloffProduct
        fields = "__all__"


class TimedealProductAddSerializer(DynamicDocumentSerializer):
    brandid = serializers.CharField()

    class Meta:
        model = AlloffProduct
        fields = [
            "canceldescription",
            "deliverydescription",
            "sizedescription",
            "instruction",
            "faults",
            "description",
            "originalprice",
            "discountedprice",
            "discountrate",
            "inventory",
            "producttype",
            "soldout",
            "images",
            "name",
            "productgroupid",
            "brandid",
        ]

    def create(self, validated_data):
        brandid = validated_data.get("brandid")
        brand = Brand.objects.get(id=brandid)

        AlloffProduct(
            brand=brand,
            created=datetime.now(),
            updated=datetime.now(),
            **validated_data
        )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
