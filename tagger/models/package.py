from datetime import date, datetime
from typing import Optional

from django.db import models
from shortuuid import ShortUUID

from alloff_backoffice_server.settings import CODE_CHARSET
from tagger.models.courier import Courier
from tagger.models.shipping_notice import ShippingNoticeItem, ShippingNotice


class PackageStatus(models.TextChoices):
    CREATED = "CREATED"
    SEALED = "SEALED"
    SHIPPED = "SHIPPED"
    DELIVER_CONFIRMED = "DELIVER_CONFIRMED"


class Package(models.Model):
    code = models.CharField(max_length=13, unique=True, db_index=True, null=False)
    status = models.CharField(max_length=30, choices=PackageStatus.choices, default=PackageStatus.CREATED)

    address = models.TextField(blank=False, null=False)
    postcode = models.CharField(max_length=5, blank=False, null=False)

    recipient_name = models.CharField(max_length=60, blank=False, null=False)
    recipient_mobile = models.CharField(max_length=60, blank=False, null=False)

    courier = models.ForeignKey(to=Courier, on_delete=models.PROTECT, null=True, blank=True)
    tracking_number = models.CharField(max_length=50, blank=False, null=False)

    shipping_notice_items = models.ManyToManyField(to=ShippingNoticeItem)
    notice = models.ForeignKey(to=ShippingNotice, on_delete=models.PROTECT, related_name='packages')

    shipped_at = models.DateTimeField(null=True, blank=True)
    sealed_at = models.DateTimeField(null=True, blank=True)
    deliver_confirmed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def tracking_url(self) -> Optional[str]:
        if self.courier is None or self.tracking_number is None or self.tracking_number == "":
            return None

        return f"{self.courier.tracking_url_base}{self.courier.name} {self.tracking_number}"

    @property
    def extended_orders(self):
        return list(set([x.item.extended_order for x in self.shipping_notice_items.all()]))

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.code is None or self.code == "":
            self.code = Package.generate_usable_code()

        if self.status == PackageStatus.SHIPPED:
            self.shipped_at = datetime.now()
        elif self.status == PackageStatus.SEALED:
            self.sealed_at = datetime.now()
        elif self.status == PackageStatus.DELIVER_CONFIRMED:
            self.deliver_confirmed_at = datetime.now()

        return super().save(force_insert, force_update, using, update_fields)

    @staticmethod
    def generate_usable_code():
        code = ""
        is_unique = False

        while not is_unique:
            code = Package._make_code()
            if Package.objects.filter(code=code).count() == 0:
                is_unique = True

        return code

    @staticmethod
    def _make_code():
        today = date.today().isoformat()[2:].replace("-", "")
        random_code = ShortUUID(CODE_CHARSET).random(length=2)
        return f"""PKG-{today}-{random_code}"""
