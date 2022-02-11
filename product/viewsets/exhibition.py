from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, status, viewsets

from product.serializers.exhibition import (
    CreateExhibitionSerializer,
    EditExhibitionSerializer,
    ExhibitionSerializer,
    ListExhibitionRequestSerializer,
    ListExhibitionsResponseSerializer,
)
from product.services.exhibition import ExhibitionService
from protos.product.exhibition_pb2 import (
    CreateExhibitionResponse,
    EditExhibitionResponse,
    GetExhibitionRequest,
    ListExhibitionsRequest,
    ListExhibitionsResponse,
)


class ExhibitionViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.ViewSet,
):
    serializer_class = ExhibitionSerializer

    @extend_schema(
        parameters=[ListExhibitionRequestSerializer],
        request=ListExhibitionRequestSerializer,
        responses={status.HTTP_200_OK: ListExhibitionsResponse},
    )
    def list(self, request, *args, **kwargs):
        offset = request.query_params.get("offset", 0)
        limit = request.query_params.get("limit", 1000)

        req = ListExhibitionsRequest(offset=int(offset), limit=int(limit))
        res = ExhibitionService.list(req)
        serializer = ListExhibitionsResponseSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        req = GetExhibitionRequest(exhibition_id=pk)
        res = ExhibitionService.get(req)
        serializer = ExhibitionSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CreateExhibitionSerializer,
        responses={status.HTTP_200_OK: CreateExhibitionResponse},
    )
    def create(self, request, *args, **kwargs):
        serializer = CreateExhibitionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ExhibitionService.create(serializer.message)
        serializer = ExhibitionSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=EditExhibitionSerializer,
        responses={status.HTTP_200_OK: EditExhibitionResponse},
    )
    def update(self, request, pk, *args, **kwargs):
        serializer = EditExhibitionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ExhibitionService.edit(serializer.message)
        serializer = ExhibitionSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
