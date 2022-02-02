from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from office.label.print_label import print_label
from office.label.receiving_label import make_receiving_label
from office.serializers.received_item import (
    PaginatedReceivedItemSerializer,
    ReceivedItemSerializer,
    ReceivedItemStatus,
)
from office.services.received_item import ReceivedItemService
from rest_framework import response, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from office.utils.openapi import PROTO_PAGINATION_QUERY_PARAMS
from rest_framework.exceptions import APIException

from office.viewsets.pagination import PaginationListMixin


@extend_schema_view(
    list=extend_schema(
        responses={status.HTTP_200_OK: PaginatedReceivedItemSerializer},
        parameters=PROTO_PAGINATION_QUERY_PARAMS
        + [
            OpenApiParameter(
                "statuses",
                {
                    "type": "array",
                    "items": {"type": "string", "enum": ReceivedItemStatus.values},
                },
                OpenApiParameter.QUERY,
                explode=True,
            ),
        ],
    ),
    receive_inventory=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)]
    ),
    cancel_receiving=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)]
    ),
    revert_inventory=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)]
    ),
)
class ReceivedItemViewSet(PaginationListMixin, viewsets.ViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return PaginatedReceivedItemSerializer
        if self.action in ["receive_inventory", "revert_inventory", "cancel_receiving"]:
            return None
        return ReceivedItemSerializer

    def list(self, request: Request, *args, **kwargs):
        list_response = ReceivedItemService.list(
            size=int(request.query_params.get("size")),
            page=int(request.query_params.get("page")),
            search=request.query_params.get("search"),
            statuses=request.query_params.getlist("statuses"),
        )
        serializer = PaginatedReceivedItemSerializer(list_response)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["POST"])
    def receive_inventory(self, request: Request, pk=None):
        received_item = ReceivedItemService.receive(int(pk), user=request.user)
        if received_item.inventory is None:
            raise APIException("Received item has no inventory.")
        serializer = ReceivedItemSerializer(received_item)
        print_label(make_receiving_label(received_item))
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["POST"])
    def cancel_receiving(self, request: Request, pk=None):
        received_item = ReceivedItemService.cancel(int(pk), user=request.user)
        serializer = ReceivedItemSerializer(received_item)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["POST"])
    def revert_inventory(self, request: Request, pk=None):
        received_item = ReceivedItemService.revert(int(pk), user=request.user)
        serializer = ReceivedItemSerializer(received_item)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
