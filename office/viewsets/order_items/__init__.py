from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from office.serializers.order_item import (
    OrderItemListSerializer,
    OrderItemRetrieveSerializer,
    OrderItemStatus,
    PaginatedOrderItemSerializer,
)
from office.services.order_item import OrderItemService
from office.utils.openapi import PROTO_PAGINATION_QUERY_PARAMS
from office.viewsets.order_items.add_memo import AddOrderItemMemoSerializer
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action

# from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from office.viewsets.order_items.change_status import ChangeStatusSerializer
from office.viewsets.order_items.delete_memo import DeleteItemOrderMemoSerializer

from office.viewsets.pagination import PaginationListMixin


@extend_schema_view(
    retrieve=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.STR, OpenApiParameter.PATH)],
        responses=OrderItemRetrieveSerializer,
    ),
    list=extend_schema(
        responses={status.HTTP_200_OK: PaginatedOrderItemSerializer},
        parameters=PROTO_PAGINATION_QUERY_PARAMS
        + [
            OpenApiParameter(
                "statuses",
                {
                    "type": "array",
                    "items": {"type": "string", "enum": OrderItemStatus.values},
                },
                OpenApiParameter.QUERY,
                explode=True,
            ),
        ],
    ),
    # force_make_ri=extend_schema(
    # responses={status.HTTP_200_OK: ReceivedItemSerializer(many=True)},
    # ),
)
class OrderItemViewSet(
    PaginationListMixin,
    mixins.RetrieveModelMixin,
    viewsets.ViewSet,
):
    # permission_classes = [IsAuthenticated]

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
        # elif self.action == "force_make_ri":
        #     return ForceMakeRiSerializer
        # elif "minimum" in self.action:
        #     return OrderMinimumSerializer
        return OrderItemListSerializer

    def retrieve(self, request: Request, pk=None):
        retrieve_response = OrderItemService.retrieve(pk)
        serializer = OrderItemRetrieveSerializer(retrieve_response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def list(self, request: Request, *args, **kwargs):
        list_response = OrderItemService.list(
            **self.get_pagination_params(request),
            statuses=request.query_params.getlist("statuses"),
        )
        serializer = PaginatedOrderItemSerializer(list_response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # @extend_schema(
    #     responses=OrderItemListSerializer(many=True),
    #     parameters=[
    #         OpenApiParameter("user_id", OpenApiTypes.STR, OpenApiParameter.PATH)
    #     ],  # path variable was overridden
    # )
    # @action(
    #     methods=["GET"],
    #     detail=False,
    #     pagination_class=None,
    #     url_path="by_user/(?P<user_id>[^/.]+)",
    # )
    # def by_user(self, request: Request, user_id: str):
    #     items = OrderItem.objects.filter(order__user_id=user_id).all()
    #     return Response(
    #         OrderItemListSerializer(items, many=True).data, status=status.HTTP_200_OK
    #     )

    @extend_schema(
        responses={status.HTTP_200_OK: OrderItemListSerializer},
        parameters=[
            OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)
        ],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def add_memo(self, request: Request, pk=None):
        serializer = AddOrderItemMemoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = OrderItemService.add_memo(
            int(pk),
            serializer.validated_data.get("body"),
            request.user,
        )
        return Response(
            OrderItemRetrieveSerializer(item).data, status=status.HTTP_200_OK
        )

    @extend_schema(
        responses={status.HTTP_200_OK: OrderItemListSerializer},
        parameters=[
            OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)
        ],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def delete_memo(self, request: Request, pk=None):
        serializer = DeleteItemOrderMemoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = OrderItemService.delete_memo(
            int(pk),
            serializer.validated_data.get("memo_id"),
            request.user,
        )
        return Response(
            OrderItemRetrieveSerializer(item).data, status=status.HTTP_200_OK
        )

    # @extend_schema(
    #     parameters=[
    #         OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)
    #     ],  # path variable was overridden
    # )
    # @action(detail=True, methods=["POST"])
    # def delete_memo(self, request: Request, id=None):
    #     return delete_memo(self, request, id)

    @extend_schema(
        parameters=[
            OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)
        ],  # path variable was overridden
    )
    @action(detail=True, methods=["POST"])
    def change_status(self, request: Request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = OrderItemService.change_status(
            int(pk),
            serializer.validated_data.get("status"),
            tracking_number=serializer.validated_data.get("tracking_number"),
            tracking_url=serializer.validated_data.get("tracking_url"),
            user=request.user,
        )
        return Response(
            OrderItemRetrieveSerializer(item).data, status=status.HTTP_200_OK
        )

    # @action(detail=True, methods=["POST"], pagination_class=None)
    # def force_make_ri(self, request: Request, id=None):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     received_items = ReceivedItemService.force_make(
    #         self.get_object(), serializer.data.get("quantity")
    #     )
    #     item = self.get_object()
    #     for ri in received_items:
    #         OrderItemActionLog.objects.create(
    #             order_item=item,
    #             admin=request.user,
    #             action_type=OrderItemActionType.FORCE_GENERATED_RECEIVED_ITEM,
    #             detail=ri["code"],
    #         )
    #         ReceivedItemGenerationLog.objects.create(
    #             admin=request.user,
    #             order_item=item,
    #             received_item_id=ri["id"],
    #             received_item_code=ri["code"],
    #             is_force=True,
    #         )
    #     return Response(
    #         ReceivedItemSerializer(received_items, many=True).data,
    #         status=status.HTTP_200_OK,
    #     )

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
