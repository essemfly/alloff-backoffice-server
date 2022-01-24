from django import http
from django.http import Http404
from html5lib import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.serializers.notification import ListNotiSerializer, NotiSerializer
from product.services.notification import NotificationService
from protos.product.notification_pb2 import ListNotiRequest


class NotificationList(APIView):
    def get(self, request, format=None):
        offset = request.query_params.get("offset", 0)
        limit = request.query_params.get("limit", 100)

        req = ListNotiRequest(offset=offset, limit=limit)
        notis = NotificationService.list(req)
        serializer = ListNotiSerializer(notis)
        return Response(serializer.data)


class NotificationDetail(APIView):
    def post(self, request, format=None):
        noti = NotificationService.create(request)
        if noti.succeeded:
            return Response({"succeeded": True}, status=status.HTTP_200_OK)
        return Response({"succeded": False})

    def send(self, request, pk, format=None):
        noti = NotificationService.push(request)
        if noti.is_sent:
            return Response({"succeeded": True}, status=status.HTTP_200_OK)
        return Response({"succeded": False})
