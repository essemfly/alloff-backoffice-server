from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from bson.objectid import ObjectId

from tagger.core.drf.search_filter import CustomSearchFilter
from tagger.core.mongo.models.alloff_product_group import AlloffProductGroup
from tagger.core.mongo.models.notification import Notification, NotificationStatus, NotificationType
from tagger.core.mongo.models.user import Device
from tagger.core.mongo.models.order import Order
from tagger.core.mongo.models.product import Product
from tagger.serializers.notification import NotificationSerializer
from tagger.viewsets.notification.send_notification import SendNotificationSerializer
from datetime import datetime

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects().order_by("-id")
    search_fields = [
        "notificationtype"
        "deviceids"
        "message"
        "title"
    ]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "send_notification":
            return SendNotificationSerializer
        elif self.action == "create":
            return CreateNotificationSerializer
        return NotificationSerializer

    def create(self, request: Request, *args, **kwargs):
        serializer = CreateNotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["created"] = datetime.now()
            serializer.validated_data["updated"] = datetime.now()
            serializer.validated_data["sended"] = None
            serializer.validated_data["deviceids"] = []
            serializer.validated_data["status"] = NotificationStatus.READY
            serializer.validated_data["referenceid"] = ""
            if serializer.validated_data["notificationtype"] == NotificationType.TIMEDEAL_OPEN_NOTIFICATION:
                serializer.validated_data["navigateto"] = "/timedeals"
                if "referenceid" not in serializer.validated_data:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                try:
                    AlloffProductGroup.objects.get(id=ObjectId(serializer.validated_data["referenceid"]))
                except AlloffProductGroup.DoesNotExist:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                serializer.validated_data["referenceid"] = "/" + serializer.validated_data["referenceid"]
            elif serializer.validated_data["notificationtype"] == NotificationType.PRODUCT_DIFF_NOTIFICATION:
                serializer.validated_data["navigateto"] = "/products"
                if "referenceid" not in serializer.validated_data:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                try: 
                    Product.objects.get(id=ObjectId(serializer.validated_data["referenceid"]))
                except Product.DoesNotExist:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                serializer.validated_data["referenceid"] = "/" + serializer.validated_data["referenceid"]
            else:
                serializer.validated_data["navigateto"] = "/home"

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateNotificationSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    message = serializers.CharField(required=True)
    notificationtype = serializers.ChoiceField(
        choices=NotificationType.choices, required=True)
    referenceid = serializers.CharField(required=False)
    scheduleddate = serializers.DateTimeField()

    class Meta:
        model = Notification
        fields = ['title', 'message', 'notificationtype', 'referenceid', 'scheduleddate']

    def create(self, validated_data):
        notification = Notification.objects.create(**validated_data)
        return notification