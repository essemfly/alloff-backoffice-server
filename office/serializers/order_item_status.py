from django.db import models


class OrderItemStatus(models.TextChoices):
    ORDER_ITEM_CREATED = "ORDER_ITEM_CREATED"
    ORDER_ITEM_RECREATED = "ORDER_ITEM_RECREATED"
    ORDER_ITEM_PAYMENT_PENDING = "ORDER_ITEM_PAYMENT_PENDING"
    ORDER_ITEM_PAYMENT_FINISHED = "ORDER_ITEM_PAYMENT_FINISHED"
    ORDER_ITEM_PRODUCT_PREPARING = "ORDER_ITEM_PRODUCT_PREPARING"
    ORDER_ITEM_FOREIGN_PRODUCT_INSPECTING = "ORDER_ITEM_FOREIGN_PRODUCT_INSPECTING"
    ORDER_ITEM_DELIVERY_PREPARING = "ORDER_ITEM_DELIVERY_PREPARING"
    ORDER_ITEM_FOREIGN_DELIVERY_STARTED = "ORDER_ITEM_FOREIGN_DELIVERY_STARTED"
    ORDER_ITEM_DELIVERY_STARTED = "ORDER_ITEM_DELIVERY_STARTED"
    ORDER_ITEM_DELIVERY_FINISHED = "ORDER_ITEM_DELIVERY_FINISHED"
    ORDER_ITEM_CONFIRM_PAYMENT = "ORDER_ITEM_CONFIRM_PAYMENT"
    ORDER_ITEM_CANCEL_FINISHED = "ORDER_ITEM_CANCEL_FINISHED"
    ORDER_ITEM_EXCHANGE_REQUESTED = "ORDER_ITEM_EXCHANGE_REQUESTED"
    ORDER_ITEM_EXCHANGE_PENDING = "ORDER_ITEM_EXCHANGE_PENDING"
    ORDER_ITEM_EXCHANGE_FINISHED = "ORDER_ITEM_EXCHANGE_FINISHED"
    ORDER_ITEM_RETURN_REQUESTED = "ORDER_ITEM_RETURN_REQUESTED"
    ORDER_ITEM_RETURN_PENDING = "ORDER_ITEM_RETURN_PENDING"
    ORDER_ITEM_RETURN_FINISHED = "ORDER_ITEM_RETURN_FINISHED"
