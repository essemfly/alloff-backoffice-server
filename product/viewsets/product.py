from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from product.serializers.product import (
    CreateProductRequestSerializer,
    EditProductRequestSerializer,
    ProductSerializer,
    ListProductSerializer,
)
from product.services.product import ProductService
from protos.product.product_pb2 import (
    CreateProductRequest,
    EditProductRequest,
    GetProductRequest,
    GetProductResponse,
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
            offset=offset, limit=limit, query=query
        )

        res = ProductService.list(req)
        serializer = ProductSerializer(res.products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        product_id = request.query_params.get("id")
        req = GetProductRequest(alloff_product_id=product_id)
        pd = ProductService.get(req)
        serializer = ProductSerializer(pd)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = CreateProductRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ProductService.create(serializer.message)
        serializer = ProductSerializer(res)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, alloff_product_id, *args, **kwargs):
        serializer = EditProductRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = ProductService.edit(serializer.message)
        serializer = ProductSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
