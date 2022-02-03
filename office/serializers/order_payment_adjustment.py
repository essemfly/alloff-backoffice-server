from rest_framework import fields

from django.db import models
import simplejson
from office.serializers.user_recorded_model import WithUserSerializer
from protos.order.order_item_payment_adjustment import order_item_payment_adjustment_pb2
from drf_spectacular.utils import extend_schema_field


class PaymentAdjustmentType(models.TextChoices):
    CARD_CANCEL = "CARD_CANCEL"
    CASH = "CASH"


class OrderItemPaymentAdjustmentSerializer(WithUserSerializer):
    method = fields.ChoiceField(PaymentAdjustmentType.choices)
    previous_balance = fields.IntegerField()
    resulting_balance = fields.IntegerField()
    amount = fields.IntegerField()
    bank_account_info = fields.CharField(allow_null=True)
    reason = fields.CharField(allow_null=True)

    pg_response = fields.SerializerMethodField()

    @extend_schema_field(fields.JSONField(allow_null=True))
    def get_pg_response(self, obj):
        try:
            return simplejson.loads(obj.pg_response)
        except Exception:
            return None

    class Meta:
        proto_class = order_item_payment_adjustment_pb2.OrderItemPaymentAdjustment
