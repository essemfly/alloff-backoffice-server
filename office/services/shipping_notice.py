import queue
from typing import List, Optional, TypedDict

from alloff_backoffice_server.settings import (
    GRPC_LOGISTICS_SERVER_URL,
    GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
)
from office.serializers.shipping_notice import ShippingNoticeStatus
from office.serializers.shipping_notice_item import ShippingNoticeItemRemovalType
from office.services.base import GrpcService
from protos.logistics.shipping_notice import (
    shipping_notice_pb2,
    shipping_notice_pb2_grpc,
)


class PackageTrackingPair(TypedDict):
    package_code: str
    tracking_number: str


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
    def remove_item(
        cls, id: int, item_id: int, removal_type: ShippingNoticeItemRemovalType
    ):
        request = shipping_notice_pb2.ShippingNoticeRemoveItemRequest(
            id=id,
            item_id=item_id,
            removal_type=removal_type,
        )
        with cls.channel:
            return shipping_notice_pb2_grpc.ShippingNoticeControllerStub(
                cls.channel
            ).RemoveItem(request)

    @classmethod
    def move_item(cls, id: int, item_id: int, target_id: int, source_id: int):
        request = shipping_notice_pb2.ShippingNoticeMoveItemRequest(
            id=id,
            item_id=item_id,
            target_id=target_id,
            source_id=source_id,
        )
        with cls.channel:
            return shipping_notice_pb2_grpc.ShippingNoticeControllerStub(
                cls.channel
            ).MoveItem(request)

    @classmethod
    def lock_and_package(cls, id: int):
        request = shipping_notice_pb2.ShippingNoticeRetrieveRequest(id=id)
        with cls.channel:
            return shipping_notice_pb2_grpc.ShippingNoticeControllerStub(
                cls.channel
            ).LockAndPackage(request)

    @classmethod
    def record_shipping_template(cls, id: int, template_url: str):
        request = shipping_notice_pb2.RecordShippingTemplateRequest(
            id=id, template_url=template_url
        )
        with cls.channel:
            return shipping_notice_pb2_grpc.ShippingNoticeControllerStub(
                cls.channel
            ).RecordShippingTemplate(request)

    @classmethod
    def submit_tracking_excel(cls, tracking_pairs: List[PackageTrackingPair]):
        request = shipping_notice_pb2.SubmitTrackingExcelRequest(
            id=id,
            tracking_pairs=[
                shipping_notice_pb2.PackageTrackingPair(**pair)
                for pair in tracking_pairs
            ],
        )
        with cls.channel:
            return shipping_notice_pb2_grpc.ShippingNoticeControllerStub(
                cls.channel
            ).SubmitTrackingExcel(request)

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
