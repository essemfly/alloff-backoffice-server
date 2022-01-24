from office.serializers.received_item import ReceivedItemSerializer
from office.services.received_item import ReceivedItemService
from rest_framework import mixins, response, status, viewsets


class ReceivedItemViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        received_items = ReceivedItemService.list()
        serializer = ReceivedItemSerializer(received_items, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
