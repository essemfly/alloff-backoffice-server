from rest_framework_mongoengine.serializers import (
    DynamicDocumentSerializer,
)

from tagger.core.mongo.models.alloff_product_group import AlloffProductGroup


class TimedealSerializer(DynamicDocumentSerializer):
    class Meta:
        model = AlloffProductGroup
        fields = "__all__"
