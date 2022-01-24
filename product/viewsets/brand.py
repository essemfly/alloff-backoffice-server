from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.serializers.brand import BrandSerializer
from product.services.brand import BrandService

from office.serializers.inventory import InventorySerializer
from office.services.inventory import InventoryService
from rest_framework import mixins, response, status, viewsets

# from logistics.models import Inventory
from drf_spectacular.utils import extend_schema


class BrandViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.ViewSet):
    serializer_class = BrandSerializer

    def list(self, request, *args, **kwargs):
        brands = BrandService.list()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            new_brand = BrandService.create(serializer.message)
            return Response(new_brand, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
