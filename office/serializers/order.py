from office.serializers.daos.user import UserDAOSerializer
# from office.serializers.order_payment_adjustment import OrderPaymentAdjustmentSerializer
from office.serializers.payment import PaymentSerializer
from rest_framework import serializers

# from order.models.order import Order


class OrderSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(many=True)
    payment = PaymentSerializer()
    # iamport = fields.DictField()
    # payment_adjustments = OrderPaymentAdjustmentSerializer(many=True)
    user = UserDAOSerializer()

    class Meta:
        # model = Order
        fields = "__all__"
