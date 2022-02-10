from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from office.serializers.order_item import (OrderItemListSerializer,
                                           OrderItemRetrieveSerializer)
from office.services.order_item import OrderItemService
from office.viewsets.order_items.base import OrderItemViewSetBase
from office.viewsets.order_items.logics.add_memo import \
    AddOrderItemMemoSerializer
from office.viewsets.order_items.logics.change_status import ChangeStatusSerializer
from office.viewsets.order_items.logics.delete_memo import \
    DeleteItemOrderMemoSerializer
from office.viewsets.order_items.serializers import (
    OrderItemAdjustPaymentSerializer, UpdateRefundSerializer)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


class OrderItemBackofficeViewSet(OrderItemViewSetBase):
    # permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={status.HTTP_200_OK: OrderItemListSerializer},
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["POST"])
    def change_status(self, request: Request, pk=None):
        serializer = ChangeStatusSerializer(data=request.data)
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

    @extend_schema(
        responses={status.HTTP_200_OK: OrderItemListSerializer},
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
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
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
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

    @extend_schema(
        responses=OrderItemListSerializer,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["POST"])
    def force_receive(self, request: Request, pk=None):
        item = OrderItemService.force_receive(int(pk), request.user)
        return Response(
            OrderItemRetrieveSerializer(item).data, status=status.HTTP_200_OK
        )

    @extend_schema(
        request=OrderItemAdjustPaymentSerializer,
        responses=OrderItemRetrieveSerializer,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["POST"])
    def adjust_payment(self, request: Request, pk=None):
        serializer = OrderItemAdjustPaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = OrderItemService.adjust_payment(
            id=int(pk),
            user=request.user,
            amount=serializer.validated_data.get("amount"),
            method=serializer.validated_data.get("method"),
            bank_account_info=serializer.validated_data.get("bank_account_info"),
            reason=serializer.validated_data.get("reason"),
        )
        return Response(
            OrderItemRetrieveSerializer(item).data, status=status.HTTP_200_OK
        )

    @extend_schema(
        request=UpdateRefundSerializer,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["POST"])
    def update_refund(self, request: Request, pk=None):
        serializer = UpdateRefundSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = OrderItemService.update_refund(
            id=int(pk),
            user=request.user,
            refund_amount=serializer.validated_data.get("refund_amount"),
            refund_fee=serializer.validated_data.get("refund_fee"),
        )
        return Response(
            OrderItemRetrieveSerializer(item).data, status=status.HTTP_200_OK
        )
