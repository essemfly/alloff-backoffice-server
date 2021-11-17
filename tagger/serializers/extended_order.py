from rest_framework import serializers

from tagger.models import ExtendedOrderItem, ExtendedOrder


class ExtendedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedOrder
        fields = "__all__"


class ExtendedOrderItemSerializer(serializers.ModelSerializer):
    extended_order = ExtendedOrderSerializer()

    class Meta:
        model = ExtendedOrderItem
        fields = "__all__"
