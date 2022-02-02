from django_grpc_framework import proto_serializers
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer


@extend_schema_serializer(many=False)
class PaginationSerializer(proto_serializers.ProtoSerializer):
    count = serializers.IntegerField()
    results = serializers.ListField(serializers.DictField())
    next = serializers.IntegerField()
    previous = serializers.IntegerField()
