from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, status, viewsets

from alloff_backoffice_server.settings import PAGE_SIZE

from product.serializers.alloff_category import (
    AlloffCategorySerializer,
    ListAlloffCategoryResponseSerializer,
)

from product.services.alloff_category import AlloffCategoryService
from protos.product.alloffcategory_pb2 import (
    ListAlloffCategoryRequest,
    ListAlloffCategoryResponse,
)


class AlloffCategoryViewSet(
    mixins.ListModelMixin,
    viewsets.ViewSet,
):
    serializer_class = AlloffCategorySerializer

    @extend_schema(
        parameters=[ListAlloffCategoryRequest],
        request=ListAlloffCategoryRequest,
        responses={status.HTTP_200_OK: ListAlloffCategoryResponse},
    )
    def list(self, request, *args, **kwargs):
        parent_id = request.query_params.get("parent_id", "")

        req = ListAlloffCategoryRequest(parent_id=parent_id)
        res = AlloffCategoryService.list(req)
        serializer = ListAlloffCategoryResponseSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
