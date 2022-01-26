from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from product.serializers.notification import (
    CreateNotiSerializer,
    ListNotiSerializer,
    NotiSerializer,
    SendNotiSerializer,
)
from product.services.notification import NotificationService
from protos.product.notification_pb2 import CreateNotiRequest, ListNotiRequest
from rest_framework import mixins, status, viewsets


class NotificationViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.ViewSet
):
    serializer_class = NotiSerializer

    def list(self, request, *args, **kwargs):
        offset = request.query_params.get("offset", 0)
        limit = request.query_params.get("limit", 100)

        req = ListNotiRequest(offset=offset, limit=limit)
        notis = NotificationService.list(req)
        serializer = ListNotiSerializer(notis)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CreateNotiSerializer,
        responses={status.HTTP_201_CREATED: CreateNotiSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = CreateNotiSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = NotificationService.create(serializer.message)
        if res:
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(res, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=SendNotiSerializer, responses={status.HTTP_200_OK})
    @action(detail=True, methods=["post"])
    def send(self, request, *args, **kwargs):
        serializer = SendNotiSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = NotificationService.create(serializer.message)
        if res:
            return Response(res, status=status.HTTP_200_OK)
        return Response(res, status=status.HTTP_200_OK)
