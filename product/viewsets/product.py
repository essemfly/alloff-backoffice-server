from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from product.serializers.product import (
    CreateProductRequestSerializer,
    EditProductRequestSerializer,
    ListProductResultSerializer,
    ListProductSerializer,
    ProductSerializer,
)
from product.services.product import ProductService
from protos.product.product_pb2 import (
    GetProductRequest,
    ListProductsRequest,
    ProductQuery,
)


from rest_framework import mixins, status, viewsets


class ProductViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    viewsets.ViewSet,
):
    serializer_class = ProductSerializer

    @extend_schema(
        request=ListProductSerializer,
        responses={status.HTTP_200_OK: ListProductResultSerializer},
    )
    def list(self, request, *args, **kwargs):
        offset = request.query_params.get("offset", 0)
        limit = request.query_params.get("limit", 100)
        search_query = request.query_params.get("query", "")
        brand_id = request.query_params.get("brand_id", "")
        category_id = request.query_params.get("category_id", "")
        alloff_category_id = request.query_params.get("alloff_category_id", "")

        query: ProductQuery = ProductQuery(
            search_query=search_query,
            brand_id=brand_id,
            category_id=category_id,
            alloff_category_id=alloff_category_id,
        )
        req: ListProductsRequest = ListProductsRequest(
            offset=int(offset), limit=int(limit), query=query
        )

        res = ProductService.list(req)
        serializer = ProductSerializer(res.products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        req = GetProductRequest(alloff_product_id=pk)
        pd = ProductService.get(req)
        serializer = ProductSerializer(pd)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CreateProductRequestSerializer,
        responses={status.HTTP_201_CREATED: ProductSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = CreateProductRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ProductService.create(serializer.message)
        serializer = ProductSerializer(res)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=EditProductRequestSerializer,
        responses={status.HTTP_200_OK: ProductSerializer},
    )
    def update(self, request, pk, *args, **kwargs):
        serializer = EditProductRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ProductService.edit(serializer.message)
        serializer = ProductSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
