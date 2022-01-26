from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from product.serializers.product import EditProductRequestSerializer
from product.serializers.product_group import (
    EditProductGroupSerializer,
    ProductGroupSerializer,
    PushProductsSerializer,
    CreateProductGroupSeriazlier,
)
from product.services.product_group import ProductGroupService
from protos.product.productGroup_pb2 import (
    GetProductGroupRequest,
)
from rest_framework import mixins, status, viewsets


class ProductGroupViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.ViewSet,
):
    serializer_class = ProductGroupSerializer

    def list(self, request, *args, **kwargs):
        pgs = ProductGroupService.list()
        serializer = ProductGroupSerializer(pgs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        req = GetProductGroupRequest(product_group_id=pk)
        pg = ProductGroupService.get(req)
        serializer = ProductGroupSerializer(pg)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CreateProductGroupSeriazlier,
        responses={status.HTTP_201_CREATED: ProductGroupSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = CreateProductGroupSeriazlier(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ProductGroupService.create(serializer.message)
        serializer = ProductGroupSerializer(res)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=EditProductRequestSerializer,
        responses={status.HTTP_200_OK: ProductGroupSerializer},
    )
    def update(self, request, *args, **kwargs):
        serializer = EditProductGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ProductGroupService.edit(serializer.message)
        serializer = ProductGroupSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=PushProductsSerializer,
        responses={status.HTTP_200_OK: ProductGroupSerializer},
    )
    @action(detail=True, methods=["POST"])
    def push_products(self, request, *args, **kwargs):
        serializer = PushProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ProductGroupService.push(serializer.message)
        serializer = ProductGroupSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
