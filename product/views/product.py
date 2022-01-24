from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.serializers.product import ListProductSerializer, ProductSerializer
from product.services.product import ProductService
from protos.product.product_pb2 import (
    CreateProductRequest,
    EditProductRequest,
    GetProductRequest,
    GetProductResponse,
    ListProductsRequest,
    ProductQuery,
)


class ProductList(APIView):
    def get(self, request, format=None):
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
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, product_id, format=None):
        req = GetProductRequest(alloff_product_id=product_id)
        pd = ProductService.get(req)
        serializer = ProductSerializer(pd)
        return Response(serializer.data)

    # (TODO) Make serializer -> request
    def post(self, request, format=None):
        req = CreateProductRequest()
        pd = ProductService.create(req)
        serializer = ProductSerializer(pd)
        return Response(serializer.data)

    # (TODO) Make serializer -> request
    def put(self, request, product_id, format=None):
        req = EditProductRequest(alloff_product_id=product_id)
        serializer = ProductSerializer(req)
        return Response(serializer.data)

    # (TODO) Make serializer -> request
    def putSpecial(self, request, pk, format=None):
        pd = ProductService.putSpecial(request)
        serializer = ProductSerializer(pd)
        return Response(serializer.data)
