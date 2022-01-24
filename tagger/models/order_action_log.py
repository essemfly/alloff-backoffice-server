from django.contrib.auth.models import User
from django.db import models
from tagger.core.mongo.models.order import OrderStatus


class OrderActionType(models.TextChoices):
    STATUS_CHANGE = "STATUS_CHANGE"
    MEMO_ADD = "MEMO_ADD"
    MEMO_DELETE = "MEMO_DELETE"
    PAYMENT_ADJUSTMENT = "PAYMENT_ADJUSTMENT"
    REFUND_UPDATE = "REFUND_UPDATE"


class OrderAlimtalkType(models.TextChoices):
    DELIVERY_STARTED = "DELIVERY_STARTED"
    CANCEL_FINISHED = "CANCEL_FINISHED"


class OrderActionLog(models.Model):
    order_id = models.CharField(max_length=24, db_index=True)
    admin = models.ForeignKey(to=User, on_delete=models.PROTECT)
    detail = models.TextField(null=True)
    action_type = models.CharField(max_length=100, choices=OrderActionType.choices)
    performed_at = models.DateTimeField(auto_now_add=True)


class OrderRefundUpdateLog(models.Model):
    order_id = models.CharField(max_length=24, db_index=True)
    action_log = models.OneToOneField(OrderActionLog, on_delete=models.CASCADE)
    refund_delivery_price = models.IntegerField()
    refund_price = models.IntegerField()
    refund_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class OrderStatusChangeLog(models.Model):
    order_id = models.CharField(max_length=24, db_index=True)
    action_log = models.OneToOneField(OrderActionLog, on_delete=models.CASCADE)
    status_from = models.CharField(max_length=100, choices=OrderStatus.choices)
    status_to = models.CharField(max_length=100, choices=OrderStatus.choices)
    delivery_tracking_number_from = models.CharField(max_length=100, null=True)
    delivery_tracking_url_from = models.CharField(max_length=100, null=True)
    delivery_tracking_number_to = models.CharField(max_length=100, null=True)
    delivery_tracking_url_to = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderAlimtalkLog(models.Model):
    order_id = models.CharField(max_length=24, db_index=True)
    action_log = models.OneToOneField(OrderActionLog, on_delete=models.CASCADE)
    alimtalk_type = models.CharField(max_length=100, choices=OrderAlimtalkType.choices)
    request_id = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
