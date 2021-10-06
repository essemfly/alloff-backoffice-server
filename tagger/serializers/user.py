from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer
from tagger.core.mongo.models.user import AlloffUser


class UserSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = AlloffUser
        fields = "__all__"
