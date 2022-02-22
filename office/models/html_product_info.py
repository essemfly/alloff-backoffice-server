from django.db import models


class HtmlProductInfo(models.Model):
    product_id = models.CharField(max_length=24, db_index=True, unique=True)
    raw_html = models.TextField()
