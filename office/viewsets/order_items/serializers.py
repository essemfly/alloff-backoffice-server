from rest_framework import serializers

from office.serializers.order_payment_adjustment import PaymentAdjustmentType


class ForceMakeRiSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)


class UpdateRefundSerializer(serializers.Serializer):
    refund_amount = serializers.IntegerField(min_value=0)
    refund_fee = serializers.IntegerField(min_value=0)


class OrderItemAdjustPaymentSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=0)
    method = serializers.ChoiceField(PaymentAdjustmentType.choices)
    bank_account_info = serializers.CharField(allow_null=True, required=False)
    reason = serializers.CharField(allow_null=True, required=False)
