from django.contrib.auth.models import User
from django.db import models
from django.utils.functional import empty

# from tagger.models.supplier import Supplier


class OrderPaymentAdjustementType(models.TextChoices):
    CARD_CANCEL = "CARD_CANCEL"
    CASH = "CASH"


class OrderPaymentAdjustment(models.Model):
    method = models.CharField(
        max_length=20,
        choices=OrderPaymentAdjustementType.choices,
    )
    order_id = models.CharField(max_length=24, db_index=True)
    admin = models.ForeignKey(to=User, on_delete=models.PROTECT)
    previous_balance = models.IntegerField()
    amount = models.IntegerField()
    resulting_balance = models.IntegerField()
    pg_response = models.JSONField(null=True)
    bank_account_info = models.CharField(max_length=100, null=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
