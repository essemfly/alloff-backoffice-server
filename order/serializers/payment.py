from rest_framework_mongoengine.serializers import DynamicDocumentSerializer
from tagger.core.mongo.models.order import Payment


class PaymentSerializer(DynamicDocumentSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
