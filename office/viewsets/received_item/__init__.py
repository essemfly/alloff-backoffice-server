from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from office.serializers.received_item import (
    PaginatedReceivedItemSerializer,
    ReceivedItemSerializer,
    ReceivedItemStatus,
)
from office.services.received_item import ReceivedItemService
from rest_framework import mixins, response, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from office.utils.openapi import PROTO_PAGINATION_QUERY_PARAMS
from order.models.order_item import OrderItem

from order.models.order_item_action_log import (
    InventoryReceiptLog,
    OrderItemActionLog,
    OrderItemActionType,
)


@extend_schema_view(
    list=extend_schema(
        responses={status.HTTP_200_OK: PaginatedReceivedItemSerializer},
        parameters=PROTO_PAGINATION_QUERY_PARAMS
        + [
            OpenApiParameter(
                "statuses",
                {
                    "type": "array",
                    "items": {"type": "string", "enum": ReceivedItemStatus.values},
                },
                OpenApiParameter.QUERY,
                explode=True,
            ),
        ],
    ),
    destroy=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)]
    ),
    make_inventory=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)]
    ),
)
class ReceivedItemViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return PaginatedReceivedItemSerializer
        return ReceivedItemSerializer

    def list(self, request: Request, *args, **kwargs):
        list_response = ReceivedItemService.list(
            size=int(request.query_params.get("size")),
            page=int(request.query_params.get("page")),
            search=request.query_params.get("search"),
            statuses=request.query_params.getlist("statuses"),
        )
        serializer = PaginatedReceivedItemSerializer(list_response)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["POST"])
    def make_inventory(self, request: Request, pk=None):
        received_item = ReceivedItemService.receive(int(pk))
        already_received = InventoryReceiptLog.objects.filter(
            inventory_id=received_item.id
        ).exists()
        if not already_received:
            order_item = OrderItem.objects.get(id=received_item.order_item_id)
            log = OrderItemActionLog.objects.create(
                # admin=request.user,
                admin_id=1,
                order_item=order_item,
                action_type=OrderItemActionType.RECEIVED_INVENTORY,
            )
            InventoryReceiptLog.objects.create(
                # admin=request.user,
                admin_id=1,
                order_item=order_item,
                action_log=log,
                received_item_id=received_item.id,
                received_item_code=received_item.code,
                inventory_id=received_item.inventory.id,
                inventory_code=received_item.inventory.code,
            )
        serializer = ReceivedItemSerializer(received_item)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

        # ri = self.get_object()  # type: ReceivedItem
        # inventory = make_inventory_with_received_item(ri)
        # ri.processor = request.user if (
        #         request.user is not None and not request.user.is_anonymous) else User.objects.filter(
        #     username="backoffice_server").first()
        # ri.status = ReceivedItemStatus.RECEIVED
        # ri.inventory = inventory
        # ri.save()
        # print_label(make_receiving_label(inventory))
        # return Response(InventorySerializer(inventory).data, status=status.HTTP_200_OK)

    @action(detail=True, url_path="revert-inventory", methods=["POST"])
    def revert_inventory(self, request: Request, pk=None):
        return response.Response({""})
        # ri = self.get_object()  # type: ReceivedItem
        # if ri.inventory is None:
        #     raise BaseException("Inventory does not exist")
        # inventory = ri.inventory
        # ri.inventory = None
        # ri.save()

        # inventory.delete()
        # ri.status = ReceivedItemStatus.REQUESTED
        # ri.save()

        # return Response(ReceivedItemSerializer(ri).data, status=status.HTTP_200_OK)
