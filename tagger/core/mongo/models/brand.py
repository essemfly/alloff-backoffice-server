from mongoengine import (
    DateTimeField,
    DynamicDocument,
    EmbeddedDocumentField,
    IntField,
    StringField,
)
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import BooleanField, EmbeddedDocumentListField, ListField
from tagger.core.mongo.models.category import EmbeddedCategory


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
    category = EmbeddedDocumentListField(EmbeddedCategory)


class Brand(_Brand, DynamicDocument):
    meta = {"collection": "brands"}


class EmbeddedBrand(_Brand, EmbeddedDocument):
    meta = {"strict": False}
    _id = StringField(required=True)
