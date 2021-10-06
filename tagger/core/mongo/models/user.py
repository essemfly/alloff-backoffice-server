from mongoengine import EmbeddedDocument, StringField, DateTimeField


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
