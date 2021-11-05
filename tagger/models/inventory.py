from django.db import models
from tagger.core.mongo.models.order import OrderType


class InventoryStatus(models.TextChoices):
    IN_STOCK = "IN_STOCK"
    SHIPPED = "SHIPPED"


class ProductType(models.TextChoices):
    NORMAL_PRODUCT = "NORMAL"
    TIMEDEAL_PRODUCT = "TIMEDEAL"


class Inventory(models.Model):
    code = models.CharField(max_length=30, db_index=True)
    status = models.CharField(max_length=30)
    size = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    product_id = models.CharField(max_length=50)
    product_from_order_url = models.CharField(max_length=100, null=True)
    product_name = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=30)
    product_type = models.CharField(max_length=50, choices=ProductType.choices)


# 출고 만들기
