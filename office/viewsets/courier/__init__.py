from office.serializers.courier import CourierSerializer
from office.services.courier import CourierService
from rest_framework import mixins, response, status, viewsets


class CourierViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        couriers = CourierService.list()
        serializer = CourierSerializer(couriers, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
