from django.db import models
from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_field
from gen.pyalloff import order_item_pb2
from office.iamport import IMP
from office.models.company import Company
from office.serializers.company import CompanySerializer
from office.serializers.daos.cancel_description import CancelDescriptionDAOSerializer
from office.serializers.daos.delivery_description import (
    DeliveryDescriptionDAOSerializer,
)
from office.serializers.order import OrderSerializer
from office.serializers.order_item_action_log import OrderItemActionLogSerializer
from office.serializers.order_item_status import OrderItemStatus
from office.serializers.order_memo import OrderItemMemoSerializer
from office.serializers.order_payment_adjustment import (
    OrderItemPaymentAdjustmentSerializer,
)
from office.serializers.pagination import PaginationSerializer
from office.serializers.refund_item import RefundItemSerializer
from rest_framework import fields
from rest_framework.exceptions import APIException


class OrderItemType(models.TextChoices):
    NORMAL_ORDER = "NORMAL_ORDER"
    TIMEDEAL_ORDER = "TIMEDEAL_ORDER"
    EXHIBITION_ORDER = "EXHIBITION_ORDER"
    UNKNOWN_ORDER = "UNKNOWN_ORDER"


class _OrderItemSerializer(proto_serializers.ProtoSerializer):
    # ----- Fields -----
    id = fields.IntegerField()
    order_item_code = fields.CharField()
    order_item_type = fields.ChoiceField(OrderItemType.choices)
    order_item_status = fields.ChoiceField(OrderItemStatus.choices)

    # brand
    brand_keyname = fields.CharField()
    brand_korname = fields.CharField()

    # company
    company = fields.SerializerMethodField()

    @extend_schema_field(CompanySerializer(allow_null=True))
    def get_company(self, obj):
        try:
            company = Company.objects.get(keyname=obj.company_keyname)
            return CompanySerializer(company).data
        except:
            # Object does not necessarily have a company
            return None

    # product
    product_id = fields.CharField()
    product_url = fields.CharField(allow_null=True)
    product_img = fields.CharField()
    product_name = fields.CharField()

    cancel_description = CancelDescriptionDAOSerializer()
    delivery_description = DeliveryDescriptionDAOSerializer()

    sales_price = fields.IntegerField()
    size = fields.CharField()
    color = fields.CharField(allow_null=True)
    quantity = fields.IntegerField()

    # tracking
    tracking_url = fields.ListField(child=fields.CharField())
    tracking_number = fields.ListField(child=fields.CharField())

    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()
    ordered_at = fields.DateTimeField(allow_null=True)

    payment_finished_at = fields.DateTimeField(allow_null=True)
    product_preparing_at = fields.DateTimeField(allow_null=True)
    foreign_product_inspecting_at = fields.DateTimeField(allow_null=True)
    delivery_preparing_at = fields.DateTimeField(allow_null=True)

    foreign_delivery_started_at = fields.DateTimeField(allow_null=True)
    delivery_started_at = fields.DateTimeField(allow_null=True)

    delivery_finished_at = fields.DateTimeField(allow_null=True)

    confirmed_at = fields.DateTimeField(allow_null=True)

    cancel_requested_at = fields.DateTimeField(allow_null=True)
    cancel_finished_at = fields.DateTimeField(allow_null=True)

    exchange_requested_at = fields.DateTimeField(allow_null=True)
    exchange_started_at = fields.DateTimeField(allow_null=True)
    exchange_finished_at = fields.DateTimeField(allow_null=True)

    return_requested_at = fields.DateTimeField(allow_null=True)
    return_started_at = fields.DateTimeField(allow_null=True)
    return_finished_at = fields.DateTimeField(allow_null=True)

    # ----- Relations -----
    order = OrderSerializer()

    # ----- Properties -----
    product_option = fields.CharField()
    total_amount = fields.IntegerField()
    is_foreign = fields.BooleanField()
    shipped_items_count = fields.IntegerField()
    fulfillable_items_count = fields.IntegerField()

    class Meta:
        proto_class = order_item_pb2.OrderItem


class OrderItemListSerializer(_OrderItemSerializer):
    pass


class OrderItemRetrieveSerializer(_OrderItemSerializer):
    logs = OrderItemActionLogSerializer(many=True)
    memos = OrderItemMemoSerializer(many=True)
    payment_adjustments = OrderItemPaymentAdjustmentSerializer(many=True)
    iamport = fields.SerializerMethodField()
    refund_item = fields.SerializerMethodField()

    @extend_schema_field(RefundItemSerializer(allow_null=True))
    def get_refund_item(self, obj):
        if obj.refund_item.refund_amount == 0:
            return None
        return RefundItemSerializer(obj.refund_item).data

    @extend_schema_field(fields.DictField)
    def get_iamport(self, obj):
        return IMP.instance().get_payment_detail(obj.order.alloff_order_id)


class PaginatedOrderItemSerializer(PaginationSerializer):
    results = OrderItemListSerializer(many=True)
