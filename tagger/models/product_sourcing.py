from django.contrib.auth.models import User
from django.db import models
from tagger.core.mongo.models.order import OrderType


class OrderedItem(models.Model):
    order_id = models.CharField()
    item_type = models.CharField(choices=OrderType.choices)
    item_name = models.CharField()
    quantity = models.IntegerField(default=1)
    box_id = models.CharField(null=True)
    assigned = models.CharField(null=True)
    product_url = models.CharField()
    invetory_id = models.CharField()
    is_received = models.CharField(null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
