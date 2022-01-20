from rest_framework import viewsets, mixins, response, status

from logistics.serializers.courier import CourierSerializer
from logistics.services.courier import CourierService


class CourierViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        couriers = CourierService.ListProducts()
        print(couriers)
        serializer = CourierSerializer(data=couriers, many=True)
        if not serializer.is_valid(raise_exception=True):
            print("asdfjkfnasfkjnsakjlfnksa;lfmn")
            return ""
        return response.Response(
            data=serializer.initial_data, status=status.HTTP_200_OK
        )
