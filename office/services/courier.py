from typing import List
from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL

from logistics.protos.courier_proto import courier_pb2, courier_pb2_grpc
from office.services.base import GrpcService


class CourierService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(cls) -> List[dict]:
        request = courier_pb2.CourierListRequest()
        with cls.channel:
            return courier_pb2_grpc.CourierControllerStub(cls.channel).List(request)
