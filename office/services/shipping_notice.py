from typing import List, Optional
import queue

from alloff_backoffice_server.settings import (
    GRPC_LOGISTICS_SERVER_URL,
    GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
)
from protos.logistics.shipping_notice import (
    shipping_notice_pb2,
    shipping_notice_pb2_grpc,
)
from office.serializers.shipping_notice import ShippingNoticeStatus
from office.services.base import GrpcService


class ShippingNoticeService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def retrieve(cls, id):
        request = shipping_notice_pb2.ShippingNoticeRetrieveRequest(id=id)
        with cls.channel:
            return shipping_notice_pb2_grpc.ShippingNoticeControllerStub(
                cls.channel
            ).Retrieve(request)

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

    @classmethod
    def get_candidates(cls):
        request = shipping_notice_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        with cls.channel:
            return shipping_notice_pb2_grpc.ShippingNoticeControllerStub(
                cls.channel
            ).GetCandidates(request)

    @classmethod
    def submit_candidates(cls, data: List[dict]):
        items = [
            shipping_notice_pb2.ShippingNoticeCandidateSubmitItem(
                order_item_id=x["order_item_id"], inventory_ids=x["inventory_ids"]
            )
            for x in data
        ]
        with cls.channel:
            shipping_notice_pb2_grpc.ShippingNoticeControllerStub(
                cls.channel
            ).SubmitCandidates(
                shipping_notice_pb2.ShippingNoticeCandidateSubmitRequest(
                    candidates=items
                )
            )
