from rest_framework.fields import CharField, DictField
from rest_framework.serializers import SerializerMethodField
from rest_framework_mongoengine.serializers import DynamicDocumentSerializer
from tagger.core.iamport import IMP
from tagger.core.mongo.models.order import Order, Payment, Refund
from tagger.models.order_action_log import OrderActionLog
from tagger.models.order_memo import OrderMemo
from tagger.models.order_payment_adjustment import OrderPaymentAdjustment
from tagger.serializers.order_action_log import OrderActionLogSerializer
from tagger.serializers.order_memo import OrderMemoSerializer
from tagger.serializers.order_payment_adjustment import OrderPaymentAdjustmentSerializer
from tagger.serializers.payment import PaymentSerializer
from tagger.serializers.refund import RefundSerializer
from tagger.serializers.user import UserSerializer
from drf_yasg.utils import swagger_serializer_method


class _OrderSerializer(DynamicDocumentSerializer):
    id = CharField(required=True)
    payment = SerializerMethodField()
    user = UserSerializer(many=False)
    refund = SerializerMethodField()

    @swagger_serializer_method(serializer_or_field=PaymentSerializer)
    def get_payment(self, obj):
        payment = Payment.objects.filter(merchantuid=str(obj.id)).first()
        return PaymentSerializer(payment, many=False).data if payment else None

    @swagger_serializer_method(serializer_or_field=RefundSerializer)
    def get_refund(self, obj):
        refund = Refund.objects.filter(orderid=str(obj.id)).first()
        return RefundSerializer(refund, many=False).data if refund else None

    class Meta:
        model = Order
        fields = "__all__"


class OrderRetrieveSerializer(_OrderSerializer):
    iamport = SerializerMethodField()
    payment_adjustments = SerializerMethodField()
    memos = SerializerMethodField()
    logs = SerializerMethodField()

    @swagger_serializer_method(serializer_or_field=OrderActionLogSerializer(many=True))
    def get_logs(self, obj):
        return OrderActionLogSerializer(
            OrderActionLog.objects.filter(order_id=obj.id)
            .order_by("-performed_at")
            .all(),
            many=True,
        ).data

    @swagger_serializer_method(serializer_or_field=OrderMemoSerializer(many=True))
    def get_memos(self, obj):
        return OrderMemoSerializer(
            OrderMemo.objects.filter(order_id=obj.id).order_by("-created_at").all(),
            many=True,
        ).data

    @swagger_serializer_method(
        serializer_or_field=OrderPaymentAdjustmentSerializer(many=True)
    )
    def get_payment_adjustments(self, obj):
        return OrderPaymentAdjustmentSerializer(
            OrderPaymentAdjustment.objects.filter(order_id=obj.id).all(),
            many=True,
        ).data

    @swagger_serializer_method(serializer_or_field=DictField)
    def get_iamport(self, obj):
        return IMP.instance().get_payment_detail(obj.id)


class OrderListSerializer(_OrderSerializer):
    pass
