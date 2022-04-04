from typing import Optional

from alloff_backoffice_server.settings import (
    GRPC_LOGISTICS_SERVER_URL, GRPC_PAGINATION_DEFAULT_PAGE_SIZE)
from django.contrib.auth.models import User
from gen.pyalloff import product_inquiry_pb2, product_inquiry_pb2_grpc
from office.services.base import GrpcAuthType, GrpcService, grpc_request


class ProductInquiryService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL
    stub = product_inquiry_pb2_grpc.ProductInquiryControllerStub

    @classmethod
    @grpc_request(
        product_inquiry_pb2.ProductInquiryRetrieveRequest,
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
        product_inquiry_pb2.ProductInquiryListRequest,
        auth_types=[GrpcAuthType.COMPANY],
    )
    def List(
        cls,
        page: int = 1,
        size: int = GRPC_PAGINATION_DEFAULT_PAGE_SIZE,
        search: Optional[str] = None,
        status=None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        user: User = None,
    ):
        pass

    @classmethod
    @grpc_request(
        product_inquiry_pb2.ProductInquiryReplyCreateRequest,
        auth_types=[GrpcAuthType.COMPANY, GrpcAuthType.USER],
    )
    def CreateReply(
        cls,
        id: int = None,
        body: str = None,
        user: User = None,
    ) -> dict:
        pass

    @classmethod
    @grpc_request(
        product_inquiry_pb2.ProductInquiryReplyDestroyRequest,
        auth_types=[GrpcAuthType.COMPANY],
    )
    def DeleteReply(
        cls,
        id: int = None,
        user: User = None,
    ) -> dict:
        pass
