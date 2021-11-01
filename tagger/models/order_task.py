from django.db import models

class OrderTask(models.Model):
    
    order_id = models.CharField(max_length=24, unique=True, db_index=True)
