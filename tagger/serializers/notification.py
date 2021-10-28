from rest_framework_mongoengine.serializers import DocumentSerializer

from tagger.core.mongo.models.notification import Notification


class NotificationSerializer(DocumentSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
