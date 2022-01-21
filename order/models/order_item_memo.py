from django.contrib.auth.models import User
from django.db import models

from order.models.order_item import OrderItem


class OrderItemMemo(models.Model):
    class Meta:
        db_table = "order_item_memos"
    order_item = models.ForeignKey(OrderItem, on_delete=models.PROTECT, related_name="memos")
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
