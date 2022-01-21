from rest_framework import serializers, fields
from office.serializers.order_payment_adjustment import OrderPaymentAdjustmentSerializer
from office.serializers.payment import PaymentSerializer

from order.models.order import Order


class OrderSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(many=True)
    payment = PaymentSerializer()
    # iamport = fields.DictField()
    payment_adjustments = OrderPaymentAdjustmentSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
