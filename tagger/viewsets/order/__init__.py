from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework_mongoengine import viewsets
from tagger.core.drf.search_filter import OrdersSearchFilter
from tagger.core.mongo.models.order import Order
from tagger.serializers.order import OrderListSerializer, OrderRetrieveSerializer
from tagger.viewsets.order.add_memo import AddOrderMemoSerializer, add_memo
from tagger.viewsets.order.add_payment_adjustment import (
    AddPaymentAdjustmentSerializer,
    add_payment_adjustment,
)
from tagger.viewsets.order.change_status import ChangeStatusSerializer, change_status
from tagger.viewsets.order.delete_memo import DeleteOrderMemoSerializer, delete_memo
from tagger.viewsets.order.update_refund import UpdateRefundSerializer, update_refund


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Order.objects(
        orderstatus__nin=["CREATED", "RECREATED", "PAYMENT_PENDING"]
    ).order_by("-id")
    filter_backends = [OrdersSearchFilter]
    search_fields = [
        "user__mobile",
        "orders__product__name",
        "orders__alloffproduct__name",
    ]
    permission_classes = [IsAuthenticated]

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
        return OrderListSerializer

    @action(detail=True, methods=["POST"])
    def add_memo(self, request: Request, id=None):
        return add_memo(self, request, id)

    @action(detail=True, methods=["POST"])
    def delete_memo(self, request: Request, id=None):
        return delete_memo(self, request, id)

    @action(detail=True, methods=["POST"])
    def change_status(self, request: Request, id=None):
        return change_status(self, request, id)

    @action(detail=True, methods=["POST"])
    def add_payment_adjustment(self, request: Request, id=None):
        return add_payment_adjustment(self, request, id)

    @action(detail=True, methods=["POST"])
    def update_refund(self, request: Request, id=None):
        return update_refund(self, request, id)
