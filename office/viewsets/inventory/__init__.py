from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import mixins, response, status, viewsets, request
from rest_framework.exceptions import APIException

from alloff_backoffice_server.settings import PAGE_SIZE
from office.serializers.inventory import (
    InventorySerializer,
    InventoryStatus,
    PaginatedInventorySerializer,
)
from office.services.inventory import InventoryService
from office.utils.openapi import PROTO_PAGINATION_QUERY_PARAMS


@extend_schema_view(
    list=extend_schema(
        parameters=PROTO_PAGINATION_QUERY_PARAMS
        + [
            OpenApiParameter(
                "statuses",
                {
                    "type": "array",
                    "items": {"type": "string", "enum": InventoryStatus.values},
                },
                OpenApiParameter.QUERY,
                explode=True,
            ),
        ],
    ),
    destroy=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)]
    ),
)
class InventoryViewSet(
    mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.ViewSet
):
    def get_serializer_class(self):
        if self.action == "list":
            return PaginatedInventorySerializer
        return InventorySerializer

    def list(self, request: request.Request):
        page = request.query_params.get("page", 1)
        size = request.query_params.get("size", PAGE_SIZE)

        inventories = InventoryService.list(
            page=int(page),
            size=int(size),
            search=request.query_params.get("search"),
            statuses=request.query_params.getlist("statuses"),
        )
        serializer = PaginatedInventorySerializer(inventories)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request: request.Request, pk=None):
        try:
            InventoryService.delete(int(pk))
            return response.Response(data={"message": ""}, status=status.HTTP_200_OK)
        except Exception as e:
            raise APIException(str(e.details()))
