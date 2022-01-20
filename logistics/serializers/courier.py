from rest_framework import serializers
from django_grpc_framework import proto_serializers

from logistics.models import Courier
from logistics.protos.courier_proto import courier_pb2


class CourierProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Courier
        proto_class = courier_pb2.Courier
        fields = "__all__"


class CourierSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    sweettracker_id = serializers.CharField(max_length=6)
    tracking_url_base = serializers.CharField(allow_blank=True)
