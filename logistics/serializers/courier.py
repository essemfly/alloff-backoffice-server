from django_grpc_framework import proto_serializers
from logistics.models import Courier
from logistics.protos.courier_proto import courier_pb2


class CourierProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Courier
        proto_class = courier_pb2.Courier
        fields = "__all__"
