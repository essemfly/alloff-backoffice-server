from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from office.serializers.received_item import ReceivedItemSerializer, ReceivedItemStatus
from office.services.received_item import ReceivedItemService
from rest_framework import mixins, response, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                "statuses",
                {
                    "type": "array",
                    "items": {"type": "string", "enum": ReceivedItemStatus.values},
                },
                OpenApiParameter.QUERY,
                explode=True,
            ),
            OpenApiParameter("code", OpenApiTypes.STR, OpenApiParameter.QUERY),
            OpenApiParameter("product_name", OpenApiTypes.STR, OpenApiParameter.QUERY),
            OpenApiParameter(
                "product_brand_name", OpenApiTypes.STR, OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                "product_brand_key_name", OpenApiTypes.STR, OpenApiParameter.QUERY
            ),
        ],
    ),
    destroy=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)]
    ),
)
class ReceivedItemViewSet(mixins.ListModelMixin, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        received_items = ReceivedItemService.list()
        serializer = ReceivedItemSerializer(received_items, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, url_path="make-inventory", methods=["POST"])
    def make_inventory(self, request: Request, pk=None):
        return response.Response({""})

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
