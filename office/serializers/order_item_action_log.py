from django.db import models
from drf_spectacular.utils import extend_schema_field
from gen.pyalloff import (inventory_receipt_log_pb2, order_item_action_log_pb2,
                          order_item_alimtalk_log_pb2,
                          order_item_refund_update_log_pb2,
                          order_item_status_change_log_pb2,
                          received_item_generation_log_pb2)
from office.serializers.order_item_status import OrderItemStatus
from office.serializers.user_recorded_model import WithUserSerializer
from rest_framework import fields


class OrderItemActionType(models.TextChoices):
    STATUS_CHANGE = "STATUS_CHANGE"
    MEMO_ADD = "MEMO_ADD"
    MEMO_DELETE = "MEMO_DELETE"
    PAYMENT_ADJUSTMENT = "PAYMENT_ADJUSTMENT"
    REFUND_UPDATE = "REFUND_UPDATE"
    GENERATED_RECEIVED_ITEM = "GENERATED_RECEIVED_ITEM"
    CANCELED_RECEIVED_ITEM = "CANCELED_RECEIVED_ITEM"
    RECEIVED_INVENTORY = "RECEIVED_INVENTORY"
    REVERTED_INVENTORY = "REVERTED_INVENTORY"


class OrderItemAlimtalkType(models.TextChoices):
    DELIVERY_STARTED = "DELIVERY_STARTED"
    CANCEL_FINISHED = "CANCEL_FINISHED"


class OrderItemAlimtalkLogSerializer(WithUserSerializer):
    id = fields.IntegerField()
    alimtalk_type = fields.ChoiceField(OrderItemAlimtalkType.choices)
    request_id = fields.CharField(allow_null=True)
    created_at = fields.DateTimeField()

    class Meta:
        proto_class = order_item_alimtalk_log_pb2.OrderItemAlimtalkLog


class OrderItemRefundUpdateLogSerializer(WithUserSerializer):
    id = fields.IntegerField()
    refund_fee = fields.IntegerField()
    refund_amount = fields.IntegerField()
    created_at = fields.DateTimeField()

    class Meta:
        proto_class = order_item_refund_update_log_pb2.OrderItemRefundUpdateLog


class OrderItemStatusChangeLogSerializer(WithUserSerializer):
    id = fields.IntegerField()
    status_from = fields.ChoiceField(OrderItemStatus.choices)
    status_to = fields.ChoiceField(OrderItemStatus.choices)
    tracking_number_from = fields.CharField(allow_null=True)
    tracking_number_to = fields.CharField(allow_null=True)
    tracking_url_from = fields.CharField(allow_null=True)
    tracking_url_to = fields.CharField(allow_null=True)
    created_at = fields.DateTimeField()

    class Meta:
        proto_class = order_item_status_change_log_pb2.OrderItemStatusChangeLog


class ReceivedItemGenerationLogSerializer(WithUserSerializer):
    id = fields.IntegerField()
    is_force = fields.BooleanField()
    received_item_id = fields.IntegerField()
    received_item_code = fields.CharField()
    created_at = fields.DateTimeField()
    is_force = fields.BooleanField()

    class Meta:
        proto_class = received_item_generation_log_pb2.ReceivedItemGenerationLog


class InventoryReceiptLogSerializer(WithUserSerializer):
    id = fields.IntegerField()
    received_item_id = fields.IntegerField()
    received_item_code = fields.CharField()
    inventory_id = fields.IntegerField()
    inventory_code = fields.CharField()
    created_at = fields.DateTimeField()

    class Meta:
        proto_class = inventory_receipt_log_pb2.InventoryReceiptLog


class OrderItemActionLogSerializer(WithUserSerializer):
    alimtalk = fields.SerializerMethodField()

    @extend_schema_field(OrderItemAlimtalkLogSerializer(allow_null=True))
    def get_alimtalk(self, obj):
        if obj.alimtalk.created_at == "":
            return None
        return OrderItemAlimtalkLogSerializer(obj.alimtalk).data

    status_change = fields.SerializerMethodField()

    @extend_schema_field(OrderItemStatusChangeLogSerializer(allow_null=True))
    def get_status_change(self, obj):
        if obj.status_change.created_at == "":
            return None
        return OrderItemStatusChangeLogSerializer(obj.status_change).data

    refund_update = fields.SerializerMethodField()

    @extend_schema_field(OrderItemRefundUpdateLogSerializer(allow_null=True))
    def get_refund_update(self, obj):
        if obj.refund_update.created_at == "":
            return None
        return OrderItemRefundUpdateLogSerializer(obj.refund_update).data

    received_item = fields.SerializerMethodField()

    @extend_schema_field(ReceivedItemGenerationLogSerializer(allow_null=True))
    def get_received_item(self, obj):
        if obj.received_item.created_at == "":
            return None
        return ReceivedItemGenerationLogSerializer(obj.received_item).data

    inventory = fields.SerializerMethodField()

    @extend_schema_field(InventoryReceiptLogSerializer(allow_null=True))
    def get_inventory(self, obj):
        if obj.inventory.created_at == "":
            return None
        return InventoryReceiptLogSerializer(obj.inventory).data

    detail = fields.CharField(allow_null=True)
    action_type = fields.ChoiceField(OrderItemActionType.choices)
    created_at = fields.DateTimeField()

    class Meta:
        proto_class = order_item_action_log_pb2.OrderItemActionLog
