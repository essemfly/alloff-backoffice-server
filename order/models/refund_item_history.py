from django.db import models

from order.models.refund_item import RefundItem


class RefundItemHistory(models.Model):
    class Meta:
        db_table = "refund_item_histories"

    amount_from = models.IntegerField(null=True, blank=True)
    fee_from = models.IntegerField(null=True, blank=True)
    amount_to = models.IntegerField()
    fee_to = models.IntegerField()
    refund_item = models.ForeignKey(
        RefundItem, related_name="histories", on_delete=models.PROTECT
    )
