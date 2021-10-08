from mongoengine import DateTimeField, StringField, DynamicDocument
from mongoengine.fields import (
    BooleanField,
    ListField,
    IntField,
)


class AlloffProductGroup(DynamicDocument):
    meta = {"collection": "alloff_products_group"}
    title = StringField()
    shorttitle = StringField()
    numalarms = IntField(required=True)
    instruction = ListField(StringField(), required=True)
    imgurl = StringField(required=True)
    hidden = BooleanField(required=True)
    created = DateTimeField(required=True)
    starttime = DateTimeField(required=True)
    finishtime = DateTimeField(required=True)
