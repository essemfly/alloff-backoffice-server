from rest_framework_mongoengine.serializers import DocumentSerializer

from tagger.core.mongo.models.brand import Brand


class BrandSerializer(DocumentSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
