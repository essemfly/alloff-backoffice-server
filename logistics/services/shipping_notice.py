from typing import List
from logistics.protos.shipping_notice_proto import (
    shipping_notice_pb2,
    shipping_notice_pb2_grpc,
)
from django_grpc_framework import generics

from logistics.models import ShippingNotice
from logistics.serializers.shipping_notice import ShippingNoticeProtoSerializer
from .base import GrpcService


class ShippingNoticeService(generics.ModelService):
    queryset = ShippingNotice.objects.all()
    serializer_class = ShippingNoticeProtoSerializer


class ShippingNoticeGrpcService(GrpcService):
    url = "ec2-13-209-64-30.ap-northeast-2.compute.amazonaws.com:9000"

    @classmethod
    def list(cls) -> List[dict]:
        request = shipping_notice_pb2.ShippingNoticeListRequest()
        with cls.channel:
            stub = shipping_notice_pb2_grpc.ShippingNoticeControllerStub(cls.channel)
            response = stub.List(request)
            return cls.to_array(response)
