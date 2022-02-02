from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.utils.functional import cached_property
from rest_framework.pagination import PageNumberPagination


# Without this, MongoEngine pagination will be too slow.
class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        return self.object_list.count()


class CustomPageNumberPagination(PageNumberPagination):
    max_page_size = 100
    page_size_query_param = "size"  # items per page
    django_paginator_class = FasterDjangoPaginator
