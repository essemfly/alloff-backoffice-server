from typing import List, Optional

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from gen.pyalloff import inventory_pb2, inventory_pb2_grpc
from office.services.base import GrpcService


class InventoryService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(
        cls,
        page: int = None,
        size: int = None,
        search: str = None,
        statuses: Optional[List[str]] = None,
    ) -> List[dict]:
        request = inventory_pb2.InventoryListRequest(
            page=page,
            size=size,
            search=search,
            statuses=statuses,
        )
        with cls.channel:
            return inventory_pb2_grpc.InventoryControllerStub(cls.channel).List(request)

    @classmethod
    def delete(cls, id: int):
        request = inventory_pb2.InventoryRetrieveRequest(id=id)
        with cls.channel:
            stub = inventory_pb2_grpc.InventoryControllerStub(cls.channel)
            stub.Destroy(request)
