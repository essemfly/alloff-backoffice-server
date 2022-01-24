from rest_framework_mongoengine.serializers import DocumentSerializer
from tagger.core.mongo.models.order import Refund


class RefundSerializer(DocumentSerializer):
    class Meta:
        model = Refund
        fields = "__all__"
