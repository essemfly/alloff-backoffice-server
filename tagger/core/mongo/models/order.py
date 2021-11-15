from typing import Optional

from bson import ObjectId
from django.db import models
from mongoengine import (
    DateTimeField,
    DynamicDocument,
    EmbeddedDocumentField,
    IntField,
    StringField,
    Document,
)
from mongoengine.fields import EmbeddedDocumentListField

from tagger.core.mongo.models.order_item import OrderItem
from tagger.core.mongo.models.user import AlloffUser


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
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)


class Order(DynamicDocument):
    meta = {"collection": "orders"}
    orderstatus = StringField(choices=OrderStatus.choices, required=True)
    ordertype = StringField(choices=OrderType.choices, required=True)
    totalprice = IntField(required=True)
    productprice = IntField(required=True)
    deliveryprice = IntField(required=True)
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)
    orderedAt = DateTimeField(required=False)
    deliveryStartedAt = DateTimeField(required=False)
    deliveryFinishedAt = DateTimeField(required=False, default_timezone="utc")
    cancelRequestedAt = DateTimeField(required=False)
    cancelFinishedAt = DateTimeField(required=False)
    confirmedAt = DateTimeField(required=False)
    memo = StringField(empty=True, required=True)
    deliverytrackingnumber = StringField(empty=True)
    deliverytrackingurl = StringField(empty=True)
    user = EmbeddedDocumentField(AlloffUser, required=True)
    orders = EmbeddedDocumentListField(OrderItem, required=True)

    @property
    def payment(self) -> Optional[Payment]:
        query = Payment.objects(merchantuid=str(self.id)).order_by("-id")
        if len(query) == 0:
            return None
        return query.first()

    @staticmethod
    def get(code_or_id: str) -> Optional["Order"]:
        if len(code_or_id) == 5:
            return Order.get_by_code(code_or_id)
        elif len(code_or_id) == 24:
            return Order.objects(id=ObjectId(code_or_id)).first()
        else:
            raise BaseException(f"Code or ID should be 5 or 24 characters long --- given: {len(code_or_id)}")

    @staticmethod
    def get_by_code(code: str) -> Optional["Order"]:
        from tagger.models import ExtendedOrder
        eo = ExtendedOrder.objects.filter(code=code.upper()).first()
        return eo.order if eo is not None else None

    @property
    def code(self) -> str:
        from tagger.models import ExtendedOrder
        eo = ExtendedOrder.objects.filter(order_id=str(self.id)).first()
        if eo is None:
            eo = ExtendedOrder.make_from(self)
        return eo.code
