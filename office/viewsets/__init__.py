from rest_framework import mixins, response, status, viewsets
from rest_framework.request import Request
from rest_framework.decorators import action

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view

from office.serializers.shipping_notice import ShippingNoticeStatus



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
            OpenApiParameter("product_name", OpenApiTypes.STR, OpenApiParameter.QUERY),
        ],
    ),
)
class ShippingNoticeViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        return response.Response({""})
