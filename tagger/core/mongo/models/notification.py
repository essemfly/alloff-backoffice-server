from typing import Text
from django.db.models.enums import Choices, TextChoices
from mongoengine import Document, EmbeddedDocumentField, StringField
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import BooleanField, DictField, IntField, ListField, DateTimeField


class NotificationStatus(TextChoices):
    READY = "READY"
    IN_QUEUE = "IN_QUEUE"
    CANCELED = "CANCELED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class NotificationType(TextChoices):
    PRODUCT_DIFF_NOTIFICATION = "PRODUCT_DIFF_NOTIFICATION"
    BRAND_NEW_PRODUCT_NOTIFICATION = "BRAND_NEW_PRODUCT_NOTIFICATION"
    TIMEDEAL_OPEN_NITIFICATION = "TIMEDEAL_OPEN_NITIFICATION"
    BRAND_OPEN_NOTIFICATION = "BRAND_OPEN_NOTIFICATION"
    EVENT_NOTIFICATION = "EVENT_NOTIFICATION"
    GENERAL_NOTIFICATION = "GENERAL_NOTIFICATION"


class _Notification:
    status = StringField(choices=NotificationStatus.choices)
    notificationtype = StringField(choices=NotificationType.choices)
    title = StringField(required=True)
    message = StringField(required=True)
    deviceids = ListField(StringField())
    mobiles = StringField()
    navigateto = StringField()
    referenceid = StringField()
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)
    sended = DateTimeField()
    scheduleddate = DateTimeField(required=True)
    result = DictField()


class Notification(_Notification, Document):
    meta = {"collection": "notifications"}
