from rest_framework import serializers

from tagger.models.courier import Courier
from tagger.models.package import Package
from tagger.models.shipping_notice import ShippingNotice, ShippingNoticeItem


class ShippingNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingNotice
        fields = "__all__"


class ShippingNoticeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingNoticeItem
        fields = "__all__"


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = "__all__"
