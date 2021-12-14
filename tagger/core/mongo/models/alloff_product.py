from mongoengine import DateTimeField, Document, EmbeddedDocumentField, StringField
from mongoengine.document import DynamicDocument, EmbeddedDocument
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
    images = ListField(StringField(), required=False)
    thumbnail = StringField(required=False)


class _AlloffProductTemplate:
    brand = EmbeddedDocumentField(EmbeddedBrand, required=True)
    canceldescription = ListField(StringField(), required=True)
    deliverydescription = ListField(StringField(), required=True)
    description = ListField(StringField(), default=list)
    discountedprice = IntField(required=True)
    discountrate = IntField(required=True)
    faults = EmbeddedDocumentListField(Fault, default=list)
    images = ListField(StringField(), required=True)
    instruction = EmbeddedDocumentField(Instruction, required=True)
    name = StringField(required=True)
    originalprice = IntField(required=True)
    producttype = ListField(StringField(), required=True)
    sizedescription = ListField(StringField(), default=list)
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)
    removed = BooleanField()


class _AlloffProduct(_AlloffProductTemplate):
    productgroupid = StringField(required=True)
    inventory = EmbeddedDocumentListField(Inventory, required=True)
    soldout = BooleanField(required=True)
    templateId = StringField(required=False)


class AlloffProductTemplate(_AlloffProductTemplate, DynamicDocument):
    meta = {"collection": "alloff_products_templates"}


class AlloffProduct(_AlloffProduct, DynamicDocument):
    meta = {"collection": "alloff_products"}


class EmbeddedAlloffProduct(_AlloffProduct, EmbeddedDocument):
    _id = StringField(required=True)
    pass
