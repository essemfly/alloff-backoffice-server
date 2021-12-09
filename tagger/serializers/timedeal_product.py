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
    class Meta:
        model = AlloffProduct
        fields = [
            "canceldescription",
            "deliverydescription",
            "sizedescription",
            "brand",
            "instruction.description",
            "instruction.title",
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
        ]

    def create(self, validated_data):
        prod = AlloffProduct(**validated_data)
        prod.brand._id = validated_data.get("brandid")
        prod.save()
        return prod

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
