from core.company_auth_viewset import with_company_api
from drf_spectacular.utils import extend_schema
from gen.pyalloff.alloffcategory_pb2 import (
    ListAlloffCategoryRequest,
    ListAlloffCategoryResponse,
)
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from product.serializers.alloff_category import (
    AlloffCategorySerializer,
    ListAlloffCategoryResponseSerializer,
    ListAlloffCateogoryRequestSerializer,
)
from product.services.alloff_category import AlloffCategoryService


class AlloffCategoryViewSet(
    mixins.ListModelMixin,
    viewsets.ViewSet,
):
    serializer_class = AlloffCategorySerializer

    @extend_schema(
        parameters=[ListAlloffCateogoryRequestSerializer],
        responses=ListAlloffCategoryResponseSerializer,
    )
    @with_company_api
    def list(self, request, *args, **kwargs):
        parent_id = request.query_params.get("parent_id", "")

        req = ListAlloffCategoryRequest(parent_id=parent_id)
        res = AlloffCategoryService.list(req)
        serializer = ListAlloffCategoryResponseSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
