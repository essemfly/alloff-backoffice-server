from mongoengine import (
    DateTimeField,
    DynamicDocument,
    EmbeddedDocumentField,
    IntField,
    StringField,
)
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import BooleanField, EmbeddedDocumentListField, ListField


class SizeGuide(EmbeddedDocument):
    label = StringField(required=True)
    imgurl = StringField(required=True)


class _Brand:
    keyname = StringField(required=True)
    created = DateTimeField(required=True)
    engname = StringField(required=True)
    korname = StringField(required=True)
    logoimgurl = StringField(required=True)
    onpopular = BooleanField(required=True)
    description = StringField(required=True)
    isopen = BooleanField(required=True)
    modulename = StringField(required=True)
    maxdiscountrate = IntField(required=True)
    numnewproducts = IntField(required=True)
    sizeguide = EmbeddedDocumentListField(SizeGuide)


class Brand(_Brand, Document):
    meta = {"collection": "brands"}


class EmbeddedBrand(_Brand, EmbeddedDocument):
    _id = StringField(required=True)
