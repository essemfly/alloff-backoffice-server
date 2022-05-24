from typing import List, Optional

from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from product.serializers.alloff_size import (
    AlloffSizeSerializer,
    ListAlloffSizeRequestSerializer,
    ListAlloffSizeReponseSerializer,
    ListAlloffSizeRequest,
    EditAlloffSizeSerializer,
    CreateAlloffSizeSerializer,
)
from product.services.alloff_size import AlloffSizeService
from gen.pyalloff.alloff_size_pb2 import (
    GetAlloffSizeRequest
)


class AlloffSizeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.ViewSet
):
    serializer_class = AlloffSizeSerializer

    @extend_schema(
        request=ListAlloffSizeRequestSerializer,
        responses=ListAlloffSizeReponseSerializer
    )
    def list(self, request, *args, **kwargs):
        req = ListAlloffSizeRequest()
        res = AlloffSizeService.list(req)
        serializer = ListAlloffSizeReponseSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CreateAlloffSizeSerializer,
        responses={status.HTTP_201_CREATED: AlloffSizeSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = CreateAlloffSizeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = AlloffSizeService.create(serializer.message)
        serializer = AlloffSizeSerializer(res)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=EditAlloffSizeSerializer,
        responses={status.HTTP_200_OK: AlloffSizeSerializer}
    )
    def update(self, request, pk, *args, **kwargs):
        serializer = EditAlloffSizeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = AlloffSizeService.edit(serializer.message)
        serializer = AlloffSizeSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        req = GetAlloffSizeRequest(alloff_size_id=pk)
        res = AlloffSizeService.get(req)
        serializer = AlloffSizeSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)