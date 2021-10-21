from mongoengine import EmbeddedDocument, StringField, DateTimeField, Document
from mongoengine.fields import BooleanField
from mongoengine.queryset.transform import update


class AlloffUser(EmbeddedDocument):
    meta = {"collection": "users"}
    _id = StringField()
    name = StringField()
    uuid = StringField()
    email = StringField()
    created = DateTimeField()
    mobile = StringField(required=True)
    baseaddress = StringField()
    detailaddress = StringField()
    postcode = StringField()


class Device(Document):
    meta = {"collection": "devices"}
    userid = StringField()
    deviceid = StringField()
    allownotification = BooleanField()
    updated = DateTimeField()
    created = DateTimeField()
