from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from tagger.models import Package
from tagger.serializers.shipping import PackageSerializer
from tagger.viewsets.shipping_notice import seal_package


class PackageViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Package.objects.order_by("-id").all()
    serializer_class = PackageSerializer

    @extend_schema(
        request=None,
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, url_path="reprint", methods=["POST"])
    def reprint(self, request: Request, pk=None):
        return Response(self.get_serializer(seal_package(self.get_object())).data, status=status.HTTP_200_OK)
