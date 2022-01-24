from mongoengine import EmbeddedDocumentField, StringField
from mongoengine.document import EmbeddedDocument, DynamicDocument
from mongoengine.fields import BooleanField, IntField, ListField, DateTimeField, DictField

from tagger.core.mongo.models.alloff_category import AlloffCategories
from tagger.core.mongo.models.brand import EmbeddedBrand
from tagger.core.mongo.models.category import EmbeddedCategory


class _Product:
    productid = StringField(required=True)
    name = StringField(required=True)
    images = ListField(StringField())
    removed = BooleanField()
    soldout = BooleanField()
    brand = EmbeddedDocumentField(EmbeddedBrand, required=True)
    category = EmbeddedDocumentField(EmbeddedCategory, required=True)
    alloffcategories = EmbeddedDocumentField(AlloffCategories, required=True)
    producturl = StringField(required=True)
    discountrate = IntField(required=True)
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)
    discountedprice = IntField(required=True)
    isupdated = BooleanField(required=True)
    canceldescription = ListField(StringField(), required=True)
    originalprice = StringField(required=True)
    deliverydescription = ListField(StringField(), required=True)
    isimagecached = StringField(required=True)
    isnewlycrawled = StringField(required=True)
    sizeavailable = StringField(required=True)
    description = DictField(required=False)


class Product(_Product, DynamicDocument):
    meta = {"collection": "products"}


class EmbeddedProduct(_Product, EmbeddedDocument):
    meta = {"strict": False}
    _id = StringField(required=True)
