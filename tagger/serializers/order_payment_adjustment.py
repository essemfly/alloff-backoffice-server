from rest_framework import serializers

from tagger.models.admin import OrderPaymentAdjustment


class OrderPaymentAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPaymentAdjustment
        fields = "__all__"
