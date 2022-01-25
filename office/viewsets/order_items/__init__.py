import operator
from functools import reduce

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from office.serializers.order_item import (
    OrderItemListSerializer,
    OrderItemRetrieveSerializer,
)
from office.viewsets.order_items.add_memo import AddOrderItemMemoSerializer, add_memo
from office.viewsets.order_items.change_status import (
    ChangeStatusSerializer,
    change_status,
)
from office.viewsets.order_items.delete_memo import (
    DeleteItemOrderMemoSerializer,
    delete_memo,
)
from order.models.order_item import OrderItem, OrderItemStatus
from rest_framework import filters, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from django.db.models import Prefetch

from order.models.order_item_action_log import OrderItemActionLog

# class OrdersSearchFilter(filters.SearchFilter):
#     def filter_queryset(self, request, queryset, view):
#         search_fields = self.get_search_fields(view, request)
#         search_terms = self.get_search_terms(request)

#         if not search_fields or not search_terms:
#             return queryset

#         orm_lookups = [
#             self.construct_search(str(search_field)) for search_field in search_fields
#         ]

#         conditions = []
#         payment_conditions = []

#         for search_term in search_terms:
#             queries = [Q(**{orm_lookup: search_term}) for orm_lookup in orm_lookups if "code" not in orm_lookup]
#             conditions.append(reduce(operator.or_, queries))

#             payment_query = Q(**{"buyername__icontains": search_term})
#             payment_conditions.append(payment_query)

#         payment_queryset = Payment.objects.filter(
#             reduce(operator.or_, payment_conditions)
#         ).all()

#         oids_q = Q(**{"id__in": [x.order_id for x in ExtendedOrder.objects.filter(code__icontains=search_terms[0]).all()]})

#         payment_matched_q = Q(
#             **{"id__in": [x.merchantuid for x in payment_queryset.all()]}
#         )

#         conditions = [x | payment_matched_q | oids_q for x in conditions]
#         print(conditions)
#         queryset = queryset.filter(reduce(operator.and_, conditions))
#         return queryset


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                "statuses",
                {"type": "array", "items": {"type": "string"}},
                OpenApiParameter.QUERY,
                explode=False,
            ),
            OpenApiParameter("created__gte", OpenApiTypes.DATE, OpenApiParameter.QUERY),
            OpenApiParameter("created__lte", OpenApiTypes.DATE, OpenApiParameter.QUERY),
        ]
    ),
)
class OrderItemViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    # filter_backends = [OrdersSearchFilter]

    # search_fields = [
    #     "user__mobile",
    #     "orders__product__name",
    #     "orders__alloffproduct__name",
    #     "code"
    # ]

    # permission_classes = [IsAuthenticated]

    # my_filter_fields = ('statuses', 'created__gte', 'created__lte')  # specify the fields on which you want to filter

    # def get_kwargs_for_filtering(self):
    #     filtering_kwargs = {}
    #     for field in self.my_filter_fields:  # iterate over the filter fields
    #         field_value = self.request.query_params.get(field)  # get the value of a field from request query parameter
    #         if field_value:
    #             filtering_kwargs[field] = field_value
    #     return filtering_kwargs

    def get_queryset(self):
        queryset = OrderItem.objects.exclude(
            order_item_status__in=[
                OrderItemStatus.ORDER_ITEM_CREATED,
                OrderItemStatus.ORDER_ITEM_RECREATED,
                OrderItemStatus.ORDER_ITEM_PAYMENT_PENDING,
            ],
        ).order_by("-id")

        # if "search" in self.request.query_params:
        #     return queryset

        # filtering_kwargs = self.get_kwargs_for_filtering()  # get the fields with values for filtering
        # if filtering_kwargs:
        #     for key, value in filtering_kwargs.items():
        #         if key == 'statuses':
        #             queryset = queryset.filter(__raw__={'orderstatus': {"$in": value.split(",")}})
        #         else:
        #             queryset = queryset.filter(**{key: value})  # filter the queryset based on 'filtering_kwargs'
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)
        ],  # path variable was overridden
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get_object(self):
        try:
            item = OrderItem.get(self.kwargs.get("id"))
        except Exception as e:
            raise APIException("Failed fetching order item: " + str(e))
        # make_ri(order)
        return item

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderItemRetrieveSerializer
        # elif self.action == "add_payment_adjustment":
        #     return AddPaymentAdjustmentSerializer
        # elif self.action == "update_refund":
        #     return UpdateRefundSerializer
        elif self.action == "change_status":
            return ChangeStatusSerializer
        elif self.action == "add_memo":
            return AddOrderItemMemoSerializer
        elif self.action == "delete_memo":
            return DeleteItemOrderMemoSerializer
        # elif self.action == "remake_ri":
            # return ReceivedItemSerializer
        # elif "minimum" in self.action:
        #     return OrderMinimumSerializer
        return OrderItemListSerializer

    # @extend_schema(
    #     parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    # )
    # @action(detail=True, methods=["POST"])
    # def remake_ri(self, request: Request, id=None):
    #     return remake_ri(self, request, id)

    # # Separate logics must be implemented for analytics purposes
    # @extend_schema(responses=OrderMinimumSerializer(many=True))
    # @action(methods=["GET"], detail=False, pagination_class=None, url_path='list-minimum-all')
    # def list_minimum(self, request: Request):
    #     return Response(self.get_serializer(Order.objects(
    #         orderstatus__nin=["CREATED", "RECREATED", "PAYMENT_PENDING"],
    #         user__mobile__nin=["01028861089", "01077591771"]
    #     ).all(), many=True).data, status=status.HTTP_200_OK)

    @extend_schema(
        responses=OrderItemListSerializer(many=True),
        parameters=[
            OpenApiParameter("user_id", OpenApiTypes.STR, OpenApiParameter.PATH)
        ],  # path variable was overridden
    )
    @action(
        methods=["GET"],
        detail=False,
        pagination_class=None,
        url_path="by_user/(?P<user_id>[^/.]+)",
    )
    def by_user(self, request: Request, user_id: str):
        items = OrderItem.objects.filter(order__user_id=user_id).all()
        return Response(
            OrderItemListSerializer(items, many=True).data, status=status.HTTP_200_OK
        )

    @extend_schema(
        parameters=[
            OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)
        ],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def add_memo(self, request: Request, id=None):
        return add_memo(self, request, id)

    @extend_schema(
        parameters=[
            OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)
        ],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def delete_memo(self, request: Request, id=None):
        return delete_memo(self, request, id)

    @extend_schema(
        parameters=[
            OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)
        ],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def change_status(self, request: Request, id=None):
        return change_status(self, request, id)

    # @extend_schema(
    #     parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    # )
    # @action(detail=True, methods=["POST"])
    # def add_payment_adjustment(self, request: Request, id=None):
    #     return add_payment_adjustment(self, request, id)

    # @extend_schema(
    #     parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    # )
    # @action(detail=True, methods=["POST"])
    # def update_refund(self, request: Request, id=None):
    #     return update_refund(self, request, id)
