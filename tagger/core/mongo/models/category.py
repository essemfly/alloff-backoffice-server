from mongoengine import DynamicDocument, StringField
from mongoengine.document import EmbeddedDocument


class _Category:
    name = StringField(required=True)
    keyname = StringField(required=True)
    catidentifier = StringField(required=True)
    brandkeyname = StringField(required=True)


class Category(_Category, DynamicDocument):
    meta = {"collection": "categories"}


class EmbeddedCategory(_Category, EmbeddedDocument):
    meta = {"strict": False}
    pass
