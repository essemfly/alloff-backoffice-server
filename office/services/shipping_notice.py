from typing import List, Optional

from alloff_backoffice_server.settings import (
    GRPC_LOGISTICS_SERVER_URL,
    GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
)
from logistics.protos.shipping_notice_proto import (
    shipping_notice_pb2,
    shipping_notice_pb2_grpc,
)
from office.serializers.shipping_notice import ShippingNoticeStatus
from office.services.base import GrpcService


class ShippingNoticeService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(
        cls,
        page: int = 1,
        size: int = GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
        search: Optional[str] = None,
        statuses: Optional[List[ShippingNoticeStatus]] = None,
    ):
        request = shipping_notice_pb2.ShippingNoticeListRequest(
            page=page,
            size=size,
            search=search,
            statuses=statuses,
        )
        with cls.channel:
            return shipping_notice_pb2_grpc.ShippingNoticeControllerStub(
                cls.channel
            ).List(request)
