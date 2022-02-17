from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from alloff_backoffice_server.settings import SUPERCOMPANY_KEYNAME
from office.models.company import Company


class ProfileType(models.TextChoices):
    ADMIN = "ADMIN"
    COMPANY_USER = "COMPANY_USER"
    COMPANY_API = "COMPANY_API"


class Profile(models.Model):
    class Meta:
        db_table = "profiles"

    profile_type = models.CharField(
        max_length=30, choices=ProfileType.choices, default=ProfileType.ADMIN
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid4,
        editable=False,
        unique=True,
    )

    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    @property
    def is_admin(self):
        return (
            self.profile_type == ProfileType.ADMIN
            and self.company.keyname == SUPERCOMPANY_KEYNAME
        )

    def __str__(self):
        return f"User Profile #{self.id} - [{self.profile_type}] {self.name}"
