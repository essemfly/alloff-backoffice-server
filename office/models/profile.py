from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    uuid = models.UUIDField(db_index=True, default=uuid4)
