from typing import List, Optional

from alloff_backoffice_server.settings import (
    GRPC_LOGISTICS_SERVER_URL,
    GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
)
from django.contrib.auth.models import User
from gen.pyalloff import order_item_pb2, order_item_pb2_grpc
from office.serializers.order_item import OrderItemStatus
from office.serializers.order_payment_adjustment import PaymentAdjustmentType
from office.services.base import GrpcAuthType, GrpcService, grpc_request


class OrderItemService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL
    stub = order_item_pb2_grpc.OrderItemControllerStub

    @classmethod
    @grpc_request(
        order_item_pb2.OrderItemRetrieveRequest,
        auth_types=[GrpcAuthType.COMPANY],
    )
    def Retrieve(
        cls,
        id: str = None,
        user: User = None,
    ):
        pass

    @classmethod
    @grpc_request(
        order_item_pb2.OrderItemListRequest,
        auth_types=[GrpcAuthType.COMPANY],
    )
    def List(
        cls,
        page: int = 1,
        size: int = GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
        search: Optional[str] = None,
        statuses: Optional[List[str]] = None,
        user_id: Optional[str] = None,
        alloff_order_id: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        user: User = None,
    ):
        pass

    @classmethod
    @grpc_request(
        order_item_pb2.OrderItemStatusChangeRequest,
        auth_types=[GrpcAuthType.USER],
    )
    def ChangeStatus(
        cls,
        id: int = None,
        status: OrderItemStatus = None,
        user: User = None,
        courier_id: Optional[int] = None,
        tracking_number: Optional[str] = None,
        tracking_url: Optional[str] = None,
    ) -> dict:
        pass

    @classmethod
    @grpc_request(
        order_item_pb2.OrderItemSetTrackingInfoRequest,
        auth_types=[GrpcAuthType.COMPANY, GrpcAuthType.USER],
    )
    def SetTrackingInfo(
        cls,
        id: int = None,
        courier_id: int = None,
        tracking_number: Optional[str] = None,
        tracking_url: Optional[str] = None,
        user: User = None,
    ) -> dict:
        pass

    @classmethod
    @grpc_request(
        order_item_pb2.OrderItemAddMemoRequest,
        auth_types=[GrpcAuthType.USER],
    )
    def AddMemo(
        cls,
        id: int = None,
        body: str = None,
        user: User = None,
    ) -> dict:
        pass

    @classmethod
    @grpc_request(
        order_item_pb2.OrderItemDeleteMemoRequest,
        auth_types=[GrpcAuthType.USER],
    )
    def DeleteMemo(
        cls,
        id: int = None,
        memo_id: int = None,
        user: User = None,
    ) -> dict:
        pass

    @classmethod
    @grpc_request(
        order_item_pb2.OrderItemForceReceiveRequest,
        auth_types=[GrpcAuthType.USER],
    )
    def ForceReceive(
        cls,
        id: int = None,
        user: User = None,
    ):
        pass

    @classmethod
    @grpc_request(
        order_item_pb2.UpdateRefundRequest,
        auth_types=[GrpcAuthType.USER],
    )
    def UpdateRefund(
        cls,
        id: int = None,
        refund_amount: int = None,
        refund_fee: int = None,
        user: User = None,
    ):
        pass

    @classmethod
    @grpc_request(
        order_item_pb2.OrderItemAdjustPaymentRequest,
        auth_types=[GrpcAuthType.USER],
    )
    def AdjustPayment(
        cls,
        id: int = None,
        user: User = None,
        method: PaymentAdjustmentType = None,
        amount: int = None,
        bank_account_info: Optional[str] = None,
        reason: Optional[str] = None,
    ):
        pass

    @classmethod
    @grpc_request(
        order_item_pb2.OrderItemExcelDataRequest,
        auth_types=[GrpcAuthType.COMPANY],
        keep_channel=True,
    )
    def GetOrderItemExcelData(
        cls,
        user: User = None,
        date_from: str = None,
        date_to: str = None,
    ):
        pass
