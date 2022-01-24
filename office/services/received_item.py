from typing import List

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from protos.logistics.received_item_proto import (
    received_item_pb2,
    received_item_pb2_grpc,
)
from office.services.base import GrpcService


class ReceivedItemService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(cls) -> List[dict]:
        request = received_item_pb2.ReceivedItemListRequest()
        with cls.channel:
            stub = received_item_pb2_grpc.ReceivedItemControllerStub(cls.channel)
            response = stub.List(request)
            return cls.to_array(response)
