from rest_framework import serializers


class ForceMakeRiSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
