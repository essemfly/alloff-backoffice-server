from bson import ObjectId
from django.db import models
from shortuuid import ShortUUID

from alloff_backoffice_server.settings import CODE_CHARSET
from tagger.models.inventory import ProductType


class ExtendedOrder(models.Model):
    code = models.CharField(max_length=10, unique=True, db_index=True, null=False)
    order_id = models.CharField(max_length=30, unique=True, db_index=True, null=False)

    # orderstatus = models.CharField(max_length=30, choices=OrderStatus.choices)
    ordered_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def make(order, force_update=False) -> "ExtendedOrder":
        order_id = str(order.id)
        eo = ExtendedOrder.objects.filter(order_id=order_id).first()

        if not force_update and eo is not None:
            raise BaseException(f"Order {order_id} is already extended!")

        if eo is None:
            print(f"eo not found for order {order.id}, making one...")
            eo = ExtendedOrder.objects.create(
                order_id=order_id,
                ordered_at=order.created,
                # orderstatus=order.orderstatus,
            )
            print(f"order {order.id} - eo {eo.code}")

        if eo.extendedorderitem_set.count() != len(order.orders):
            print(f"order items not extended correctly for eo {eo.code}.. purging and remaking")
            from tagger.models.extended_order_item import ExtendedOrderItem
            eo.extendedorderitem_set.all().delete()
            for item in order.orders:
                product_type = ProductType.TIMEDEAL_PRODUCT if item.alloffproduct is not None else ProductType.NORMAL_PRODUCT
                product = item.alloffproduct if item.alloffproduct is not None else item.product
                eoi = ExtendedOrderItem.objects.create(
                    product_type=product_type,
                    product_id=product._id,
                    name=product.name,
                    brand_keyname=product.brand.keyname,
                    size=item.size,
                    quantity=item.quantity,
                    extended_order=eo
                )
                print(f"{eo.code} - {eoi.product_code}")

        return eo

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.code is None or self.code == "":
            self.code = ExtendedOrder.generate_usable_code()
        return super().save(force_insert, force_update, using, update_fields)

    @staticmethod
    def generate_usable_code():
        code = ""
        is_unique = False

        while not is_unique:
            code = ExtendedOrder._make_code()
            if ExtendedOrder.objects.filter(code=code).count() == 0:
                is_unique = True

        return code

    @staticmethod
    def _make_code():
        return ShortUUID(CODE_CHARSET).random(length=5)

    @property
    def order(self):
        from tagger.core.mongo.models.order import Order
        return Order.objects(id=ObjectId(self.order_id)).first()
