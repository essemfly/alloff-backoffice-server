from office.serializers.daos.user import UserDAOSerializer

# from office.serializers.order_payment_adjustment import OrderPaymentAdjustmentSerializer
from office.serializers.payment import PaymentSerializer
from django.db import models

# from order.models.order import Order
from django_grpc_framework import proto_serializers
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
