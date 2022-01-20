from office.serializers.package import PackageSerializer
from office.services.package import PackageService
from rest_framework import mixins, response, status, viewsets


class PackageViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        packages = PackageService.list()
        serializer = PackageSerializer(packages, many=True)
        return response.Response(
            data=serializer.data, status=status.HTTP_200_OK
        )
