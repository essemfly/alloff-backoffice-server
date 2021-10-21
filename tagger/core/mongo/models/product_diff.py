from typing import Text
from typing_extensions import Required
from django.db.models.enums import Choices, TextChoices
from mongoengine import Document, EmbeddedDocumentField, StringField
from mongoengine.document import DynamicDocument, EmbeddedDocument
from mongoengine.fields import BooleanField, DictField, IntField, ListField, DateTimeField

from tagger.core.mongo.models.product import Product


class ProductDiffType(TextChoices):
    PRICE_DIFF = "price"
    SOLDOUT_DIFF = "soldout"
    SIZE_DIFF = "size"


class _ProductDiff(DynamicDocument):
    newproduct = EmbeddedDocumentField(Product, required=True)
    oldproduct = EmbeddedDocumentField(Product, required=True)
    diff_type = StringField(choices=ProductDiffType.choices,
                            required=True, db_column="type")
    ispushed = BooleanField(required=True)
    _id = StringField(required=True)


class ProductDiff(_ProductDiff, Document):
    meta = {"collection": "product_diffs"}
