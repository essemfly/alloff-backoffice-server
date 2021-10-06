from datetime import datetime
from typing import List
from drf_yasg.utils import swagger_auto_schema

from iamport.client import Iamport
from rest_framework import mixins, serializers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from tagger.core.alimtalk.cancel_finished import CancelFinishedAlimtalk
from tagger.core.drf.search_filter import CustomSearchFilter, OrdersSearchFilter
from tagger.core.iamport import IMP
from tagger.core.mongo.models.order import Order, OrderStatus, Payment, Refund
from tagger.models.order_action_log import (
    OrderActionLog,
    OrderActionType,
    OrderAlimtalkLog,
    OrderAlimtalkType,
    OrderStatusChangeLog,
)
from tagger.models.order_memo import OrderMemo
from tagger.models.order_payment_adjustment import (
    OrderPaymentAdjustementType,
    OrderPaymentAdjustment,
)
from tagger.serializers.admin import AdminSerializer
from tagger.serializers.order import OrderListSerializer, OrderRetrieveSerializer
from tagger.serializers.order_memo import OrderMemoSerializer
from tagger.serializers.order_payment_adjustment import OrderPaymentAdjustmentSerializer
from tagger.serializers.refund import RefundSerializer
from tagger.core.alimtalk.delivery_started import DeliveryStartedAlimtalk


class AdminUserViewSet(
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    pagination_class = None

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: AdminSerializer},
    )
    @action(methods=["GET"], detail=False)
    def me(self, request: Request):
        serializer = AdminSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
