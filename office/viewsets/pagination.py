from typing import Optional
from rest_framework import request

from alloff_backoffice_server.settings import GRPC_PAGINATION_DEFAULT_PAGE_SIZE


class PaginationListMixin:
    def get_pagination_params(self, request: request.Request) -> dict:
        return {
            "size": self.get_size(request),
            "page": self.get_page(request),
            "search": self.get_search(request),
        }

    def get_size(self, request: request.Request) -> int:
        try:
            return int(request.query_params.get("size"))
        except TypeError:
            return GRPC_PAGINATION_DEFAULT_PAGE_SIZE

    def get_page(self, request: request.Request) -> int:
        try:
            return int(request.query_params.get("page"))
        except TypeError:
            return 1

    def get_search(self, request: request.Request) -> Optional[str]:
        return request.query_params.get("search")
