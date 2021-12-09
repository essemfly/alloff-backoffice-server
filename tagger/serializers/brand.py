from rest_framework_mongoengine.serializers import DocumentSerializer
from datetime import datetime

from tagger.core.mongo.models.brand import Brand


class BrandSerializer(DocumentSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

    def create(self, validated_data):
        brand: Brand = Brand.objects.create(**validated_data)
        brand.created = datetime.now()
        brand.modulename = "nomodule"
        brand.inmaintenance = False
        brand.category = None
        brand.maxdiscountrate = 0
        brand.numnewproducts = 0

        brand.save()
        return brand
