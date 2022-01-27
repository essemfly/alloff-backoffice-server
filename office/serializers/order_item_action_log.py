from office.serializers.user_recorded_model import UserRecordedSerializer
from protos.order.order_item_action_log import order_item_action_log_pb2
from protos.order.order_item_alimtalk_log import order_item_alimtalk_log_pb2
from protos.order.order_item_refund_update_log import order_item_refund_update_log_pb2
from protos.order.order_item_status_change_log import order_item_status_change_log_pb2

from django.db import models


class OrderItemActionType(models.TextChoices):
    STATUS_CHANGE = "STATUS_CHANGE"
    MEMO_ADD = "MEMO_ADD"
    MEMO_DELETE = "MEMO_DELETE"
    PAYMENT_ADJUSTMENT = "PAYMENT_ADJUSTMENT"
    REFUND_UPDATE = "REFUND_UPDATE"
    GENERATED_RECEIVED_ITEM = "GENERATED_RECEIVED_ITEM"
    FORCE_GENERATED_RECEIVED_ITEM = "FORCE_GENERATED_RECEIVED_ITEM"
    RECEIVED_INVENTORY = "RECEIVED_INVENTORY"


class OrderItemAlimtalkType(models.TextChoices):
    DELIVERY_STARTED = "DELIVERY_STARTED"
    CANCEL_FINISHED = "CANCEL_FINISHED"


class OrderItemAlimtalkLogSerializer(UserRecordedSerializer):
    class Meta:
        proto_class = order_item_alimtalk_log_pb2.OrderItemAlimtalkLog


class OrderItemRefundUpdateLogSerializer(UserRecordedSerializer):
    class Meta:
        proto_class = order_item_refund_update_log_pb2.OrderItemRefundUpdateLog


class OrderItemStatusChangeLogSerializer(UserRecordedSerializer):
    class Meta:
        proto_class = order_item_status_change_log_pb2.OrderItemStatusChangeLog


class OrderItemActionLogSerializer(UserRecordedSerializer):
    alimtalk = OrderItemAlimtalkLogSerializer(allow_null=True)
    status_change = OrderItemStatusChangeLogSerializer(allow_null=True)
    refund_update = OrderItemRefundUpdateLogSerializer(allow_null=True)

    class Meta:
        proto_class = order_item_action_log_pb2.OrderItemActionLog

# class ReceivedItemGenerationLog(UserRecordedModel):
#     class Meta:
#         db_table = "received_item_generation_logs"

#     order_item = models.ForeignKey(OrderItem, on_delete=models.PROTECT)
#     action_log = models.OneToOneField(
#         OrderItemActionLog, on_delete=models.CASCADE, related_name="received_item"
#     )
#     is_force = models.BooleanField()
#     received_item_id = models.IntegerField(db_index=True)
#     received_item_code = models.CharField(max_length=30, db_index=True)
#     created_at = models.DateTimeField(auto_now_add=True)


# class InventoryReceiptLog(UserRecordedModel):
#     class Meta:
#         db_table = "inventory_receipt_logs"

#     order_item = models.ForeignKey(OrderItem, on_delete=models.PROTECT)
#     action_log = models.OneToOneField(
#         OrderItemActionLog, on_delete=models.CASCADE, related_name="inventory"
#     )
#     received_item_id = models.IntegerField(db_index=True)
#     received_item_code = models.CharField(max_length=30, db_index=True)
#     inventory_id = models.IntegerField(db_index=True)
#     inventory_code = models.CharField(max_length=30, db_index=True)
#     created_at = models.DateTimeField(auto_now_add=True)
