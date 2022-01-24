from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from product.serializers.product_group import ProductGroupSerializer
from product.services.product_group import ProductGroupService
from protos.product.productGroup_pb2 import (
    GetProductGroupRequest,
    ListProductGroupsRequest,
)
from rest_framework import mixins, status, viewsets


class ProductGroupViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.ViewSet,
):
    serializer_class = ProductGroupSerializer

    def list(self, request, *args, **kwargs):
        pgs = ProductGroupService.list()
        serializer = ProductGroupSerializer(pgs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        pg_id = request.query_params.get("id")
        req = GetProductGroupRequest(product_group_id=pg_id)
        pg = ProductGroupService.get(req)
        serializer = ProductGroupSerializer(pg)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # (TODO)
    def create(self, request, *args, **kwargs):
        pg = ProductGroupService.create(request)
        serializer = ProductGroupSerializer(pg)
        return Response(status=status.HTTP_201_CREATED)

    # (TODO)
    @action(detail=True, methods=["post"])
    def push_products(self, request, *args, **kwargs):
        pg = ProductGroupService.push(request)
        serializer = ProductGroupSerializer(pg)
        return Response(serializer.data, status=status.HTTP_200_OK)
