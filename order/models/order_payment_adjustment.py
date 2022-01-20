from django.contrib.auth.models import User
from django.db import models

from order.models.order import Order


class PaymentAdjustmentBalanceNotMatchingException(Exception):
    pass


class OrderItemPaymentAdjustementType(models.TextChoices):
    CARD_CANCEL = "CARD_CANCEL"
    CASH = "CASH"


class OrderItemPaymentAdjustment(models.Model):
    method = models.CharField(
        max_length=20,
        choices=OrderItemPaymentAdjustementType.choices,
    )
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    previous_balance = models.IntegerField()
    amount = models.IntegerField()
    resulting_balance = models.IntegerField()
    pg_response = models.JSONField(null=True, blank=True)
    bank_account_info = models.CharField(max_length=100, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs) -> None:
        if self.resulting_balance + self.amount != self.previous_balance:
            raise PaymentAdjustmentBalanceNotMatchingException
        return super().save(*args, **kwargs)
