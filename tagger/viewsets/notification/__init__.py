from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status, serializers
from rest_framework import request, mixins
from rest_framework.decorators import action
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
from tagger.core.pushserver.product_diff import ProductDiffPush
from tagger.core.pushserver.timedeal_open import TimedealOpenPush
from tagger.serializers.notification import NotificationSerializer
from datetime import datetime


class CreateNotificationSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    message = serializers.CharField(required=True)
    notificationtype = serializers.ChoiceField(
        choices=NotificationType.choices, required=True)
    referenceid = serializers.CharField(required=False)
    scheduleddate = serializers.DateTimeField()

    class Meta:
        model = Notification
        fields = ['title', 'message', 'notificationtype',
                  'referenceid', 'scheduleddate']

    def create(self, validated_data):
        notification = Notification.objects.create(**validated_data)
        return notification


class SendNotificationSerializer(serializers.Serializer):
    ids = serializers.CharField()
    is_test = serializers.BooleanField(default=True)

    class Meta:
        model = Notification

    def update(self, instance, validated_data):
        instance.sended = datetime.now()
        instance.status = NotificationStatus.SUCCEEDED
        instance.result = validated_data
        instance.save()
        return instance


class NotificationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Notification.objects().order_by("-id")
    search_fields = [
        "notificationtype"
        "deviceids"
        "message"
        "title"
    ]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "send":
            return SendNotificationSerializer
        elif self.action == "create":
            return CreateNotificationSerializer
        return NotificationSerializer

    @extend_schema(request=CreateNotificationSerializer(many=False))
    def create(self, request: Request, *args, **kwargs):
        serializer = CreateNotificationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.validated_data["notificationtype"] == NotificationType.TIMEDEAL_OPEN_NOTIFICATION:
            serializer.validated_data["navigateto"] = "/timedeals"
            if "referenceid" not in serializer.validated_data:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            try:
                AlloffProductGroup.objects.get(id=ObjectId(
                    serializer.validated_data["referenceid"]))
            except AlloffProductGroup.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.validated_data["referenceid"] = "/" + \
                serializer.validated_data["referenceid"]
        elif serializer.validated_data["notificationtype"] == NotificationType.PRODUCT_DIFF_NOTIFICATION:
            serializer.validated_data["navigateto"] = "/products"
            if "referenceid" not in serializer.validated_data:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            try:
                Product.objects.get(id=ObjectId(
                    serializer.validated_data["referenceid"]))
            except Product.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.validated_data["referenceid"] = "/" + \
                serializer.validated_data["referenceid"]
        else:
            serializer.validated_data["navigateto"] = "/home"
            serializer.validated_data["referenceid"] = "/"

        devices: Device = Device.objects.filter(allownotification=True)
        device_ids = [d.deviceid for d in devices]
        device_groups = list_chunk(device_ids, 300)
        for device_group in device_groups:
            noti = Notification(
                status=NotificationStatus.READY,
                notificationtype=serializer.validated_data["notificationtype"],
                title=serializer.validated_data["title"],
                message=serializer.validated_data["message"],
                deviceids= device_group,
                mobiles="",
                navigateto=serializer.validated_data["navigateto"],
                referenceid=serializer.validated_data["referenceid"],
                created=datetime.now(),
                updated=datetime.now(),
                scheduleddate=datetime.now(),
                sended=None,
                result=None,
            )
            noti.save()
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def send(self, request: Request):
        serializer = SendNotificationSerializer(data=request.data)
        if serializer.is_valid():
            noti_ids = serializer.validated_data["ids"].split(",")
            is_test = serializer.validated_data["is_test"]
            prod_test_devices = [
                "c0IfW-xzdUx3nu6XmpzXNz:APA91bGYmuaoWsdoNzhp_SqUiaKm_8bPK-MfUgmJpmvprUui6run4qKTEeF8QpPSnrR7f5oK2Suy5BJduO04C2DuKWmYHbYZJCRy_FtI6Rm6kAxEopwiRSGjymiqGzXVpz8i8nffFYV1",
                "dJ4rSV2L60aLpHxQjxoFz-:APA91bGJR2YXQkmBbv0rELM6caPUeZ3C1MnBkz1wlI68wCzDRhc9Bsma3stSCRXTGip-6mxdtj2GfuMT4c0XV85AWDuLr0lkH33VDNRsuc8nqo24JGOHmDDpYl_wetLh9vYL-3I0A6ID",
                "cBRNxXqZwEeapVVni8KJcG:APA91bG7UnRCfxWvNR7ngSYNfhTazApx9yAlQXtXqCJDWpn_X-cwVMnnUDLmjLUCso9s7_oiP_xrBkOqoa-1ie3LaRsckENluZTaxWcNAKpdUvVZtV9Pq_TRgRdmwtpA0kE_-Mx-_Nzl",
                "eEx9IUeGQtGgo__aVsJih4:APA91bG0NaGdVP_2NyfBWAXXXdZ0-iR9J-pRTf6JxjueMowaIg9HQDYiZ5PkGeqTypblQNDg-Fecdask8W6o15lNHOhzCHfHzIzofE63APEZPNQQbRVjaaBCTk6m3kAeIqoBuJl9rmHh",
            ]

            for notification_id in noti_ids:
                noti: Notification = Notification.objects.get(
                    id=ObjectId(notification_id))
                if noti.status != NotificationStatus.READY:
                    continue
                if noti.notificationtype == NotificationType.PRODUCT_DIFF_NOTIFICATION:
                    res = ProductDiffPush(reference_id=noti.referenceid).send(
                        title=noti.title, message=noti.message, devices=noti.deviceids if not is_test else prod_test_devices)
                elif noti.notificationtype == NotificationType.TIMEDEAL_OPEN_NOTIFICATION:
                    res = TimedealOpenPush(reference_id=noti.referenceid).send(
                        title=noti.title, message=noti.message, devices=noti.deviceids if not is_test else prod_test_devices)
                else:
                    pass

                noti.result = res
                noti.updated = datetime.now()
                if res["success"] == "ok":
                    noti.status = NotificationStatus.SUCCEEDED
                    noti.sended = datetime.now()
                else:
                    noti.status = NotificationStatus.FAILED
                noti.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]