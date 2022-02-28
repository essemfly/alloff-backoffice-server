from django.db import models
from django_grpc_framework import proto_serializers
from protos.order.payment import payment_pb2
from rest_framework import fields


class PaymentStatus(models.TextChoices):
    PAYMENT_CREATED = "PAYMENT_CREATED"
    PAYMENT_CONFIRMED = "PAYMENT_CONFIRMED"
    PAYMENT_TIME_OUT = "PAYMENT_TIME_OUT"
    PAYMENT_CANCELED = "PAYMENT_CANCELED"
    PAYMENT_REFUND_REQUESTED = "PAYMENT_REFUND_REQUESTED"
    PAYMENT_REFUND_FINISHED = "PAYMENT_REFUND_FINISHED"


class PaymentSerializer(proto_serializers.ProtoSerializer):
    imp_uid = fields.CharField(allow_null=True)
    payment_status = fields.ChoiceField(PaymentStatus.choices)
    pg = fields.CharField()
    pay_method = fields.CharField()
    name = fields.CharField()
    merchant_uid = fields.CharField()
    amount = fields.IntegerField()
    buyer_name = fields.CharField()
    buyer_mobile = fields.CharField()
    buyer_address = fields.CharField()
    buyer_post_code = fields.CharField()
    company = fields.CharField()
    app_scheme = fields.CharField()
    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()

    personal_customs_number = fields.CharField(
        max_length=13, allow_null=True, allow_blank=True)

    class Meta:
        proto_class = payment_pb2.Payment
