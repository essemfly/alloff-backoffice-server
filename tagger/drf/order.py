from tagger.core.mongo.models.user import User
from tagger.core.iamport import IMP
from rest_framework_mongoengine import viewsets
from rest_framework_mongoengine.serializers import (
    DynamicDocumentSerializer,
    EmbeddedDocumentSerializer,
)
from tagger.core.drf.search_filter import CustomSearchFilter
from tagger.core.mongo.models.order import Order, OrderStatus, Payment
from rest_framework.serializers import SerializerMethodField


class UserSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(DynamicDocumentSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class OrderSerializer(DynamicDocumentSerializer):
    iamport = SerializerMethodField()
    payment = SerializerMethodField()
    user = UserSerializer(many=False)

    def get_payment(self, obj):
        payment = Payment.objects(merchantuid=str(obj.id)).first()
        return PaymentSerializer(payment, many=False).data if payment else None

    def get_iamport(self, obj):
        return IMP.instance().get_payment_detail(obj.id)

    class Meta:
        model = Order
        fields = "__all__"


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects(orderstatus__nin=["CREATED", "RECREATED"])
    filter_backends = [CustomSearchFilter]
    search_fields = ["user__mobile"]
