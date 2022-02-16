from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from product.serializers.brand import (
    BrandSerializer,
    CreateBrandSerializer,
    EditBrandSerializer,
)
from product.serializers.product import EditProductRequestSerializer
from product.services.brand import BrandService

from rest_framework import mixins, response, status, viewsets
from drf_spectacular.utils import extend_schema


class BrandViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.ViewSet,
):
    serializer_class = BrandSerializer

    @extend_schema(responses={status.HTTP_200_OK: BrandSerializer})
    def list(self, request, *args, **kwargs):
        brands = BrandService.list()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CreateBrandSerializer,
        responses={status.HTTP_201_CREATED: BrandSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = BrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_brand = BrandService.create(serializer.message)
        return Response(new_brand, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=EditProductRequestSerializer,
        responses={status.HTTP_200_OK: BrandSerializer},
    )
    def update(self, request, pk, *args, **kwargs):
        serializer = EditBrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = BrandService.edit(serializer.message)
        serializer = BrandSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
