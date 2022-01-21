from bson import ObjectId
from rest_framework import filters
from functools import reduce
import operator
from mongoengine import Q
from tagger.core.mongo.models.order import Payment
from tagger.models import ExtendedOrder


class CustomSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(str(search_field)) for search_field in search_fields
        ]

        conditions = []
        for search_term in search_terms:
            queries = [Q(**{orm_lookup: search_term}) for orm_lookup in orm_lookups]
            conditions.append(reduce(operator.or_, queries))
        queryset = queryset.filter(reduce(operator.and_, conditions))
        return queryset


class OrdersSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(str(search_field)) for search_field in search_fields
        ]

        conditions = []
        payment_conditions = []

        for search_term in search_terms:
            queries = [Q(**{orm_lookup: search_term}) for orm_lookup in orm_lookups if "code" not in orm_lookup]
            conditions.append(reduce(operator.or_, queries))

            payment_query = Q(**{"buyername__icontains": search_term})
            payment_conditions.append(payment_query)

        payment_queryset = Payment.objects.filter(
            reduce(operator.or_, payment_conditions)
        ).all()

        oids_q = Q(**{"id__in": [x.order_id for x in ExtendedOrder.objects.filter(code__icontains=search_terms[0]).all()]})

        payment_matched_q = Q(
            **{"id__in": [x.merchantuid for x in payment_queryset.all()]}
        )

        conditions = [x | payment_matched_q | oids_q for x in conditions]
        print(conditions)
        queryset = queryset.filter(reduce(operator.and_, conditions))
        return queryset
