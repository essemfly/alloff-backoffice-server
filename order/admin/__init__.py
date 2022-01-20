from django.contrib import admin

from order.models import Payment, Order, RefundItem, RefundItemHistory

# import only. register each files and
from .order import OrderAdmin

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(RefundItem)
admin.site.register(RefundItemHistory)
