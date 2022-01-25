from typing import List

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from order.models.order_item import OrderItem
from protos.logistics.received_item_proto import (
    received_item_pb2,
    received_item_pb2_grpc,
)
from office.services.base import GrpcService


class ReceivedItemService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(cls) -> List[received_item_pb2.ReceivedItem]:
        request = received_item_pb2.ReceivedItemListRequest()
        with cls.channel:
            stub = received_item_pb2_grpc.ReceivedItemControllerStub(cls.channel)
            response = stub.List(request)
            return cls.to_array(response)

    @classmethod
    def make(cls, item: OrderItem) -> List[received_item_pb2.ReceivedItem]:
        request = received_item_pb2.MakeReceivedItemRequest(
            order_id=item.order_id,
            order_item_id=item.order_item_id,
            code=item.code,
            product_brand_id=item.product_brand_id,
            product_brand_name=item.product_brand_name,
            product_brand_key_name=item.product_brand_key_name,
            product_id=item.product_id,
            product_name=item.product_name,
            product_size=item.size,
            product_color=item.color,
            quantity=item.quantity,
        )

        with cls.channel:
            stub = received_item_pb2_grpc.ReceivedItemControllerStub(cls.channel)
            response = stub.Make(request)
            return cls.to_array(response)
