from rest_framework import serializers


class CourierSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sweettracker_id = serializers.CharField()
    tracking_url_base = serializers.CharField()
