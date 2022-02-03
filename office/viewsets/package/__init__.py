from office.serializers.package import PackageSerializer
from rest_framework import response, status, viewsets, fields, request
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, inline_serializer
from drf_spectacular.openapi import OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from office.services.package import PackageService

from office.viewsets.shipping_notice import print_package_labels


class PackageViewSet(viewsets.ViewSet):
    serializer_class = PackageSerializer

    @extend_schema(
        request=None,
        responses=inline_serializer(
            "ReprintLabelResponse", {"message": fields.CharField()}
        ),
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["post"])
    def reprint_label(self, request: request.Request, pk=None):
        service = PackageService()
        package = service.retrieve(int(pk))
        print_package_labels(package)
        return response.Response({"message": "ok"}, status=status.HTTP_200_OK)

    # def list(self, request, *args, **kwargs):
    #     packages = PackageService.list()
    #     serializer = PackageSerializer(packages, many=True)
    #     return response.Response(
    #         data=serializer.data, status=status.HTTP_200_OK
    #     )
