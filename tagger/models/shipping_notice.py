from datetime import date, datetime, timedelta

from django.db import models

from tagger.models import Inventory, ExtendedOrderItem


class ShippingNoticeStatus(models.TextChoices):
    CREATED = "CREATED"
    LOCKED = "LOCKED"
    SHIPPED = "SHIPPED"


class ShippingNotice(models.Model):
    code = models.CharField(max_length=13, unique=True, db_index=True, null=False)
    status = models.CharField(max_length=20, choices=ShippingNoticeStatus.choices, default=ShippingNoticeStatus.CREATED)
    locked_at = models.DateTimeField(null=True, blank=True)
    shipped_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.code is None or self.code == "":
            self.code = ShippingNotice.generate_usable_code()

        if self.status == ShippingNoticeStatus.LOCKED:
            self.locked_at = datetime.now()

        if self.status == ShippingNoticeStatus.SHIPPED:
            self.shipped_at = datetime.now()

        return super().save(force_insert, force_update, using, update_fields)

    @staticmethod
    def generate_usable_code():
        code = ""
        is_unique = False

        while not is_unique:
            code = ShippingNotice._make_code()
            if ShippingNotice.objects.filter(code=code).count() == 0:
                is_unique = True

        return code

    @staticmethod
    def _make_code():
        _today = date.today()
        _tomorrow = _today + timedelta(days=1)
        today = _today.isoformat()[2:].replace("-", "")

        today_notices_count = ShippingNotice.objects.filter(created_at__gte=_today, created_at__lt=_tomorrow).count()
        sequence = f"{today_notices_count + 1}".zfill(2)
        return f"""SHP-{today}-{sequence}"""


class ShippingNoticeItem(models.Model):
    notice = models.ForeignKey(to=ShippingNotice, on_delete=models.CASCADE)
    inventory = models.OneToOneField(to=Inventory, on_delete=models.PROTECT)
    item = models.ForeignKey(to=ExtendedOrderItem, on_delete=models.PROTECT)
