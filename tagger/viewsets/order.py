from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework_mongoengine import viewsets
from tagger.core.drf.search_filter import CustomSearchFilter
from tagger.core.mongo.models.order import Order
from tagger.serializers.order import OrderListSerializer, OrderRetrieveSerializer


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Order.objects(orderstatus__nin=["CREATED", "RECREATED"])
    filter_backends = [CustomSearchFilter]
    search_fields = ["user__mobile"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderRetrieveSerializer
        return OrderListSerializer

    @action(detail=True, methods=["POST"])
    def add_payment_adjustment(self, request, pk=None):
        pass
