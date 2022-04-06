from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter

PROTO_PAGINATION_QUERY_PARAMS = [
    OpenApiParameter("page", OpenApiTypes.INT, OpenApiParameter.QUERY),
    OpenApiParameter("size", OpenApiTypes.INT, OpenApiParameter.QUERY),
    OpenApiParameter("search", OpenApiTypes.STR, OpenApiParameter.QUERY),
]
