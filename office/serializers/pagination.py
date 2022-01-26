from django_grpc_framework import proto_serializers
from rest_framework import serializers


class PaginationSerializer(proto_serializers.ProtoSerializer):
    count = serializers.IntegerField()
    results = serializers.ListField(serializers.DictField())
    next = serializers.IntegerField()
    previous = serializers.IntegerField()
