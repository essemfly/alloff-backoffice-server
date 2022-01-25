from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from office.serializers.shipping_notice import (
    PaginatedShippingNoticeSerializer,
    ShippingNoticeSerializer,
    ShippingNoticeStatus,
)
from office.services.shipping_notice import ShippingNoticeService
from rest_framework import mixins, request, response, status, viewsets
from rest_framework.decorators import action


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                "statuses",
                {
                    "type": "array",
                    "items": {"type": "string", "enum": ShippingNoticeStatus.values},
                },
                OpenApiParameter.QUERY,
                explode=True,
            ),
            OpenApiParameter("code", OpenApiTypes.STR, OpenApiParameter.QUERY),
        ],
    ),
)
class ShippingNoticeViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return PaginatedShippingNoticeSerializer
        return ShippingNoticeSerializer

    def list(self, request: request.Request):
        received_items = ShippingNoticeService.list(
            code=request.query_params.get("code"),
            statuses=request.query_params.getlist("statuses"),
        )
        serializer = PaginatedShippingNoticeSerializer(received_items)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, url_path="make-upload-template", methods=["POST"])
    def make_upload_template(self, request: request.Request, pk=None):
        return response.Response({"message": "ok"}, status=status.HTTP_200_OK)

    @action(detail=True, url_path="seal", methods=["POST"])
    def seal(self, request: request.Request, pk=None):
        return response.Response({"message": "ok"}, status=status.HTTP_200_OK)

    @action(detail=True, url_path="package", methods=["POST"])
    def package(self, request: request.Request, pk=None):
        return response.Response({"message": "ok"}, status=status.HTTP_200_OK)
