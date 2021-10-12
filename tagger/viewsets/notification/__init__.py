from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from tagger.core.drf.search_filter import CustomSearchFilter
from tagger.core.mongo.models.alloff_product_group import AlloffProductGroup
from tagger.core.mongo.models.notification import Notification
from tagger.serializers.notification import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects().order_by("-id")
    search_fields = [
        "notificationtype"
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer