from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from datetime import datetime
from bson.objectid import ObjectId


from tagger.models.received_item import ReceivedItem
from tagger.serializers.received_item import ReceivedItemSerializer
from tagger.core.mongo.models.order import Order, OrderType, OrderCodeMap


class ReceivedItemViewSet(viewsets.ModelViewSet):
    queryset = ReceivedItem.objects
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=ReceivedItemSerializer(many=True))
    def list(self, request):
        # self.insert_all_order_items()
        queryset = ReceivedItem.objects.order_by("-id").all()
        page = self.paginate_queryset(queryset)
        serializer = ReceivedItemSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def insert_all_order_items(self):
        orders = (
            Order.objects(
                orderstatus__in=[
                    "PAYMENT_FINISHED",
                    "PRODUCT_PREPARING",
                    "DELIVERY_PREPARING",
                    "CANCEL_REQUESTED",
                    "CANCEL_PENDING",
                ],
            )
            .order_by("id")
            .all()
        )

        for order in orders:
            ocodemap = OrderCodeMap.objects(orderid=ObjectId(order.id)).first()
            for orderItem in order.orders:
                itemType, itemName, itemId = None, None, None
                if orderItem.alloffproduct is not None:
                    itemType = OrderType.TIMEDEAL_ORDER
                    itemName = orderItem.alloffproduct.name
                    itemId = orderItem.alloffproduct._id
                elif orderItem.product is not None:
                    itemType = OrderType.NORMAL_ORDER
                    itemName = orderItem.product.name
                    itemId = orderItem.product._id

                ReceivedItem.objects.get_or_create(
                    order_id=order.id,
                    order_type=itemType,
                    item_name=itemName,
                    quantity=orderItem.quantity,
                    size=orderItem.size,
                    product_id=itemId,
                    sourcing_code=ocodemap.code if ocodemap else None,
                )
