from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.serializers.product import ProductSerializer
from product.services.product import ProductService


class ProductList(APIView):
    def get(self, request, format=None):
        pds = ProductService.list()
        serializer = ProductSerializer(pds, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, pk, format=None):
        pd = ProductService.get(request)
        serializer = ProductSerializer(pd)
        return Response(serializer.data)

    def post(self, request, format=None):
        pd = ProductService.create(request)
        serializer = ProductSerializer(pd)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pd = ProductService.edit(request)
        serializer = ProductSerializer(pd)
        return Response(serializer.data)

    def putSpecial(self, request, pk, format=None):
        pd = ProductService.putSpecial(request)
        serializer = ProductSerializer(pd)
        return Response(serializer.data)
