from django.db import models


class Courier(models.Model):
    name = models.CharField(max_length=30)
    sweettracker_id = models.IntegerField()
    tracking_url_base = models.TextField()
