from django_filters import FilterSet, ChoiceFilter, CharFilter, BaseInFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from tagger.models.inventory import Inventory, InventoryStatus
from tagger.serializers.inventory import InventorySerializer


class ChoiceInFilter(BaseInFilter, ChoiceFilter):
    pass


class InventoryFilter(FilterSet):
    location = CharFilter(lookup_expr='icontains')
    statuses = ChoiceInFilter(field_name='status', choices=InventoryStatus.choices, lookup_expr='in')

    class Meta:
        model = Inventory
        fields = ['location', 'statuses']


class InventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.order_by("-id").all()
    serializer_class = InventorySerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['code', 'product_name', 'out_order_id', 'in_order_id']
    filterset_class = InventoryFilter
