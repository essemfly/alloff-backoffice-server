from django.http import Http404
from html5lib import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.serializers.notification import NotiSerializer
from product.services.notification import NotificationService


class NotificationList(APIView):
    def get(self, request, format=None):
        pgs = NotificationService.list()
        serializer = NotiSerializer(pgs, many=True)
        return Response(serializer.data)


class NotificationDetail(APIView):
    def post(self, request, format=None):
        pg = NotificationService.create(request)
        serializer = NotiSerializer(pg)
        return Response(serializer.data)

    def send(self, request, pk, format=None):
        pg = NotificationService.push(request)
        serializer = NotiSerializer(pg)
        return Response(serializer.data)
