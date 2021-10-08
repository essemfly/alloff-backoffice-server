from rest_framework_mongoengine.serializers import (
    DynamicDocumentSerializer,
)

from tagger.core.mongo.models.alloff_product import AlloffProduct, AlloffProductTemplate


class TimedealProductTemplateSerializer(DynamicDocumentSerializer):
    class Meta:
        model = AlloffProductTemplate
        fields = "__all__"


class TimedealProductSerializer(DynamicDocumentSerializer):
    class Meta:
        model = AlloffProduct
        fields = "__all__"
