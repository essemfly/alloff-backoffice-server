from django.contrib.auth.models import User
from django.db import models
from django.utils.functional import empty

# from tagger.models.supplier import Supplier


# class ProductSourcing(models.Model):
#     product_type = models.TextChoices(
#         "ALLOFF", "NORMAL", "ALLOFF_TEMPLATE", #     )
#     product_id = models.CharField(max_length=24, db_index=True,
#     supplier = models.ForeignKey(to=Supplier, on_delete=models.PROTECT)
#     memo = models.TextField( )
#     url = models.TextField(null=True)
#     price = models.IntField(
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(null=True)
