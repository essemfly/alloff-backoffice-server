from typing import Iterable, Optional
from django.db import models, transaction
from order.models.order import Order

from order.models.order_item import OrderItem


class RefundAmountDoesNotMatchException(Exception):
    pass


class RefundItem(models.Model):
    class Meta:
        db_table = "refund_items"

    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    order_item = models.OneToOneField(OrderItem, on_delete=models.PROTECT)
    refund_fee = models.IntegerField(null=True, blank=True, default=0)
    refund_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[Iterable[str]] = ...,
    ) -> None:
        order_item = self.order_item  # type: OrderItem
        if self.refund_amount + self.refund_fee != order_item.total_amount:
            raise RefundAmountDoesNotMatchException

        with transaction.atomic():
            from .refund_item_history import RefundItemHistory

            try:
                current = RefundItem.objects.get(id=self.id)
                amount_from = current.refund_amount
                fee_from = current.refund_fee
            except RefundItem.DoesNotExist:
                amount_from = 0
                fee_from = 0

            RefundItemHistory.objects.create(
                amount_from=amount_from,
                fee_from=fee_from,
                amount_to=self.refund_amount,
                fee_to=self.refund_fee,
                refund_item=self,
            )
            super().save(force_insert, force_update, using, update_fields)
