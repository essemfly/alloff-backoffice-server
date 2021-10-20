from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from tagger.core.drf.search_filter import CustomSearchFilter
from tagger.core.mongo.models.alloff_product_group import AlloffProductGroup
from tagger.core.mongo.models.notification import Notification, NotificationType
from tagger.serializers.notification import NotificationSerializer
from tagger.viewsets.notification.send_notification import SendNotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects().order_by("-id")
    search_fields = [
        "notificationtype"
    ]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "send_notification":
            return SendNotificationSerializer
        elif self.action == "create":
            return CreateNotificationSerializer
        return NotificationSerializer

    def create(self, request : Request, *args, **kwargs):
        notification : Notification= self.get_object()
        if notification.notificationtype == NotificationType.TIMEDEAL_OPEN_NITIFICATION:
            notification.referenceid = request.data.referenceid
            notification.navigateto = "/timedeals"
            # notification.deviceids = 
            # Notification.Objects(id=notification._id).update_one(set__)
        else:
            pass
        return super().create(request, *args, **kwargs)



class CreateNotificationSerializer(serializers.Serializer):
    pass