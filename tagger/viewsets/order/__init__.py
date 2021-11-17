from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from tagger.core.drf.search_filter import OrdersSearchFilter
from tagger.core.mongo.models.order import Order, OrderStatus
from tagger.serializers.order import OrderListSerializer, OrderRetrieveSerializer, OrderMinimumSerializer
from tagger.viewsets.order.add_memo import AddOrderMemoSerializer, add_memo
from tagger.viewsets.order.add_payment_adjustment import (
    AddPaymentAdjustmentSerializer,
    add_payment_adjustment,
)
from tagger.viewsets.order.change_status import ChangeStatusSerializer, change_status
from tagger.viewsets.order.delete_memo import DeleteOrderMemoSerializer, delete_memo
from tagger.viewsets.order.update_refund import UpdateRefundSerializer, update_refund
from tagger.viewsets.received_items import make_ri


@extend_schema_view(
    list=extend_schema(parameters=[
        OpenApiParameter("statuses", {'type': 'array', 'items': {'type': 'string'}}, OpenApiParameter.QUERY,
                         explode=False),
        OpenApiParameter("created__gte", OpenApiTypes.DATE, OpenApiParameter.QUERY),
        OpenApiParameter("created__lte", OpenApiTypes.DATE, OpenApiParameter.QUERY),
    ]),
)
class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = [OrdersSearchFilter]

    search_fields = [
        "user__mobile",
        "orders__product__name",
        "orders__alloffproduct__name",
        "code"
    ]

    permission_classes = [IsAuthenticated]

    my_filter_fields = ('statuses', 'created__gte', 'created__lte')  # specify the fields on which you want to filter

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        for field in self.my_filter_fields:  # iterate over the filter fields
            field_value = self.request.query_params.get(field)  # get the value of a field from request query parameter
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = Order.objects(
            orderstatus__nin=["CREATED", "RECREATED", "PAYMENT_PENDING"],
        ).order_by("-id")

        if "search" in self.request.query_params:
            return queryset

        filtering_kwargs = self.get_kwargs_for_filtering()  # get the fields with values for filtering
        if filtering_kwargs:
            for key, value in filtering_kwargs.items():
                if key == 'statuses':
                    queryset = queryset.filter(__raw__={'orderstatus': {"$in": value.split(",")}})
                else:
                    queryset = queryset.filter(**{key: value})  # filter the queryset based on 'filtering_kwargs'
        return queryset

    def get_object(self):
        order = Order.get(self.kwargs.get("id"))
        make_ri(order)
        return order

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderRetrieveSerializer
        elif self.action == "add_payment_adjustment":
            return AddPaymentAdjustmentSerializer
        elif self.action == "update_refund":
            return UpdateRefundSerializer
        elif self.action == "change_status":
            return ChangeStatusSerializer
        elif self.action == "add_memo":
            return AddOrderMemoSerializer
        elif self.action == "delete_memo":
            return DeleteOrderMemoSerializer
        elif "minimum" in self.action:
            return OrderMinimumSerializer
        return OrderListSerializer

    # Separate logics must be implemented for analytics purposes
    @extend_schema(responses=OrderMinimumSerializer(many=True))
    @action(methods=["GET"], detail=False, pagination_class=None, url_path='list-minimum-all')
    def list_minimum(self, request: Request):
        return Response(self.get_serializer(Order.objects(
            orderstatus__nin=["CREATED", "RECREATED", "PAYMENT_PENDING"],
            user__mobile__nin=["01028861089", "01077591771"]
        ).all(), many=True).data, status=status.HTTP_200_OK)

    @extend_schema(responses=OrderListSerializer(many=True), parameters=[
        OpenApiParameter("user_id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
                   )
    @action(methods=["GET"], detail=False, pagination_class=None, url_path='by_user/(?P<user_id>[^/.]+)')
    def by_user(self, request: Request, user_id: str):
        orders = self.get_queryset().filter(__raw__={'user._id': user_id})
        return Response(OrderListSerializer(orders, many=True).data, status=status.HTTP_200_OK)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def add_memo(self, request: Request, id=None):
        return add_memo(self, request, id)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def delete_memo(self, request: Request, id=None):
        return delete_memo(self, request, id)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def change_status(self, request: Request, id=None):
        return change_status(self, request, id)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def add_payment_adjustment(self, request: Request, id=None):
        return add_payment_adjustment(self, request, id)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def update_refund(self, request: Request, id=None):
        return update_refund(self, request, id)
