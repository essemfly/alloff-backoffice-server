from typing import Optional, Tuple

from alloff_backoffice_server.settings import COMPANY_API_HEADER
from core.grpc_exception import grpc_exception
from django.http.request import HttpRequest
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiParameter, extend_schema,
                                   extend_schema_view)
from office.models.api import ApiKey, ApiKeyStatus
from office.models.company import CompanyStatus
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


class CustomViewSet(viewsets.ViewSet):
    def initialize_request(self, request, *args, **kwargs):
        request, _ = self._set_request_user(request)

        return super().initialize_request(request, *args, **kwargs)

    def _set_request_user(self, request: HttpRequest) -> Tuple[HttpRequest, ApiKey]:
        api_key = self._get_api_key(request)
        if api_key is None:
            return request, None
        request._force_auth_user = api_key.api_user
        return request, api_key

    def _get_api_key(self, request: HttpRequest) -> Optional[ApiKey]:
        try:
            api_key_value: str = request.headers[COMPANY_API_HEADER]
            api_key = ApiKey.objects.get(key=api_key_value)
            if api_key.status != ApiKeyStatus.ACTIVE:
                raise APIException("Api key is inactive")
            elif api_key.company.status != CompanyStatus.ACTIVE:
                raise APIException("Company is inactive")
            return api_key
        except KeyError:
            return None
        except ApiKey.DoesNotExist:
            raise APIException("Invalid API key")

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
        ],
    ),
)
class OrderItemViewSetBase(
    PaginationListMixin,
    mixins.RetrieveModelMixin,
    CustomViewSet,
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


    @grpc_exception
    def retrieve(self, request: Request, pk=None):
        retrieve_response = OrderItemService.retrieve(
            id=pk,
            user=request.user,
        )
        serializer = OrderItemRetrieveSerializer(retrieve_response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def list(self, request: Request, *args, **kwargs):
        list_response = OrderItemService.list(
            statuses=request.query_params.getlist("statuses"),
            user_id=request.query_params.get("user_id"),
            alloff_order_id=request.query_params.get("alloff_order_id"),
            user=request.user,
            **self.get_pagination_params(request),
        )
        serializer = PaginatedOrderItemSerializer(list_response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
