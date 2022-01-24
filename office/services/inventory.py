from typing import List, Optional

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from logistics.protos.inventory_proto import inventory_pb2, inventory_pb2_grpc
from office.services.base import GrpcService


class InventoryService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(cls, product_name: Optional[str]) -> List[dict]:
        print(product_name)
        request = inventory_pb2.InventoryListRequest(product_name=product_name)
        with cls.channel:
            stub = inventory_pb2_grpc.InventoryControllerStub(cls.channel)
            response = stub.List(request)
            return cls.to_array(response)
