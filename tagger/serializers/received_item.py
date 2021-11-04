from rest_framework import serializers
from tagger.models.inventory import Inventory

from tagger.models.received_item import ReceivedItem, Sourcing


class ReceivedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedItem
        fields = "__all__"


class SourcingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sourcing
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"
