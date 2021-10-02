from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer
from tagger.core.mongo.models.user import User


class UserSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = User
        fields = "__all__"
