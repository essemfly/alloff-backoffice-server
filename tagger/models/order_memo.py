from django.contrib.auth.models import User
from django.db import models
from django.utils.functional import empty


class OrderMemo(models.Model):
    order_id = models.CharField(max_length=24, db_index=True)
    admin = models.ForeignKey(to=User, on_delete=models.PROTECT)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
