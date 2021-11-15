from typing import List

from django.contrib.auth.models import User
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from tagger.core.label.print_label import print_label
from tagger.core.label.receiving_label import make_receiving_label
from tagger.core.mongo.models.order import Order, OrderType
from tagger.models.received_item import ReceivedItem, ReceivedItemStatus
from tagger.serializers.inventory import InventorySerializer
from tagger.serializers.received_item import ReceivedItemSerializer
from tagger.viewsets.received_items.receive_item import make_inventory_with_received_item


def make_ri(order: Order, force=False) -> List[ReceivedItem]:
    result = []
    if not force and ReceivedItem.objects.filter(order_id=str(order.id)).count() > 0:
        return

    for orderItem in order.orders:
        itemType, itemName, itemId, keyname, images = None, None, None, None, None
        if orderItem.alloffproduct is not None:
            itemType = OrderType.TIMEDEAL_ORDER
            itemName = orderItem.alloffproduct.name
            itemId = orderItem.alloffproduct._id
            keyname = orderItem.alloffproduct.brand.keyname
            images = orderItem.alloffproduct.images
        elif orderItem.product is not None:
            itemType = OrderType.NORMAL_ORDER
            itemName = orderItem.product.name
            itemId = orderItem.product._id
            keyname = orderItem.product.brand.keyname
            images = orderItem.product.images

        for i in range(orderItem.quantity):
            ri = ReceivedItem.objects.create(
                order_id=str(order.id),
                order_type=itemType,
                item_name=itemName,
                size=orderItem.size,
                product_id=itemId,
                sourcing_code=order.code,
                brand_keyname=keyname,
                is_return="CANCEL" in order.orderstatus,
                images=images,
                ordered=order.created,
            )
            print(f"Created ri {ri.id} ({ri.item_name})")
            result.append(ri)
    return result


class ForceMakeRiSerializer(serializers.Serializer):
    order_ref = serializers.CharField()


class ReceivedItemViewSet(viewsets.ModelViewSet):
    queryset = ReceivedItem.objects.order_by("-id").all()
    filter_backends = [SearchFilter, ]
    search_fields = ['sourcing_code', 'order_id', 'item_name']

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "make_inventory":
            return InventorySerializer
        return ReceivedItemSerializer

    @extend_schema(
        responses=InventorySerializer,
        request=None,
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, url_path="make-inventory", methods=["POST"])
    def make_inventory(self, request: Request, pk=None):
        ri = self.get_object()  # type: ReceivedItem
        inventory = make_inventory_with_received_item(ri)
        ri.processor = request.user if (
                request.user is not None and not request.user.is_anonymous) else User.objects.filter(
            username="backoffice_server").first()
        ri.status = ReceivedItemStatus.RECEIVED
        ri.inventory = inventory
        ri.save()
        print_label(make_receiving_label(inventory))
        return Response(InventorySerializer(inventory).data, status=status.HTTP_200_OK)

    @extend_schema(
        request=None,
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],  # path variable was overridden
    )
    @action(detail=True, url_path="revert-inventory", methods=["POST"])
    def revert_inventory(self, request: Request, pk=None):
        ri = self.get_object()  # type: ReceivedItem
        if ri.inventory is None:
            raise BaseException("Inventory does not exist")
        inventory = ri.inventory
        ri.inventory = None
        ri.save()

        inventory.delete()
        ri.status = ReceivedItemStatus.REQUESTED
        ri.save()

        return Response(ReceivedItemSerializer(ri).data, status=status.HTTP_200_OK)

    @extend_schema(
        request=ForceMakeRiSerializer,
        responses={
            status.HTTP_200_OK: ReceivedItemSerializer(many=True)
        }
    )
    @action(detail=False, url_path="force-make", methods=["POST"])
    def force_make(self, request: Request):
        id_or_code = request.data.get("order_ref")
        if id_or_code is None:
            raise BaseException("No order ref given")

        order = Order.get(id_or_code)
        if order is None:
            raise BaseException("No order with ref " + id_or_code)

        return Response(ReceivedItemSerializer(make_ri(order, force=True), many=True).data, status=status.HTTP_200_OK)
