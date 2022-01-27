from typing import List, Optional

from alloff_backoffice_server.settings import (
    GRPC_LOGISTICS_SERVER_URL,
    GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
)

from protos.order.order_item import (
    order_item_pb2,
    order_item_pb2_grpc,
)
from office.services.base import GrpcService


class OrderItemService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(
        cls,
        page: int = 1,
        size: int = GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
        search: Optional[str] = None,
        statuses: Optional[List[str]] = None,
    ) -> List[dict]:
        request = order_item_pb2.OrderItemListRequest(
            size=size,
            page=page,
            search=search,
            statuses=statuses,
        )
        with cls.channel:
            return order_item_pb2_grpc.OrderItemControllerStub(cls.channel).List(
                request
            )
