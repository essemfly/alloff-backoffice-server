from django.db import models

from tagger.models import ExtendedOrder
from tagger.models.inventory import ProductType


class ExtendedOrderItem(models.Model):
    extended_order = models.ForeignKey(to=ExtendedOrder, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=30, choices=ProductType.choices)
    size = models.CharField(max_length=30)
    quantity = models.IntegerField()
    name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=200, db_index=True)
    product_id = models.CharField(max_length=30, db_index=True)
    brand_keyname = models.CharField(max_length=30)

    def __str__(self):
        return self.product_code

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.product_code is None or self.product_code.strip() == "":
            self.product_code = self.brand_keyname + "___" \
                                + "".join(self.name.split()) + "___" \
                                + "".join(self.size.split())
        return super().save(force_insert, force_update, using, update_fields)
