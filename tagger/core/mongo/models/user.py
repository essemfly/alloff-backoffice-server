from mongoengine import EmbeddedDocument, StringField, DateTimeField
from mongoengine.fields import BooleanField


class AlloffUser(EmbeddedDocument):
    _id = StringField()
    name = StringField()
    uuid = StringField()
    email = StringField()
    created = DateTimeField()
    mobile = StringField(required=True)
    baseaddress = StringField()
    detailaddress = StringField()
    postcode = StringField()


class Devices(EmbeddedDocument):
    _id = StringField()
    userid = StringField()
    deviceid = StringField()
    allownotificaion = BooleanField()
