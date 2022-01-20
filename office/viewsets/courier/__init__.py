from office.serializers.courier import CourierSerializer
from office.services.courier import CourierService
from rest_framework import mixins, response, status, viewsets


class CourierViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        couriers = CourierService.list()
        serializer = CourierSerializer(data=couriers, many=True)
        serializer.is_valid(raise_exception=True)
        return response.Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )
