from rest_framework.serializers import SerializerMethodField
from rest_framework_mongoengine.serializers import DynamicDocumentSerializer
from tagger.core.iamport import IMP
from tagger.core.mongo.models.order import Order, Payment, Refund
from tagger.models.admin import OrderPaymentAdjustment
from tagger.serializers.order_payment_adjustment import OrderPaymentAdjustmentSerializer
from tagger.serializers.payment import PaymentSerializer
from tagger.serializers.refund import RefundSerializer
from tagger.serializers.user import UserSerializer


class _OrderSerializer(DynamicDocumentSerializer):
    payment = SerializerMethodField()
    user = UserSerializer(many=False)
    refund = SerializerMethodField()

    def get_payment(self, obj):
        payment = Payment.objects.filter(merchantuid=str(obj.id)).first()
        return PaymentSerializer(payment, many=False).data if payment else None

    def get_refund(self, obj):
        refund = Refund.objects.filter(orderid=obj.id).first()
        return RefundSerializer(refund, many=False).data if refund else None

    class Meta:
        model = Order
        fields = "__all__"


class OrderRetrieveSerializer(_OrderSerializer):
    iamport = SerializerMethodField()
    payment_adjustments = SerializerMethodField()

    def get_payment_adjustments(self, obj):
        return OrderPaymentAdjustmentSerializer(
            OrderPaymentAdjustment.objects.filter(order_id=obj.id).all(), many=True
        ).data

    def get_iamport(self, obj):
        return IMP.instance().get_payment_detail(obj.id)


class OrderListSerializer(_OrderSerializer):
    pass
