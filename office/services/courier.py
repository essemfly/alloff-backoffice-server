from typing import List
import grpc
from logistics.protos.courier_proto import courier_pb2, courier_pb2_grpc
from google.protobuf.json_format import MessageToDict


# Create your views here.
class CourierService:
    url = "ec2-13-209-64-30.ap-northeast-2.compute.amazonaws.com:9000"

    @classmethod
    def ListProducts(cls) -> dict:
        request = courier_pb2.CourierListRequest()
        with grpc.insecure_channel(cls.url) as channel:
            stub = courier_pb2_grpc.CourierControllerStub(channel)
            response = stub.List(request)

            return [MessageToDict(x, preserving_proto_field_name=True) for x in response]
