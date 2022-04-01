from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, status, viewsets

from alloff_backoffice_server.settings import PAGE_SIZE
from product.services.hometab import HometabService, HomeTabItemStub
from product.serializers.hometab import (
    CreateHomeTabSerializer,
    EditHomeTabSerializer,
    HomeTabSerializer,
    ListHomeTabsRequestSerializer,
    ListHomeTabsResponseSerializer,
)
from gen.python.protos.hometab_pb2 import (
    GetHomeTabItemRequest,
    ListHomeTabItemsRequest,
)


class HometabItemViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.ViewSet,
):
    serializer_class = HomeTabSerializer

    @extend_schema(
        parameters=[ListHomeTabsRequestSerializer],
        request=ListHomeTabsRequestSerializer,
        responses={status.HTTP_200_OK: ListHomeTabsResponseSerializer},
    )
    def list(self, request, *args, **kwargs):
        offset = request.query_params.get("offset", 0)
        limit = request.query_params.get("limit", PAGE_SIZE)

        req = ListHomeTabItemsRequest(offset=int(offset), limit=int(limit))
        res = HometabService.list(req)
        serializer = ListHomeTabsResponseSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        req = GetHomeTabItemRequest(item_id=pk)
        res = HometabService.get(req)
        serializer = HomeTabSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CreateHomeTabSerializer,
        responses={status.HTTP_200_OK: HomeTabSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = CreateHomeTabSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = HometabService.create(serializer.message)
        serializer = HomeTabSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=EditHomeTabSerializer,
        responses={status.HTTP_200_OK: HomeTabSerializer},
    )
    def update(self, request, pk, *args, **kwargs):
        serializer = EditHomeTabSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = HometabService.edit(serializer.message)
        serializer = HomeTabSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
