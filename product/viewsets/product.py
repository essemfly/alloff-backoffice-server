from alloff_backoffice_server.settings import PAGE_SIZE
from bs4 import BeautifulSoup
from core.company_auth_viewset import with_company_api
from drf_spectacular.utils import extend_schema
from office.models.html_product_info import HtmlProductInfo
from protos.product.product_pb2 import (GetProductRequest, ListProductsRequest,
                                        ProductQuery)
from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from product.helpers.get_module_name import get_module_name
from product.serializers.product import (CreateProductRequestApiSerializer,
                                         CreateProductRequestGrpcSerializer,
                                         EditProductRequestApiSerializer,
                                         EditProductRequestGrpcSerializer,
                                         ListProductResultSerializer,
                                         ListProductSerializer,
                                         ProductSerializer)
from product.services.product import ProductService


def separate_html_from_request(request):
    raw_html = request.data.get("raw_html")
    if raw_html is not None:
        del request.data["raw_html"]
    return raw_html, request


def parse_html(raw_html):
    soup = BeautifulSoup(raw_html)
    text_nodes = [
        t for x in soup.find_all(text=True) if (t := " ".join(x.split())) != ""
    ]
    images = [x["src"] for x in soup.find_all("img")]
    return text_nodes, images

def populate_grpc_request():
    pass


class ProductViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    viewsets.ViewSet,
):
    serializer_class = ProductSerializer

    @extend_schema(
        parameters=[
            ListProductSerializer,
        ],
        responses={status.HTTP_200_OK: ListProductResultSerializer},
    )
    @with_company_api
    def list(self, request, *args, **kwargs):
        offset = request.query_params.get("offset", 0)
        limit = request.query_params.get("limit", PAGE_SIZE)
        search_query = request.query_params.get("search_query", "")
        brand_id = request.query_params.get("brand_id", "")
        category_id = request.query_params.get("category_id", "")
        alloff_category_id = request.query_params.get("alloff_category_id", "")

        module_name = get_module_name(request)

        query: ProductQuery = ProductQuery(
            search_query=search_query,
            brand_id=brand_id,
            category_id=category_id,
            alloff_category_id=alloff_category_id,
        )
        req: ListProductsRequest = ListProductsRequest(
            offset=int(offset),
            limit=int(limit),
            query=query,
            module_name=module_name,
        )

        res = ProductService.list(req)
        serializer = ListProductResultSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @with_company_api
    def retrieve(self, request, pk, *args, **kwargs):
        module_name = get_module_name(request)
        # For authorization purposes, restrict access to non-admin users if module name does not match.
        req = GetProductRequest(alloff_product_id=pk)
        pd = ProductService.get(req)
        serializer = ProductSerializer(pd)
        if module_name != "" and serializer.data.get("module_name") != module_name:
            # Raise a 404.
            raise NotFound("Product not found.")

        raw_html = ""
        try:
            raw_html = HtmlProductInfo.objects.get(
                product_id=pd.alloff_product_id
            ).raw_html
        except HtmlProductInfo.DoesNotExist:
            pass
        return Response(
            {**serializer.data, "raw_html": raw_html}, status=status.HTTP_200_OK
        )

    @extend_schema(
        request=CreateProductRequestApiSerializer,
        responses={status.HTTP_201_CREATED: ProductSerializer},
    )
    @with_company_api
    def create(self, request, *args, **kwargs):
        module_name = get_module_name(request)
        raw_html, request = separate_html_from_request(request)

        request_serializer = CreateProductRequestGrpcSerializer(
            data={**request.data, "module_name": module_name}
        )
        request_serializer.is_valid(raise_exception=True)

        res = ProductService.create(request_serializer.message)
        result_serializer = ProductSerializer(res)

        HtmlProductInfo.objects.create(res.id, raw_html)

        return Response(result_serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=EditProductRequestApiSerializer,
        responses={status.HTTP_200_OK: ProductSerializer},
    )
    @with_company_api
    def update(self, request, pk, *args, **kwargs):
        module_name = get_module_name(request)
        raw_html, request = separate_html_from_request(request)

        request_serializer = EditProductRequestGrpcSerializer(
            data={**request.data, "module_name": module_name}
        )
        request_serializer.is_valid(raise_exception=True)

        res = ProductService.edit(request_serializer.message)
        result_serializer = ProductSerializer(res)

        HtmlProductInfo.objects.update_or_create(
            product_id=pk, defaults={"raw_html": raw_html}
        )

        return Response(result_serializer.data, status=status.HTTP_200_OK)
