from rest_framework import serializers

from tagger.models.received_item import ReceivedItem


class ReceivedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedItem
        fields = "__all__"

