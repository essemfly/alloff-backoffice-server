from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from office.serializers.inventory import (
    InventorySerializer,
    InventoryStatus,
    PaginatedInventorySerializer,
)
from office.services.inventory import InventoryService
from rest_framework import mixins, response, status, viewsets, request

from drf_spectacular.types import OpenApiTypes


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
)
class InventoryViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return PaginatedInventorySerializer
        return InventorySerializer

    def list(self, request: request.Request):
        print(request.query_params.getlist("statuses"))
        inventories = InventoryService.list(
            code=request.query_params.get("code"),
            product_name=request.query_params.get("product_name"),
            product_brand_name=request.query_params.get("product_brand_name"),
            product_brand_key_name=request.query_params.get("product_brand_key_name"),
            statuses=request.query_params.getlist("statuses"),
        )
        serializer = PaginatedInventorySerializer(inventories)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


# from datetime import datetime

# from django_filters import FilterSet, ChoiceFilter, CharFilter, BaseInFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import viewsets
# from rest_framework.exceptions import APIException
# from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated

# from tagger.models import ShippingNoticeItem
# from tagger.models.inventory import Inventory, InventoryStatus
# from tagger.serializers.inventory import InventorySerializer


# class ChoiceInFilter(BaseInFilter, ChoiceFilter):
#     pass


# class InventoryFilter(FilterSet):
#     location = CharFilter(lookup_expr='icontains')
#     statuses = ChoiceInFilter(field_name='status', choices=InventoryStatus.choices, lookup_expr='in')

#     class Meta:
#         model = Inventory
#         fields = ['location', 'statuses']


# class InventoryViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Inventory.objects.filter(deleted_at__isnull=True).order_by("-id").all()
#     serializer_class = InventorySerializer
#     filter_backends = [SearchFilter, DjangoFilterBackend]
#     search_fields = ['code', 'product_name', 'out_order_id', 'in_order_id', 'product_brand']
#     filterset_class = InventoryFilter

#     def perform_destroy(self, instance: Inventory):
#         if ShippingNoticeItem.objects.filter(inventory=instance).exists():
#             raise APIException("Shipping notice item exists!")
#         instance.deleted_at = datetime.now()
#         instance.product_name = f"[DELETED] {instance.product_name}"
#         instance.save()
