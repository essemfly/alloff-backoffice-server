from rest_framework import serializers

from tagger.core.mongo.models.order import OrderStatus
from tagger.models.courier import Courier
from tagger.models.package import Package
from tagger.models.shipping_notice import ShippingNotice, ShippingNoticeItem
from tagger.serializers.extended_order import ExtendedOrderItemSerializer
from tagger.serializers.inventory import InventorySerializer


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = "__all__"


class ShippingNoticeItemSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer()
    item = ExtendedOrderItemSerializer()

    class Meta:
        model = ShippingNoticeItem
        fields = ["inventory", "item"]


class PackageOrderStatusesSerializer(serializers.Serializer):
    code = serializers.CharField()
    status = serializers.ChoiceField(OrderStatus.choices)


class PackageSerializer(serializers.ModelSerializer):
    shipping_notice_items = ShippingNoticeItemSerializer(many=True)
    tracking_url = serializers.CharField()
    courier = CourierSerializer()
    order_statuses_by_code = PackageOrderStatusesSerializer(many=True)

    class Meta:
        model = Package
        fields = "__all__"


class ShippingNoticeSerializer(serializers.ModelSerializer):
    items = ShippingNoticeItemSerializer(many=True)
    packages = PackageSerializer(many=True)

    class Meta:
        model = ShippingNotice
        fields = "__all__"
