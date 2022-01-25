from django.contrib.auth.models import User
from django.db import models

from order.models.order_item import OrderItem, OrderItemStatus


class OrderItemActionType(models.TextChoices):
    STATUS_CHANGE = "STATUS_CHANGE"
    MEMO_ADD = "MEMO_ADD"
    MEMO_DELETE = "MEMO_DELETE"
    PAYMENT_ADJUSTMENT = "PAYMENT_ADJUSTMENT"
    REFUND_UPDATE = "REFUND_UPDATE"
    RECEIVED_ITEM = "RECEIVED_ITEM"
    FORCE_RECEIVED_ITEM = "FORCE_RECEIVED_ITEM"


class OrderItemAlimtalkType(models.TextChoices):
    DELIVERY_STARTED = "DELIVERY_STARTED"
    CANCEL_FINISHED = "CANCEL_FINISHED"


class OrderItemActionLog(models.Model):
    class Meta:
        db_table = "order_item_action_logs"
        ordering = ["-id"]

    order_item = models.ForeignKey(
        OrderItem, on_delete=models.PROTECT, related_name="logs"
    )
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    detail = models.TextField(null=True, blank=True)
    action_type = models.CharField(max_length=100, choices=OrderItemActionType.choices)
    performed_at = models.DateTimeField(auto_now_add=True)


class OrderItemRefundUpdateLog(models.Model):
    class Meta:
        db_table = "order_item_refund_update_logs"

    order_item = models.ForeignKey(OrderItem, on_delete=models.PROTECT)
    action_log = models.OneToOneField(OrderItemActionLog, on_delete=models.CASCADE, related_name="refund_update")
    refund_delivery_price = models.IntegerField()
    refund_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItemStatusChangeLog(models.Model):
    class Meta:
        db_table = "order_item_status_change_logs"

    order_item = models.ForeignKey(OrderItem, on_delete=models.PROTECT)
    action_log = models.OneToOneField(OrderItemActionLog, on_delete=models.CASCADE, related_name="status_change")
    status_from = models.CharField(max_length=100, choices=OrderItemStatus.choices)
    status_to = models.CharField(max_length=100, choices=OrderItemStatus.choices)
    tracking_number_from = models.CharField(max_length=100, null=True, blank=True)
    tracking_number_to = models.CharField(max_length=100, null=True, blank=True)
    tracking_url_from = models.TextField(null=True, blank=True)
    tracking_url_to = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItemAlimtalkLog(models.Model):
    class Meta:
        db_table = "order_item_alimtalk_logs"

    order_item = models.ForeignKey(OrderItem, on_delete=models.PROTECT)
    action_log = models.OneToOneField(OrderItemActionLog, on_delete=models.CASCADE, related_name="alimtalk")
    alimtalk_type = models.CharField(
        max_length=100, choices=OrderItemAlimtalkType.choices
    )
    request_id = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
