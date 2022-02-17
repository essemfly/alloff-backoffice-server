from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, status, viewsets

from alloff_backoffice_server.settings import PAGE_SIZE

from product.serializers.top_banner import (
    CreateTopBannerSerializer,
    EditTopBannerSerializer,
    TopBannerSerializer,
    ListTopBannerRequestSerializer,
    ListTopBannerResponseSerializer,
)

from product.services.top_banner import TopBannerService

from protos.product.topbanner_pb2 import (
    ListTopBannersRequest,
)

from protos.product.exhibition_pb2 import (
    CreateExhibitionResponse,
    EditExhibitionResponse,
    GetExhibitionRequest,
)


class TopBannerViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.ViewSet,
):
    serializer_class = TopBannerSerializer

    @extend_schema(
        parameters=[ListTopBannerRequestSerializer],
        request=ListTopBannerRequestSerializer,
        responses={status.HTTP_200_OK: ListTopBannerResponseSerializer},
    )
    def list(self, request, *args, **kwargs):
        offset = request.query_params.get("offset", 0)
        limit = request.query_params.get("limit", PAGE_SIZE)

        req = ListTopBannersRequest(offset=int(offset), limit=int(limit))
        res = TopBannerService.list(req)
        serializer = ListTopBannerResponseSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        req = GetExhibitionRequest(exhibition_id=pk)
        res = TopBannerService.get(req)
        serializer = TopBannerSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CreateTopBannerSerializer,
        responses={status.HTTP_200_OK: CreateExhibitionResponse},
    )
    def create(self, request, *args, **kwargs):
        serializer = CreateTopBannerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = TopBannerService.create(serializer.message)
        serializer = TopBannerSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=EditTopBannerSerializer,
        responses={status.HTTP_200_OK: EditExhibitionResponse},
    )
    def update(self, request, pk, *args, **kwargs):
        serializer = EditTopBannerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = TopBannerService.edit(serializer.message)
        serializer = TopBannerSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
