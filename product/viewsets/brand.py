from typing import List, Optional

from core.company_auth_viewset import with_company_api
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from office.models.company import CompanyStatus
from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from product.serializers.brand import (BrandSerializer, CreateBrandSerializer,
                                       EditBrandSerializer)
from product.serializers.product import EditProductRequestApiSerializer
from product.services.brand import BrandService


def get_usable_brand_keynames(user: User) -> Optional[List[str]]:
    if user.profile.is_admin:
        # Catch None and do not filter
        return None
    elif user.profile.company.status != CompanyStatus.ACTIVE:
        raise PermissionDenied("User is not in an active company.")
    return [brand.keyname for brand in user.profile.company.company_brands.all()]


class BrandViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.ViewSet,
):
    serializer_class = BrandSerializer

    @extend_schema(responses={status.HTTP_200_OK: BrandSerializer})
    @with_company_api
    def list(self, request, *args, **kwargs):
        brands = BrandService.list()
        keynames = get_usable_brand_keynames(request.user)
        if keynames is not None:
            brands = [brand for brand in brands if brand.keyname in keynames]
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
        request=EditProductRequestApiSerializer,
        responses={status.HTTP_200_OK: BrandSerializer},
    )
    def update(self, request, pk, *args, **kwargs):
        serializer = EditBrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = BrandService.edit(serializer.message)
        serializer = BrandSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
