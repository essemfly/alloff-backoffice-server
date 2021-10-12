from mongoengine import DateTimeField, StringField, DynamicDocument
from mongoengine.fields import (
    BooleanField,
    ListField,
    IntField,
)


class AlloffProductGroup(DynamicDocument):
    meta = {"collection": "alloff_products_group"}
    title = StringField(required=True)
    shorttitle = StringField()
    numalarms = IntField(required=False)
    instruction = ListField(StringField(), required=False)
    imgurl = StringField(required=True)
    hidden = BooleanField(required=False)
    created = DateTimeField(required=False)
    starttime = DateTimeField(required=True)
    finishtime = DateTimeField(required=True)
