from typing import List, Optional

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from office.services.base import GrpcService
from logistics.protos.inventory_proto import inventory_pb2, inventory_pb2_grpc


class InventoryService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(
        cls,
        code: Optional[str] = None,
        product_name: Optional[str] = None,
        product_brand_name: Optional[str] = None,
        product_brand_key_name: Optional[str] = None,
        statuses: Optional[List[str]] = None,
    ) -> List[dict]:
        request = inventory_pb2.InventoryListRequest(
            product_name=product_name,
            product_brand_name=product_brand_name,
            code=code,
            product_brand_key_name=product_brand_key_name,
            statuses=statuses,
        )
        with cls.channel:
            stub = inventory_pb2_grpc.InventoryControllerStub(cls.channel)
            response = stub.List(request)
            return cls.to_dict(response)

    @classmethod
    def delete(
        cls,
        id: int
    ):
        request = inventory_pb2.InventoryRetrieveRequest(
            id=id
        )
        with cls.channel:
            stub = inventory_pb2_grpc.InventoryControllerStub(cls.channel)
            stub.Destroy(request)