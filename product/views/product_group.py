from django.http import Http404
from html5lib import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.serializers.product_group import ProductGroupSerializer
from product.services.product_group import ProductGroupService
from protos.product.productGroup_pb2 import (
    GetProductGroupRequest,
    ListProductGroupsRequest,
)


class ProductGroupList(APIView):
    def get(self, request, format=None):
        pgs = ProductGroupService.list()
        serializer = ProductGroupSerializer(pgs, many=True)
        return Response(serializer.data)


class ProductGroupDetail(APIView):
    def get(self, request, pg_id, format=None):
        req = GetProductGroupRequest(product_group_id=pg_id)
        pg = ProductGroupService.get(req)
        serializer = ProductGroupSerializer(pg)
        return Response(serializer.data)

    def post(self, request, format=None):
        pg = ProductGroupService.create(request)
        serializer = ProductGroupSerializer(pg)
        return Response(serializer.data)

    def push_products(self, request, pk, format=None):
        pg = ProductGroupService.push(request)
        serializer = ProductGroupSerializer(pg)
        return Response(serializer.data)
