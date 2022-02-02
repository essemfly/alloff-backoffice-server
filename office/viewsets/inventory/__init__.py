from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from office.serializers.inventory import (
    InventorySerializer,
    InventoryStatus,
    PaginatedInventorySerializer,
)
from office.services.inventory import InventoryService
from rest_framework import mixins, response, status, viewsets, request

from drf_spectacular.types import OpenApiTypes
from rest_framework.exceptions import APIException


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                "statuses",
                {
                    "type": "array",
                    "items": {"type": "string", "enum": InventoryStatus.values},
                },
                OpenApiParameter.QUERY,
                explode=True,
            ),
            OpenApiParameter("code", OpenApiTypes.STR, OpenApiParameter.QUERY),
            OpenApiParameter("product_name", OpenApiTypes.STR, OpenApiParameter.QUERY),
            OpenApiParameter(
                "product_brand_name", OpenApiTypes.STR, OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                "product_brand_key_name", OpenApiTypes.STR, OpenApiParameter.QUERY
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
        inventories = InventoryService.list(
            code=request.query_params.get("code"),
            product_name=request.query_params.get("product_name"),
            product_brand_name=request.query_params.get("product_brand_name"),
            product_brand_key_name=request.query_params.get("product_brand_key_name"),
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
