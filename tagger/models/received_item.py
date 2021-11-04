from django.contrib.auth.models import User
from django.db import models

from tagger.core.mongo.models.alloff_product import AlloffProduct
from tagger.core.mongo.models.order import OrderType, Order
from tagger.core.mongo.models.product import Product
from tagger.models.inventory import Inventory


class ReceivedItemStatus(models.TextChoices):
    CREATED = "CREATED"
    ASSGINED = "ASSGINED"
    # 마담이 재고가 있다. 확정 받아서 주문 넣어서 입금을 받은 경우
    REQUESTED = "REQUESTED"
    # 마담한테 받은 경우
    RECEIVED = "RECEIVED"
    # 소비자가 집주 전에 취소한경우 (아무일도 안일어남)
    REQUEST_CANCELED = "REQUEST_CANCELED"
    # 마담이 재고가 없다 해서 취소
    OUT_OF_STOCK = "OUT_OF_STOCK"
    # 재고에서 처리한다
    FROM_INVENTORY = "FROM_INVENTORY"


class Sourcing(models.Model):
    box_code = models.CharField(max_length=50, null=True, db_index=True)
    asignee = models.ForeignKey(to=User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ReceivedItem(models.Model):
    order_id = models.CharField(max_length=50, db_index=True)
    order_type = models.CharField(max_length=50, choices=OrderType.choices)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=50)
    sourcing = models.ForeignKey(
        to=Sourcing, on_delete=models.PROTECT, null=True)
    assignee = models.ForeignKey(to=User, on_delete=models.PROTECT, null=True)
    product_id = models.CharField(max_length=50)
    # 입고 확인후, 입고 완료된 Inventory를 넣어준다.
    inventory = models.ForeignKey(
        to=Inventory, null=True, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=30, default=ReceivedItemStatus.CREATED, choices=ReceivedItemStatus.choices)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def product(self):
        return Product.objects(id=self.product_id).first() if self.order_type == OrderType.NORMAL_ORDER \
            else AlloffProduct.objects(id=self.product_id).first()

    @property
    def order(self):
        return Order.objects(id=self.order_id).first()
