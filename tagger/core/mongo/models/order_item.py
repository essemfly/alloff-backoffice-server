from mongoengine import EmbeddedDocumentField, StringField
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import IntField
from tagger.core.mongo.models.alloff_product import EmbeddedAlloffProduct
from tagger.core.mongo.models.product import EmbeddedProduct


class OrderItem(EmbeddedDocument):
    alloffproduct = EmbeddedDocumentField(EmbeddedAlloffProduct)
    product = EmbeddedDocumentField(EmbeddedProduct)
    size = StringField(required=True)
    quantity = IntField(required=True)
