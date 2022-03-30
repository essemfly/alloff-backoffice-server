from django.db import models
# from order.models.order import Order
from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_field
from office.serializers.daos.user import UserDAOSerializer
# from office.serializers.order_payment_adjustment import OrderPaymentAdjustmentSerializer
from office.serializers.payment import PaymentSerializer
from protos.order.order import order_pb2
from rest_framework import fields


class OrderStatus(models.TextChoices):
    ORDER_CREATED = "ORDER_CREATED"
    ORDER_RECREATED = "ORDER_RECREATED"
    ORDER_PAYMENT_PENDING = "ORDER_PAYMENT_PENDING"
    ORDER_PAYMENT_FINISHED = "ORDER_PAYMENT_FINISHED"


class OrderSerializer(proto_serializers.ProtoSerializer):
    # items = OrderItemSerializer(many=True)
    payment = PaymentSerializer()
    # iamport = fields.DictField()
    # payment_adjustments = OrderPaymentAdjustmentSerializer(many=True)
    user = UserDAOSerializer()

    recipient_name = fields.SerializerMethodField()

    @extend_schema_field(fields.CharField)
    def get_recipient_name(self, obj):
        return obj.payment.buyer_name

    orderer_name = fields.SerializerMethodField()

    @extend_schema_field(fields.CharField)
    def get_orderer_name(self, obj):
        return obj.payment.buyer_name

    recipient_mobile = fields.SerializerMethodField()

    @extend_schema_field(fields.CharField)
    def get_recipient_mobile(self, obj):
        return obj.payment.buyer_mobile

    orderer_mobile = fields.SerializerMethodField()

    @extend_schema_field(fields.CharField)
    def get_orderer_mobile(self, obj):
        return "" if "mobile" not in obj.user else obj.user["mobile"]

    alloff_order_id = fields.CharField()
    order_status = fields.ChoiceField(OrderStatus.choices)

    # user
    user_id = fields.CharField()
    user = fields.JSONField()
    user_memo = fields.CharField(allow_null=True)

    # price
    product_price = fields.IntegerField()
    delivery_price = fields.IntegerField(allow_null=True)
    total_price = fields.IntegerField()
    refund_price = fields.IntegerField(allow_null=True)

    # timestamp
    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()
    ordered_at = fields.DateTimeField(allow_null=True)

    class Meta:
        proto_class = order_pb2.Order
