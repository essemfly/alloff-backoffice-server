from django import http
from django.http import Http404
from html5lib import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from product.serializers.notification import ListNotiSerializer, NotiSerializer
from product.services.notification import NotificationService
from protos.product.notification_pb2 import ListNotiRequest
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

    # (TODO)
    def create(self, request, *args, **kwargs):
        noti = NotificationService.create(request)
        if noti.succeeded:
            return Response({"succeeded": True}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

    # (TODO)
    @action(detail=True, methods=["post"])
    def send(self, request, *args, **kwargs):
        noti = NotificationService.push(request)
        if noti.is_sent:
            return Response({"succeeded": True}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)
