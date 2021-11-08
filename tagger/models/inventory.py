from django.db import models
from tagger.core.mongo.models.order import OrderType, Order
from bson import ObjectId


class InventoryStatus(models.TextChoices):
    IN_STOCK = "IN_STOCK"
    SHIPPED = "SHIPPED"
    SHIPPING_PENDING = "SHIPPING_PENDING"


class ProductType(models.TextChoices):
    NORMAL_PRODUCT = "NORMAL"
    TIMEDEAL_PRODUCT = "TIMEDEAL"


class Inventory(models.Model):
    code = models.CharField(max_length=30, db_index=True)
    status = models.CharField(max_length=30, choices=InventoryStatus.choices)
    size = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    product_id = models.CharField(max_length=50)
    product_from_order_url = models.CharField(max_length=100, null=True)
    product_name = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=30)
    product_type = models.CharField(max_length=50, choices=ProductType.choices)
    out_order_id = models.CharField(max_length=30, db_index=True, null=True)
    location = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"Inventory #{self.id} [{self.status}] {self.product_name} ({self.code})"

    @property
    def out_order(self):
        if self.out_order_id is None:
            return None

        return Order.objects(id=ObjectId(self.out_order_id)).first()

# 출고 만들기
