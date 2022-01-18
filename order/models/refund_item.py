from django.db import models

from order.models.order_item import OrderItem


class RefundItem(models.Model):
    order_id = models.CharField(max_length=100, null=False, index=True)
    order_item = models.OneToOneField(to=OrderItem)
    refund_fee = models.IntegerField()
    refund_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
