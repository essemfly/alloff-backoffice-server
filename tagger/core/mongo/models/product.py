from mongoengine import Document, EmbeddedDocumentField, StringField
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import BooleanField, IntField, ListField, DateTimeField
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


class Product(_Product, Document):
    meta = {"collection": "products"}


class EmbeddedProduct(_Product, EmbeddedDocument):
    _id = StringField(required=True)
