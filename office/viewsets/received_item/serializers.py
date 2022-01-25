from rest_framework import serializers


class ForceMakeRiSerializer(serializers.Serializer):
    order_item_id = serializers.CharField()
