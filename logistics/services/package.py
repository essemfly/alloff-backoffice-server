from django_grpc_framework import generics

from logistics.models import Package
from logistics.serializers.package import PackageProtoSerializer


class PackageService(generics.ModelService):
    queryset = Package.objects.all()
    serializer_class = PackageProtoSerializer

    def List(self, request, context):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        for message in serializer.message:
            yield message