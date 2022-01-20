from typing import List

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from logistics.protos.inventory_proto import inventory_pb2, inventory_pb2_grpc
from office.services.base import GrpcService


class InventoryService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL
    null_if_empty = [
        "deleted_at",
    ]

    @classmethod
    def list(cls) -> List[dict]:
        request = inventory_pb2.InventoryListRequest()
        with cls.channel:
            stub = inventory_pb2_grpc.InventoryControllerStub(cls.channel)
            response = stub.List(request)
            return cls.to_array(response)
