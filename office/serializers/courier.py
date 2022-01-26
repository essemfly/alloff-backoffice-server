from rest_framework import serializers
from django_grpc_framework import proto_serializers


class CourierSerializer(proto_serializers.ProtoSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    sweettracker_id = serializers.CharField(max_length=6)
    tracking_url_base = serializers.CharField(allow_blank=True)
