from django.db import models
from mongoengine import (
    DateTimeField,
    DynamicDocument,
    EmbeddedDocumentField,
    IntField,
    StringField,
    connect,
    Document,
)
from mongoengine.fields import EmbeddedDocumentListField, ListField
from tagger.core.mongo.models.order_item import OrderItem
from tagger.core.mongo.models.user import User

connect(
    "outlet_dev",
    username="root",
    password="2morebutter",
    authentication_source="admin",
    host="mongodb://db.lessbutter.co",
)


class OrderStatus(models.TextChoices):
    PAYMENT_FINISHED = "PAYMENT_FINISHED"
    PRODUCT_PREPARING = "PRODUCT_PREPARING"
    DELIVERY_PREPARING = "DELIVERY_PREPARING"
    DELIVERY_STARTED = "DELIVERY_STARTED"
    DELIVERY_FINISHED = "DELIVERY_FINISHED"
    CONFIRM_PAYMENT = "CONFIRM_PAYMENT"
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    CANCEL_PENDING = "CANCEL_PENDING"
    CANCEL_FINISHED = "CANCEL_FINISHED"


class OrderType(models.TextChoices):
    NORMAL_ORDER = "NORMAL_ORDER"
    TIMEDEAL_ORDER = "TIMEDEAL_ORDER"


class Payment(DynamicDocument):
    meta = {"collection": "payments"}
    impuid = StringField(required=True)
    paymentstatus = StringField(required=True)
    pg = StringField(required=True)
    paymethod = StringField(required=True)
    name = StringField(required=True)
    merchantuid = StringField(required=True)
    amount = IntField(required=True)
    buyername = StringField(required=True)
    deliverytrackingnumber = StringField(required=True)
    deliverytrackingurl = StringField(required=True)
    buyermobile = StringField(required=True)
    buyeraddress = StringField(required=True)
    buyerpostcode = StringField(required=True)
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)


class Refund(Document):
    meta = {"collection": "refunds"}
    orderid = StringField()
    refunddeliveryprice = IntField(required=True)
    refundprice = IntField(required=True)
    refundamount = IntField(required=True)
    created: DateTimeField(required=True)
    updated: DateTimeField(required=True)


class Order(DynamicDocument):
    meta = {"collection": "orders"}
    orderstatus = StringField(choices=OrderStatus.choices)
    ordertype = StringField(choices=OrderType.choices)
    totalprice = IntField(required=True)
    productprice = IntField(required=True)
    deliveryprice = IntField(required=True)
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)
    memo = StringField(empty=True, required=True)
    deliverytrackingnumber = StringField(empty=True, required=True)
    deliverytrackingurl = StringField(empty=True, required=True)
    user = EmbeddedDocumentField(User, required=True)
    orders = EmbeddedDocumentListField(OrderItem, required=True)
