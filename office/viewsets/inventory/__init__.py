from office.serializers.courier import CourierSerializer
from office.serializers.inventory import InventorySerializer
from office.services.inventory import InventoryService
from rest_framework import mixins, response, status, viewsets


class InventoryViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        inventories = InventoryService.list()
        serializer = InventorySerializer(inventories, many=True)
        return response.Response(
            data=serializer.data, status=status.HTTP_200_OK
        )
