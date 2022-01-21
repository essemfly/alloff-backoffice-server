from django.db import models

from office.iamport import IMP


class OrderStatus(models.TextChoices):
    ORDER_CREATED = "ORDER_CREATED"
    ORDER_RECREATED = "ORDER_RECREATED"
    ORDER_PAYMENT_PENDING = "ORDER_PAYMENT_PENDING"
    ORDER_PAYMENT_FINISHED = "ORDER_PAYMENT_FINISHED"


class Order(models.Model):
    class Meta:
        db_table = "orders"

    alloff_order_id = models.CharField(max_length=32, db_index=True)
    order_status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices,
    )

    # user
    user_id = models.CharField(max_length=24, db_index=True)
    user = models.JSONField()
    user_memo = models.TextField(default="")

    # price
    product_price = models.IntegerField()
    delivery_price = models.IntegerField(default=0)
    total_price = models.IntegerField()
    refund_price = models.IntegerField(default=0)

    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        product_name = self._get_product_name()
        return f"#{self.id} {self.alloff_order_id} - ({product_name})"

    def _get_product_name(self):
        try:
            count = self.order_items.count()
            first_product = self.order_items.first()
            product_name = first_product.product_name
            if count > 1:
                product_name += f" and {count - 1} more"
            return product_name
        except:
            return None

    @property
    def items(self):
        from .order_item import OrderItem

        return OrderItem.objects.filter(order__id=self.id)

    @property
    def payment(self):
        from .payment import Payment

        return Payment.objects.filter(merchant_uid=self.alloff_order_id).first()
    
    @property
    def iamport(self): 
        return IMP.instance().get_payment_detail(self.id)