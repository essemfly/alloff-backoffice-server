from typing import List

from logistics.protos.courier_proto import courier_pb2, courier_pb2_grpc
from office.services.base import GrpcService


# Create your views here.
class CourierService(GrpcService):
    url = "ec2-13-209-64-30.ap-northeast-2.compute.amazonaws.com:9000"
    @classmethod
    def list(cls) -> List[dict]:
        request = courier_pb2.CourierListRequest()
        with cls.channel:
            stub = courier_pb2_grpc.CourierControllerStub(cls.channel)
            response = stub.List(request)
            return cls.to_array(response)
