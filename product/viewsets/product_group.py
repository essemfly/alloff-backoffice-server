from tokenize import group
from drf_spectacular.utils import extend_schema
from jmespath import search
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from alloff_backoffice_server.settings import PAGE_SIZE
from product.serializers.product_group import (
    EditProductGroupSerializer,
    ListProductGroupRequestSerializer,
    ListProductGroupResponseSerializer,
    ProductGroupSerializer,
    PushProductsSerializer,
    CreateProductGroupSeriazlier,
    RemoveProductInProductGroupSerializer,
)
from product.services.product_group import ProductGroupService
from protos.product.productGroup_pb2 import (
    GetProductGroupRequest,
    ListProductGroupsRequest,
    ProductGroupQuery,
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

    @extend_schema(
        parameters=[ListProductGroupRequestSerializer],
        request=ListProductGroupRequestSerializer,
        responses={status.HTTP_200_OK: ListProductGroupResponseSerializer},
    )
    def list(self, request, *args, **kwargs):
        offset = request.query_params.get("offset", 0)
        limit = request.query_params.get("limit", PAGE_SIZE)
        search_query = request.query_params.get("search_query", "")
        group_type = request.query_params.get("group_type", "")

        query = query = ProductGroupQuery(search_query=search_query)
        if group_type != "" and search_query != "":
            query = ProductGroupQuery(
                search_query=search_query, group_type=group_type
            )
        elif group_type != "" and search_query == "":
            query = ProductGroupQuery(group_type=group_type)

        req = ListProductGroupsRequest(
            offset=int(offset), limit=int(limit), query=query
        )
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
        request=EditProductGroupSerializer,
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

    @extend_schema(
        request=RemoveProductInProductGroupSerializer,
        responses={status.HTTP_200_OK: ProductGroupSerializer},
    )
    @action(detail=True, methods=["POST"])
    def remove_product(self, request, *args, **kwargs):
        serializer = RemoveProductInProductGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ProductGroupService.remove(serializer.message)
        serializer = ProductGroupSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
