import enum

from core.company_auth_viewset import with_company_api
from core.grpc_exception import grpc_exception
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiParameter, extend_schema,
                                   extend_schema_view)
from office.serializers.order_item import *
from office.serializers.product_inquiry import (
    PaginatedProductInquirySerializer, ProductInquirySerializer)
from office.services.product_inquiry import ProductInquiryService
from office.utils.openapi import PROTO_PAGINATION_QUERY_PARAMS
from office.viewsets.pagination import PaginationListMixin
from rest_framework import mixins, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response


class CreateProductInquiryReplySerializer(serializers.Serializer):
    body = serializers.CharField()


class DeleteProductInquiryReplySerializer(serializers.Serializer):
    id = serializers.IntegerField()


class ProductInquiryListStatus(enum.Enum):
    ALL = 0
    PENDING = 1
    REPLIED = 2


@extend_schema_view(
    retrieve=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],
        responses=OrderItemRetrieveSerializer,
    ),
    list=extend_schema(
        responses=PaginatedProductInquirySerializer,
        parameters=PROTO_PAGINATION_QUERY_PARAMS
        + [
            OpenApiParameter(
                "is_pending",
                OpenApiTypes.BOOL,
                OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                "date_from",
                OpenApiTypes.DATE,
                OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                "date_to",
                OpenApiTypes.DATE,
                OpenApiParameter.QUERY,
            ),
        ],
    ),
)
class ProductInquiryViewSet(
    PaginationListMixin,
    mixins.RetrieveModelMixin,
    viewsets.ViewSet,
):
    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductInquirySerializer
        elif self.action == "list":
            return PaginatedProductInquirySerializer
        elif self.action == "create_reply":
            return CreateProductInquiryReplySerializer
        elif self.action == "delete_reply":
            return DeleteProductInquiryReplySerializer
        return ProductInquirySerializer

    @with_company_api
    @grpc_exception
    def retrieve(self, request: Request, pk=None):
        retrieve_response = ProductInquiryService.Retrieve(
            id=int(pk),
            user=request.user,
        )
        serializer = ProductInquirySerializer(retrieve_response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @with_company_api
    @grpc_exception
    def list(self, request: Request, *args, **kwargs):
        is_pending = request.query_params.get("is_pending")
        if is_pending is None:
            list_status = ProductInquiryListStatus.ALL
        elif is_pending == "true":
            list_status = ProductInquiryListStatus.PENDING
        else:
            list_status = ProductInquiryListStatus.REPLIED

        list_response = ProductInquiryService.List(
            status=list_status.value,
            date_from=request.query_params.get("date_from"),
            date_to=request.query_params.get("date_to"),
            user=request.user,
            **self.get_pagination_params(request),
        )
        serializer = PaginatedProductInquirySerializer(list_response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CreateProductInquiryReplySerializer,
        responses=ProductInquirySerializer,
    )
    @action(detail=True, methods=["POST"])
    @with_company_api
    @grpc_exception
    def create_reply(self, request: Request, *args, pk=None, **kwargs):
        serializer = CreateProductInquiryReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = ProductInquiryService.CreateReply(
            id=int(pk),
            body=serializer.validated_data.get("body"),
            user=request.user,
        )
        serializer = ProductInquirySerializer(response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=DeleteProductInquiryReplySerializer,
        responses=None,
    )
    @action(detail=False, methods=["POST"])
    @with_company_api
    @grpc_exception
    def delete_reply(self, request: Request, *args, **kwargs):
        serializer = DeleteProductInquiryReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ProductInquiryService.DeleteReply(
            id=serializer.validated_data.get("id"),
            user=request.user,
        )
        return Response(data=None, status=status.HTTP_200_OK)
