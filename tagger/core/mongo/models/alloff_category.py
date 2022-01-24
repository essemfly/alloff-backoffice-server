from django.db.models.enums import TextChoices
from mongoengine import Document, StringField
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import BooleanField, EmbeddedDocumentField, IntField


class AlloffCategoryType(TextChoices):
    NORMAL = "NORMAL"
    NEED_PROCESSING = "NEED_PROCESSING"
    DO_NOT_SHOW = "DO_NOT_SHOW"


class _AlloffCategory:
    name = StringField(required=True)
    imgurl = StringField()
    keyname = StringField(required=True)
    level = IntField(1, 2)
    parentid = StringField()
    type = StringField(choices=AlloffCategoryType.choices)


class AlloffCategory(_AlloffCategory, Document):
    meta = {"collection": "alloff_categories"}


class EmbeddedAlloffCategory(_AlloffCategory, EmbeddedDocument):
    _id = StringField(required=True)


class AlloffCategories(EmbeddedDocument):
    first = EmbeddedDocumentField(EmbeddedAlloffCategory)
    second = EmbeddedDocumentField(EmbeddedAlloffCategory)
    touched = BooleanField(required=True)
    done = BooleanField(required=True)
