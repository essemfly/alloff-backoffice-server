from django.db.models.enums import TextChoices
from mongoengine import StringField
from mongoengine.document import DynamicDocument, Document
from mongoengine.fields import DictField, ListField, DateTimeField, ObjectIdField


class NotificationStatus(TextChoices):
    READY = "READY"
    IN_QUEUE = "IN_QUEUE"
    CANCELED = "CANCELED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class NotificationType(TextChoices):
    PRODUCT_DIFF_NOTIFICATION = "PRODUCT_DIFF_NOTIFICATION"
    BRAND_NEW_PRODUCT_NOTIFICATION = "BRAND_NEW_PRODUCT_NOTIFICATION"
    TIMEDEAL_OPEN_NOTIFICATION = "TIMEDEAL_OPEN_NOTIFICATION"
    BRAND_OPEN_NOTIFICATION = "BRAND_OPEN_NOTIFICATION"
    EVENT_NOTIFICATION = "EVENT_NOTIFICATION"
    GENERAL_NOTIFICATION = "GENERAL_NOTIFICATION"


class _Notification:
    status = StringField(choices=NotificationStatus.choices)
    notificationtype = StringField(
        choices=NotificationType.choices, required=True)
    title = StringField(required=True)
    message = StringField(required=True)
    navigateto = StringField()
    referenceid = StringField()
    created = DateTimeField()
    updated = DateTimeField()
    sended = DateTimeField()  # TODO: Deprecate ---> Remove field OR consider renaming ("sent") (API Server DAO should be updated too)
    scheduleddate = DateTimeField(required=True)
    notificationid = StringField()
    mobiles = StringField(required=False)
    deviceids = ListField(StringField())
    result = DictField()  # TODO: Deprecate ---> Remove field (API Server DAO should be updated too)


class Notification(_Notification, DynamicDocument):
    meta = {"collection": "notifications"}


class NotificationLog(Document):
    meta = {"collection": "notification_logs"}
    notificationid = ObjectIdField()
    result = DictField()
    sent = DateTimeField()
