from datetime import datetime

from django_filters import FilterSet, ChoiceFilter, CharFilter, BaseInFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, response, status
from rest_framework.exceptions import APIException
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from office.serializers.courier import CourierSerializer
from office.services.courier import CourierService
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


class CourierViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]
    # queryset = Inventory.objects.filter(deleted_at__isnull=True).order_by("-id").all()
    # serializer_class = InventorySerializer
    # filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = ['code', 'product_name', 'out_order_id', 'in_order_id', 'product_brand']
    # filterset_class = InventoryFilter

    # def perform_destroy(self, instance: Inventory):
    #     if ShippingNoticeItem.objects.filter(inventory=instance).exists():
    #         raise APIException("Shipping notice item exists!")
    #     instance.deleted_at = datetime.now()
    #     instance.product_name = f"[DELETED] {instance.product_name}"
    #     instance.save()

    def list(self, request, *args, **kwargs):
        couriers = CourierService.list()
        print(couriers)
        serializer = CourierSerializer(data=couriers, many=True)
        if not serializer.is_valid(raise_exception=True):
            print("asdfjkfnasfkjnsakjlfnksa;lfmn")
            return ""
        return response.Response(
            data=serializer.initial_data, status=status.HTTP_200_OK
        )
