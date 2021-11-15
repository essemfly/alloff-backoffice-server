from rest_framework import serializers

from tagger.models.received_item import Sourcing


class SourcingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sourcing
        fields = "__all__"

