from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.serializers.brand import BrandSerializer
from product.services.brand import BrandService


class BrandList(APIView):
    def get(self, request, format=None):
        brands = BrandService.list()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)


class BrandDetail(APIView):
    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.data)
