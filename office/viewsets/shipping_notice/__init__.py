from office.serializers.shipping_notice import ShippingNoticeSerializer
from office.services.shipping_notice import ShippingNoticeService
from rest_framework import mixins, response, status, viewsets


class ShippingNoticeViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        received_items = ShippingNoticeService.list()
        serializer = ShippingNoticeSerializer(received_items, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
