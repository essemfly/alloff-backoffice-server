from typing import List
from logistics.protos.courier_proto import courier_pb2, courier_pb2_grpc
from django_grpc_framework import generics

from logistics.models import Courier
from logistics.serializers.courier import CourierProtoSerializer
from .base import GrpcService


class CourierService(generics.ModelService):
    queryset = Courier.objects.all()
    serializer_class = CourierProtoSerializer


class CourierGrpcService(GrpcService):
    url = "ec2-13-209-64-30.ap-northeast-2.compute.amazonaws.com:9000"

    @classmethod
    def list(cls) -> List[dict]:
        request = courier_pb2.CourierListRequest()
        with cls.channel:
            stub = courier_pb2_grpc.CourierControllerStub(cls.channel)
            response = stub.List(request)
            return cls.to_array(response)
