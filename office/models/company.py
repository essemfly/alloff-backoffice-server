from django.db import models


class CompanyStatus(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Company(models.Model):
    class Meta:
        db_table = "companies"

    name = models.CharField(max_length=100, null=False, blank=False)
    keyname = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        db_index=True,
    )
    status = models.CharField(
        max_length=10,
        choices=CompanyStatus.choices,
        blank=True,
        default=CompanyStatus.INACTIVE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Company #{self.id} - {self.name}"
