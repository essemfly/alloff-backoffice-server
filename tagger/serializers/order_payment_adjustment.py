from rest_framework import serializers

from tagger.models.order_payment_adjustment import OrderPaymentAdjustment
from tagger.serializers.admin import AdminSerializer


class OrderPaymentAdjustmentSerializer(serializers.ModelSerializer):
    admin = AdminSerializer()

    class Meta:
        model = OrderPaymentAdjustment
        fields = "__all__"
