from rest_framework import serializers
from django.db import models


class DeliveryType(models.TextChoices):
    DOMESTIC = "DOMESTIC"
    FOREIGN = "FOREIGN"


class DeliveryDescriptionDAOSerializer(serializers.Serializer):
    DeliveryType = serializers.ChoiceField(choices=DeliveryType.choices)
    DeliveryFee = serializers.IntegerField()
    EarliestDeliveryDays = serializers.IntegerField()
    LatestDeliveryDays = serializers.IntegerField()
    Texts = serializers.ListField(child=serializers.CharField())
