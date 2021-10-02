from django.contrib.auth.models import User
from django.db import models

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
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    previous_balance = models.IntegerField()
    amount = models.IntegerField()
    resulting_balance = models.IntegerField()
    pg_response = models.JSONField(null=True)
    bank_account_info = models.CharField(max_length=100)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class ProductSourcing(models.Model):
#     product_type = models.TextChoices(
#         "ALLOFF", "NORMAL", "ALLOFF_TEMPLATE", #     )
#     product_id = models.CharField(max_length=24, db_index=True,
#     supplier = models.ForeignKey(to=Supplier, on_delete=models.PROTECT)
#     memo = models.TextField( )
#     url = models.TextField(null=True)
#     price = models.IntField(
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(null=True)
