from typing import List, Optional

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL, GRPC_PAGINATION_DEFAULT_PAGE_SIZE
from order.models.order_item import OrderItem
from logistics.protos.received_item_proto import (
    received_item_pb2,
    received_item_pb2_grpc,
)
from office.services.base import GrpcService


class ReceivedItemService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(
        cls,
        page: int = 1,
        size: int = GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
        search: Optional[str] = None,
        statuses: Optional[List[str]] = None,
    ) -> List[dict]:
        request = received_item_pb2.ReceivedItemListRequest(
            size=size,
            page=page,
            search=search,
            statuses=statuses,
        )
        with cls.channel:
            return received_item_pb2_grpc.ReceivedItemControllerStub(cls.channel).List(
                request
            )

    @classmethod
    def receive(cls, id: int) -> dict:
        request = received_item_pb2.ReceivedItemRetrieveRequest(id=id)
        with cls.channel:
            stub = received_item_pb2_grpc.ReceivedItemControllerStub(cls.channel)
            return stub.Receive(request)

    @classmethod
    def force_make(cls, item: OrderItem, quantity: int) -> List[dict]:
        request = received_item_pb2.MakeReceivedItemRequest(
            order_id=item.order_id,
            order_item_id=item.id,
            order_item_code=item.order_item_code,
            brand_korname=item.brand_korname,
            brand_keyname=item.brand_keyname,
            product_id=item.product_id,
            product_img=item.product_img,
            product_name=item.product_name,
            size=item.size,
            color=item.color,
            item_quantity=item.quantity,
            request_quantity=quantity,
            force=True,
        )

        with cls.channel:
            stub = received_item_pb2_grpc.ReceivedItemControllerStub(cls.channel)
            response = stub.Make(request)
            return cls.to_array(response)

    @classmethod
    def make(cls, item: OrderItem) -> List[dict]:
        request = received_item_pb2.MakeReceivedItemRequest(
            order_id=item.order_id,
            order_item_id=item.id,
            order_item_code=item.order_item_code,
            brand_korname=item.brand_korname,
            brand_keyname=item.brand_keyname,
            product_id=item.product_id,
            product_img=item.product_img,
            product_name=item.product_name,
            size=item.size,
            color=item.color,
            item_quantity=item.quantity,
            request_quantity=item.quantity,
            force=False,
        )

        with cls.channel:
            stub = received_item_pb2_grpc.ReceivedItemControllerStub(cls.channel)
            response = stub.Make(request)
            return cls.to_array(response)
