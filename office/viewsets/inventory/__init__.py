from office.serializers.courier import CourierSerializer
from office.serializers.inventory import InventorySerializer
from office.services.inventory import InventoryService
from rest_framework import mixins, response, status, viewsets


class InventoryViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        inventories = InventoryService.list()
        serializer = InventorySerializer(data=inventories, many=True)
        serializer.is_valid(raise_exception=True)
        return response.Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )
