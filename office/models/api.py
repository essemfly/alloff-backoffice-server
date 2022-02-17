from django.contrib.auth.models import User
from django.db import models
from office.models.company import Company
from shortuuid import ShortUUID


def _make_api_key():
    uuid = ShortUUID().random(length=32)
    return f"ALLOFFAPI_{uuid}"


class ApiKeyStatus(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ApiChannel(models.TextChoices):
    SABANGNET = "SABANGNET"
    ECMONITOR = "ECMONITOR"


class ApiKey(models.Model):
    class Meta:
        db_table = "api_keys"

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=30,
        choices=ApiKeyStatus.choices,
        default=ApiKeyStatus.INACTIVE,
    )
    key = models.CharField(
        max_length=100,
        null=False,
        editable=False,
        db_index=True,
        unique=True,
        default=_make_api_key,
    )
    api_user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, editable=False
    )
    channel = models.CharField(max_length=30, choices=ApiChannel.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def api_username(self):
        return f"__{self.channel.lower()}_{self.company.keyname}"

    def __str__(self):
        return f"{self.channel} ApiKey #{self.id} for {self.company.name} ({self.status})"
