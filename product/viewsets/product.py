from alloff_backoffice_server.settings import PAGE_SIZE
from bs4 import BeautifulSoup
from core.company_auth_viewset import with_company_api
from core.download_image_to_s3 import download_image_to_s3
from drf_spectacular.utils import extend_schema
from functions.product.cache_image import check_and_download_images_to_s3
from functions.product.thumbnail import check_and_make_thumbnail
from gen.pyalloff.product_pb2 import (GetProductRequest, ListProductsRequest,
                                      ProductQuery)
from office.models.html_product_info import HtmlProductInfo
from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import APIException, NotFound
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
        is_classified_done = request.query_params.get("is_classified_done", None)

        if is_classified_done is not None:
            is_classified_done = is_classified_done == "true"

        module_name = get_module_name(request)

        if is_classified_done is None:
            query: ProductQuery = ProductQuery(
                search_query=search_query,
                brand_id=brand_id,
                category_id=category_id,
                alloff_category_id=alloff_category_id,
            )
        else:
            query: ProductQuery = ProductQuery(
                search_query=search_query,
                brand_id=brand_id,
                category_id=category_id,
                alloff_category_id=alloff_category_id,
                is_classified_done=is_classified_done,
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
        return Response(
            _upsert_product(request, is_update=False), status=status.HTTP_201_CREATED
        )

    @extend_schema(
        request=EditProductRequestApiSerializer,
        responses={status.HTTP_200_OK: ProductSerializer},
    )
    @with_company_api
    def update(self, request, pk, *args, **kwargs):
        return Response(
            _upsert_product(request, is_update=True, pk=pk), status=status.HTTP_200_OK
        )


def _upsert_product(request, is_update: bool = None, pk=None):
    if is_update is None:
        raise APIException("is_update should be explicitly set.")
    if is_update and pk is None:
        raise APIException("pk should be explicitly set when is_update is True.")

    RequestSerializer = (
        CreateProductRequestGrpcSerializer
        if not is_update
        else EditProductRequestGrpcSerializer
    )
    grpc_call = ProductService.create if not is_update else ProductService.edit

    data, raw_html = _make_grpc_request_data(request, pk)
    image_downloaded_data = check_and_download_images_to_s3(data)
    thumbnail_processed_data = check_and_make_thumbnail(image_downloaded_data)
    request_serializer = RequestSerializer(data=thumbnail_processed_data)
    request_serializer.is_valid(raise_exception=True)

    res = grpc_call(request_serializer.message)
    result_serializer = ProductSerializer(res)

    if raw_html is not None and raw_html != "":
        if is_update:
            HtmlProductInfo.objects.update_or_create(
                product_id=pk, defaults={"raw_html": raw_html}
            )
        else:
            HtmlProductInfo.objects.create(
                product_id=res.alloff_product_id, raw_html=raw_html
            )
    return result_serializer.data


def _make_grpc_request_data(request, alloff_product_id=None):
    """
    Convert request data to grpc request data.
    1. Gets module_name for authorization purposes.
    2. Gets raw_html from request for company API spec purposes.
    3. Parses raw_html to get text_nodes and images.
    4. Returns grpc request data and raw_html for saving.
    """
    module_name = get_module_name(request)
    raw_html, new_request = _separate_html_from_request(request)
    data = {**new_request.data, "module_name": module_name}
    if alloff_product_id is not None:
        data["alloff_product_id"] = alloff_product_id
    if raw_html is not None and raw_html != "":
        text_nodes, images = _parse_html(f"<div>{raw_html}</div>")
        data["description"] = text_nodes
        data["description_images"] = images
    return data, raw_html


def _separate_html_from_request(request):
    raw_html = request.data.get("raw_html")
    if raw_html is not None:
        del request.data["raw_html"]
    return raw_html, request


def _parse_html(raw_html):
    soup = BeautifulSoup(raw_html)
    text_nodes = [
        t for x in soup.find_all(text=True) if (t := " ".join(x.split())) != ""
    ]

    images = [
        x["src"]
        for x in soup.find_all("img")
        if "src" in x.attrs and x["src"][:4] == "http"
    ]
    downloaded_images = []
    for img in images:
        downloaded_images.append(download_image_to_s3(img))

    return text_nodes, downloaded_images
