from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from office.serializers.order_item import (
    OrderItemListSerializer,
    OrderItemRetrieveSerializer,
)
from office.services.order_item import OrderItemService
from office.viewsets.order_items.base import OrderItemViewSetBase
from office.viewsets.order_items.logics.change_status import ApiTrackingInfoSerializer
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class OrderItemCompanyApiViewSet(OrderItemViewSetBase):
    def get_set_tracking_info_grpc_kwargs(self, request, pk=None):
        serializer = ApiTrackingInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return {
            "id": int(pk),
            "courier_id": serializer.validated_data.get("courier_id"),
            "tracking_number": serializer.validated_data.get("tracking_number"),
            "user": request.user,
        }

    @extend_schema(
        responses={HTTP_200_OK: OrderItemListSerializer},
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["POST"])
    def set_tracking_info(self, request: Request, pk=None):
        item = OrderItemService.set_tracking_info(
            **self.get_set_tracking_info_grpc_kwargs(request, pk)
        )
        return Response(OrderItemRetrieveSerializer(item).data, status=HTTP_200_OK)
