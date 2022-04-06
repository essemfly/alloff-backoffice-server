from django.db import models
from office.models.company import Company
from shortuuid import ShortUUID


def _make_brand_key():
    uuid = ShortUUID().random(length=8)
    return f"COMPANYBRAND_{uuid}"


class CompanyBrand(models.Model):
    class Meta:
        db_table = "company_brands"

    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, related_name="company_brands"
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    keyname = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        unique=True,
    )
    brand_key = models.CharField(
        max_length=50,
        null=False,
        editable=False,
        db_index=True,
        unique=True,
        default=_make_brand_key,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
