from core.company_auth_viewset import with_company_api
from core.grpc_exception import grpc_exception
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiParameter, extend_schema,
                                   extend_schema_view)
from office.serializers.order_item import *
from office.services.order_item import OrderItemService
from office.utils.openapi import PROTO_PAGINATION_QUERY_PARAMS
from office.viewsets.order_items.logics.add_memo import \
    AddOrderItemMemoSerializer
from office.viewsets.order_items.logics.change_status import (
    ApiTrackingInfoSerializer, ChangeStatusSerializer)
from office.viewsets.order_items.logics.delete_memo import \
    DeleteItemOrderMemoSerializer
from office.viewsets.pagination import PaginationListMixin
from rest_framework import mixins, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response


@extend_schema_view(
    retrieve=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],
        responses=OrderItemRetrieveSerializer,
    ),
    list=extend_schema(
        responses=PaginatedOrderItemSerializer,
        parameters=PROTO_PAGINATION_QUERY_PARAMS
        + [
            OpenApiParameter(
                "statuses",
                {
                    "type": "array",
                    "items": {"type": "string", "enum": OrderItemStatus.values},
                },
                OpenApiParameter.QUERY,
                explode=True,
            ),
            OpenApiParameter(
                "user_id",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                "alloff_order_id",
                OpenApiTypes.STR,
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
class OrderItemViewSetBase(
    PaginationListMixin,
    mixins.RetrieveModelMixin,
    viewsets.ViewSet,
):
    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderItemRetrieveSerializer
        if self.action == "list":
            return PaginatedOrderItemSerializer
        elif self.action == "change_status":
            return ChangeStatusSerializer
        elif self.action == "add_memo":
            return AddOrderItemMemoSerializer
        elif self.action == "delete_memo":
            return DeleteItemOrderMemoSerializer
        elif self.action == "force_receive":
            return None
        elif self.action == "tracking_info":
            return ApiTrackingInfoSerializer
        return OrderItemListSerializer

    @with_company_api
    @grpc_exception
    def retrieve(self, request: Request, pk=None):
        retrieve_response = OrderItemService.Retrieve(
            id=pk,
            user=request.user,
        )
        serializer = OrderItemRetrieveSerializer(retrieve_response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @with_company_api
    @grpc_exception
    def list(self, request: Request, *args, **kwargs):
        list_response = OrderItemService.List(
            statuses=request.query_params.getlist("statuses"),
            user_id=request.query_params.get("user_id"),
            alloff_order_id=request.query_params.get("alloff_order_id"),
            date_from=request.query_params.get("date_from"),
            date_to=request.query_params.get("date_to"),
            user=request.user,
            **self.get_pagination_params(request),
        )
        serializer = PaginatedOrderItemSerializer(list_response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
