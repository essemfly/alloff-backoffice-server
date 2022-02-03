from typing import List, Optional

from alloff_backoffice_server.settings import (
    GRPC_LOGISTICS_SERVER_URL,
    GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
)
from office.serializers.order_item import OrderItemStatus
from django.contrib.auth.models import User
from protos.order.order_item import (
    order_item_pb2,
    order_item_pb2_grpc,
)
from office.services.base import GrpcService


class OrderItemService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def retrieve(cls, id):
        request = order_item_pb2.OrderItemRetrieveRequest(id=id)
        with cls.channel:
            return order_item_pb2_grpc.OrderItemControllerStub(cls.channel).Retrieve(
                request
            )

    @classmethod
    def list(
        cls,
        page: int = 1,
        size: int = GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
        search: Optional[str] = None,
        statuses: Optional[List[str]] = None,
        user_id: Optional[str] = None,
    ):
        request = order_item_pb2.OrderItemListRequest(
            size=size,
            page=page,
            search=search,
            statuses=statuses,
            user_id=user_id,
        )
        with cls.channel:
            return order_item_pb2_grpc.OrderItemControllerStub(cls.channel).List(
                request
            )

    @classmethod
    def change_status(
        cls,
        id: int,
        status: OrderItemStatus,
        user: User,
        tracking_number: Optional[str] = None,
        tracking_url: Optional[str] = None,
    ) -> dict:
        request = order_item_pb2.OrderItemStatusChangeRequest(
            id=id,
            status=status,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            **cls.get_userinfo(user),
        )
        with cls.channel:
            return order_item_pb2_grpc.OrderItemControllerStub(
                cls.channel
            ).ChangeStatus(request)

    @classmethod
    def add_memo(
        cls,
        id: int,
        body: str,
        user: User,
    ) -> dict:
        request = order_item_pb2.OrderItemAddMemoRequest(
            id=id,
            body=body,
            **cls.get_userinfo(user),
        )
        with cls.channel:
            return order_item_pb2_grpc.OrderItemControllerStub(cls.channel).AddMemo(
                request
            )

    @classmethod
    def delete_memo(cls, id: int, memo_id: int, user: User) -> dict:
        request = order_item_pb2.OrderItemDeleteMemoRequest(
            id=id,
            memo_id=memo_id,
            **cls.get_userinfo(user),
        )
        with cls.channel:
            return order_item_pb2_grpc.OrderItemControllerStub(cls.channel).DeleteMemo(
                request
            )

    @classmethod
    def force_receive(cls, id, user: User):
        request = order_item_pb2.OrderItemForceReceiveRequest(
            id=id, **cls.get_userinfo(user)
        )
        with cls.channel:
            return order_item_pb2_grpc.OrderItemControllerStub(
                cls.channel
            ).ForceReceive(request)