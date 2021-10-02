from mongoengine import DateTimeField, Document, EmbeddedDocumentField, StringField
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import (
    BooleanField,
    EmbeddedDocumentListField,
    ListField,
    IntField,
)
from tagger.core.mongo.models.brand import EmbeddedBrand


class Fault(EmbeddedDocument):
    image = StringField(required=True)
    description = StringField(required=True)


class Inventory(EmbeddedDocument):
    size = StringField(required=True)
    quantity = IntField(required=True)


class Instruction(EmbeddedDocument):
    title = StringField(required=True)
    description = ListField(StringField(), required=True)


class _AlloffProduct:
    name = StringField(required=True)
    productgroupid = StringField(required=True)
    description = ListField(StringField(), required=True)
    brand = EmbeddedDocumentField(EmbeddedBrand, required=True)
    faults = EmbeddedDocumentListField(Fault, required=True)
    inventory = EmbeddedDocumentListField(Inventory, required=True)
    instruction = EmbeddedDocumentField(Instruction, required=True)
    sizedescription = ListField(StringField(), required=True)
    canceldescription = ListField(StringField(), required=True)
    producttype = ListField(StringField(), required=True)
    deliverydescription = ListField(StringField(), required=True)
    images = ListField(StringField(), required=True)
    removed = BooleanField(required=True)
    soldout = BooleanField(required=True)
    originalprice = IntField(required=True)
    discountedprice = IntField(required=True)
    discountrate = IntField(required=True)
    templateId = StringField()
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)


class AlloffProduct(_AlloffProduct, Document):
    meta = {"collection": "alloff_products"}


class EmbeddedAlloffProduct(_AlloffProduct, EmbeddedDocument):
    pass
