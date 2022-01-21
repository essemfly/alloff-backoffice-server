from django.contrib import admin

from order.models import Payment, Order, RefundItem, RefundItemHistory
from order.models.order_item import OrderItem
from order.models.order_item_memo import OrderItemMemo

# import only. register each files and
from .order import OrderAdmin

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(RefundItem)
admin.site.register(RefundItemHistory)
admin.site.register(OrderItemMemo)
