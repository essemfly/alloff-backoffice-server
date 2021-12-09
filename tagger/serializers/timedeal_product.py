from datetime import datetime
from os import remove
from rest_framework_mongoengine.serializers import (
    DynamicDocumentSerializer,
)
from rest_framework import serializers

from tagger.core.mongo.models.brand import Brand
from tagger.core.mongo.models.alloff_product import AlloffProduct, AlloffProductTemplate
from tagger.models import inventory


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
            "brandid",
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
        ]

    def create(self, validated_data):
        brand: Brand = Brand.objects.get(id=validated_data.get("brandid"))
        brand_object = {
            "_id": str(brand.id),
            "keyname": brand.keyname,
            "korname": brand.korname,
            "engname": brand.engname,
            "logoimgurl": brand.logoimgurl,
            "onpopular": brand.onpopular,
            "description": brand.description,
            "isopen": brand.isopen,
            "ishide": brand.ishide,
            "modulename": brand.modulename,
            "maxdiscountrate": brand.maxdiscountrate,
            "numnewproducts": brand.numnewproducts,
            "sizeguide": brand.sizeguide,
            "category": brand.category,
            "created": brand.created,
            "inmaintenance": False,
        }

        prod: AlloffProduct = AlloffProduct.objects.create(
            brand=brand_object,
            canceldescription=validated_data.get("canceldescription"),
            deliverydescription=validated_data.get("deliverydescription"),
            description=validated_data.get("description"),
            discountedprice=validated_data.get("discountedprice"),
            discountrate=validated_data.get("discountrate"),
            faults=validated_data.get("faults"),
            images=validated_data.get("images"),
            instruction=validated_data.get("instruction"),
            name=validated_data.get("name"),
            originalprice=validated_data.get("originalprice"),
            producttype=validated_data.get("producttype"),
            sizedescription=validated_data.get("sizedescription"),
            productgroupid=validated_data.get("productgroupid"),
            inventory=validated_data.get("inventory"),
            soldout=validated_data.get("soldout"),
            created=datetime.now(),
            updated=datetime.now(),
            removed=False,
        )
        # TO BE FIXED: Serializer와 viewset에서의 관계에 대한 공부 필요.
        prod.brandid = validated_data.get("brandid")
        return prod

    def update(self, instance, validated_data):
        brand: Brand = Brand.objects.get(id=validated_data.get("brandid"))
        brand_object = {
            "_id": str(brand.id),
            "keyname": brand.keyname,
            "korname": brand.korname,
            "engname": brand.engname,
            "logoimgurl": brand.logoimgurl,
            "onpopular": brand.onpopular,
            "description": brand.description,
            "isopen": brand.isopen,
            "ishide": brand.ishide,
            "modulename": brand.modulename,
            "maxdiscountrate": brand.maxdiscountrate,
            "numnewproducts": brand.numnewproducts,
            "sizeguide": brand.sizeguide,
            "category": brand.category,
            "created": brand.created,
            "inmaintenance": False,
        }

        instance.update(
            brand=brand_object,
            canceldescription=validated_data.get("canceldescription"),
            deliverydescription=validated_data.get("deliverydescription"),
            description=validated_data.get("description"),
            discountedprice=validated_data.get("discountedprice"),
            discountrate=validated_data.get("discountrate"),
            faults=validated_data.get("faults"),
            images=validated_data.get("images"),
            instruction=validated_data.get("instruction"),
            name=validated_data.get("name"),
            originalprice=validated_data.get("originalprice"),
            producttype=validated_data.get("producttype"),
            sizedescription=validated_data.get("sizedescription"),
            productgroupid=validated_data.get("productgroupid"),
            inventory=validated_data.get("inventory"),
            soldout=validated_data.get("soldout"),
            updated=datetime.now(),
            removed=False,
        )

        instance.save()
        # TO BE FIXED: Serializer와 viewset에서의 관계에 대한 공부 필요.
        instance.brandid = validated_data.get("brandid")
        return instance
