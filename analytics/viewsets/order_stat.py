from calendar import week

import arrow
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from gen.serializers.order_analytics import OrderStatResponseSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from analytics.services.order_stat import OrderStatService


class OrderStatViewSet(
    viewsets.ViewSet,
):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                "date_from", OpenApiTypes.DATE, OpenApiParameter.PATH, required=False
            ),
            OpenApiParameter(
                "date_to", OpenApiTypes.DATE, OpenApiParameter.PATH, required=False
            ),
        ],
        responses={status.HTTP_200_OK: OrderStatResponseSerializer},
    )
    @action(detail=False, methods=["GET"])
    def daily(self, request, *args, **kwargs):
        res = OrderStatService.DailyOrderStat(
            date_from=request.query_params.get(
                "date_from", arrow.now().shift(weeks=-1).format("YYYY-MM-DD")
            ),
            date_to=request.query_params.get(
                "date_to", arrow.now().format("YYYY-MM-DD")
            ),
        )
        serializer = OrderStatResponseSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)
