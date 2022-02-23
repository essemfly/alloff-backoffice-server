from typing import List

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from office.services.base import GrpcAuthType, GrpcService, grpc_request
from protos.logistics.courier import courier_pb2, courier_pb2_grpc


class CourierService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL
    stub = courier_pb2_grpc.CourierControllerStub

    @classmethod
    @grpc_request(
        courier_pb2.CourierListRequest,
        auth_types=[GrpcAuthType.ANONYMOUS],
        stream_to_list=True,
    )
    def List(cls) -> List[dict]:
        pass
