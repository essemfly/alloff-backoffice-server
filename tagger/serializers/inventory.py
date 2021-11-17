from rest_framework import serializers

from tagger.models.inventory import Inventory


class InventorySerializer(serializers.ModelSerializer):
    product_code = serializers.CharField(read_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"
