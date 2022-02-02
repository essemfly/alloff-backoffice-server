from rest_framework import serializers


class AddOrderItemMemoSerializer(serializers.Serializer):
    body = serializers.CharField(required=True)
