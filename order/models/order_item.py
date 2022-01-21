from django.db import models

from .order import Order


class OrderItemStatus(models.TextChoices):
    ORDER_ITEM_CREATED = "ORDER_ITEM_CREATED"
    ORDER_ITEM_RECREATED = "ORDER_ITEM_RECREATED"
    ORDER_ITEM_PAYMENT_PENDING = "ORDER_ITEM_PAYMENT_PENDING"
    ORDER_ITEM_PAYMENT_FINISHED = "ORDER_ITEM_PAYMENT_FINISHED"
    ORDER_ITEM_PRODUCT_PREPARING = "ORDER_ITEM_PRODUCT_PREPARING"
    ORDER_ITEM_FOREIGN_PRODUCT_INSPECTING = "ORDER_ITEM_FOREIGN_PRODUCT_INSPECTING"
    ORDER_ITEM_DELIVERY_PREPARING = "ORDER_ITEM_DELIVERY_PREPARING"
    ORDER_ITEM_FOREIGN_DELIVERY_STARTED = "ORDER_ITEM_FOREIGN_DELIVERY_STARTED"
    ORDER_ITEM_DELIVERY_STARTED = "ORDER_ITEM_DELIVERY_STARTED"
    ORDER_ITEM_DELIVERY_FINISHED = "ORDER_ITEM_DELIVERY_FINISHED"
    ORDER_ITEM_CONFIRM_PAYMENT = "ORDER_ITEM_CONFIRM_PAYMENT"
    ORDER_ITEM_CANCEL_FINISHED = "ORDER_ITEM_CANCEL_FINISHED"
    ORDER_ITEM_EXCHANGE_REQUESTED = "ORDER_ITEM_EXCHANGE_REQUESTED"
    ORDER_ITEM_EXCHANGE_PENDING = "ORDER_ITEM_EXCHANGE_PENDING"
    ORDER_ITEM_EXCHANGE_FINISHED = "ORDER_ITEM_EXCHANGE_FINISHED"
    ORDER_ITEM_RETURN_REQUESTED = "ORDER_ITEM_RETURN_REQUESTED"
    ORDER_ITEM_RETURN_PENDING = "ORDER_ITEM_RETURN_PENDING"
    ORDER_ITEM_RETURN_FINISHED = "ORDER_ITEM_RETURN_FINISHED"


class OrderItemType(models.TextChoices):
    NORMAL_ORDER = "NORMAL_ORDER"
    TIMEDEAL_ORDER = "TIMEDEAL_ORDER"
    EXHIBITION_ORDER = "EXHIBITION_ORDER"
    UNKNOWN_ORDER = "UNKNOWN_ORDER"


class OrderItem(models.Model):
    class Meta:
        db_table = "order_items"

    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    order_item_code = models.CharField(max_length=16, db_index=True, unique=True)  # (구)사서함 코드
    order_item_type = models.CharField(
        max_length=50,
        choices=OrderItemType.choices,
    )
    order_item_status = models.CharField(
        choices=OrderItemStatus.choices,
        max_length=50,
    )

    # brand
    brand_keyname = models.CharField(max_length=50)
    brand_korname = models.CharField(max_length=50)

    # product
    product_id = models.CharField(max_length=24, db_index=True)
    product_url = models.URLField()
    product_img = models.URLField()
    product_name = models.CharField(max_length=100)

    cancel_description = models.JSONField()
    delivery_description = models.JSONField()

    is_removed = models.BooleanField(default=False)
    sales_price = models.IntegerField()
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField()

    # tracking
    tracking_url = models.URLField(null=True, blank=True)
    tracking_number = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered_at = models.DateTimeField(null=True, blank=True)
    delivery_started_at = models.DateTimeField(null=True, blank=True)
    delivery_finished_at = models.DateTimeField(null=True, blank=True)
    cancel_requested_at = models.DateTimeField(null=True, blank=True)
    cancel_finished_at = models.DateTimeField(null=True, blank=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    @property
    def product_option(self):
        if self.color is not None:
            return f"{self.size}-{self.color}"
        return self.size

    @property
    def total_amount(self) -> int:
        return self.sales_price * self.quantity
    
    def __str__(self):
        return f"#{self.id} {self.product_name} ({self.product_option})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # self.create_received_item()

    # def create_received_item(self):
    #     for _ in range(self.quantity):
    #         ReceivedItem.objects.create(
    #             code=self.order_item_code,
    #             status=ReceivedItemStatus.SOURCING_REQUIRED,
    #             product_brand_id=self.brand_key_name,
    #             product_brand_name=self.brand_key_name,
    #             product_id=self.alloff_product_id,
    #             product_name=self.product_name,
    #             product_size=self.size,
    #             product_color=self.color,
    #         )
