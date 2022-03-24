from core.company_auth_viewset import with_company_api
from core.grpc_exception import grpc_exception
from django.http import HttpResponse
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiParameter, extend_schema,
                                   extend_schema_view)
from office.serializers.order_item import *
from office.services.order_item import OrderItemService
from office.utils.openapi import PROTO_PAGINATION_QUERY_PARAMS
from office.viewsets.order_items.logics.add_memo import \
    AddOrderItemMemoSerializer
from office.viewsets.order_items.logics.change_status import (
    ApiTrackingInfoSerializer, ChangeStatusSerializer,
    OrderItemExcelDataRequestSerializer)
from office.viewsets.order_items.logics.delete_memo import \
    DeleteItemOrderMemoSerializer
from office.viewsets.order_items.logics.make_excel import make_order_item_excel
from office.viewsets.pagination import PaginationListMixin
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
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
        elif self.action == "get_order_item_excel":
            return OrderItemExcelDataRequestSerializer
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

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "date_from", OpenApiTypes.DATE, OpenApiParameter.QUERY, required=True
            ),
            OpenApiParameter(
                "date_to", OpenApiTypes.DATE, OpenApiParameter.QUERY, required=True
            ),
        ],
        request=OrderItemExcelDataRequestSerializer,
        responses=OpenApiTypes.BINARY,
    )
    @action(detail=False, methods=["GET"])
    @with_company_api
    @grpc_exception
    def get_order_item_excel(self, request: Request, *args, **kwargs):
        if "date_from" not in request.query_params:
            raise ValidationError("date_from is required")
        if "date_to" not in request.query_params:
            raise ValidationError("date_to is required")
        date_from = request.query_params.get("date_from")
        date_to = request.query_params.get("date_to")
        channel, stream = OrderItemService.GetOrderItemExcelData(
            date_from=date_from,
            date_to=date_to,
            user=request.user,
        )
        with channel:
            response = HttpResponse(content=make_order_item_excel(stream))
            response[
                "Content-Type"
            ] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            response[
                "Content-Disposition"
            ] = f"attachment; filename=order_items_{date_from}-{date_to}.xlsx"
            return response

    @extend_schema(
        responses={status.HTTP_200_OK: OrderItemListSerializer},
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["POST"])
    @with_company_api
    def change_status(self, request: Request, pk=None):
        serializer = ChangeStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = OrderItemService.ChangeStatus(
            id=int(pk),
            status=serializer.validated_data.get("status"),
            courier_id=serializer.validated_data.get("courier_id"),
            tracking_number=serializer.validated_data.get("tracking_number"),
            tracking_url=serializer.validated_data.get("tracking_url"),
            user=request.user,
        )
        return Response(
            OrderItemRetrieveSerializer(item).data, status=status.HTTP_200_OK
        )
