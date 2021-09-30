from enum import Enum
from tagger.core.mongo.models.user import User
from mongoengine import (
    Document,
    StringField,
    IntField,
    DynamicDocument,
    EmbeddedDocumentField,
    DateTimeField,
)
from mongoengine import connect


connect(
    "outlet_dev",
    username="root",
    password="2morebutter",
    authentication_source="admin",
    host="mongodb://db.lessbutter.co",
)


OrderStatus = (
    "PAYMENT_FINISHED",
    "PRODUCT_PREPARING",
    "DELIVERY_PREPARING",
    "DELIVERY_STARTED",
    "DELIVERY_FINISHED",
    "CONFIRM_PAYMENT",
    "CANCEL_REQUESTED",
    "CANCEL_PENDING",
    "CANCEL_FINISHED",
)


OrderType = (
    "NORMAL_ORDER",
    "TIMEDEAL_ORDER",
)


class Payment(DynamicDocument):
    meta = {"collection": "payments"}


class Order(DynamicDocument):
    meta = {"collection": "orders"}

    orderstatus = StringField(choices=OrderStatus, required=True)
    ordertype = StringField(choices=OrderType, required=True)
    totalprice = IntField(required=True)
    productprice = IntField(required=True)
    deliveryprice = IntField(required=True)
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)
    memo = StringField(empty=True, required=True)
    deliverytrackingnumber = StringField(empty=True, required=True)
    deliverytrackingurl = StringField(empty=True, required=True)
    user = EmbeddedDocumentField(User, db_field="user", required=True)
    # orders: O[];
    # refund?: R;
