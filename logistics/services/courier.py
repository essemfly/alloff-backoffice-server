from django_grpc_framework import generics

from logistics.models import Courier
from logistics.serializers.courier import CourierProtoSerializer


class CourierService(generics.ModelService):
    queryset = Courier.objects.all()
    serializer_class = CourierProtoSerializer
