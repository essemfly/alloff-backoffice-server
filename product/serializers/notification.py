from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from django_grpc_framework import proto_serializers
from gen.pyalloff.notification_pb2 import (
    CreateNotiRequest,
    ListNotiRequest,
    NotificationMessage,
    ListNotiResponse,
    SendNotiRequest,
)


class NotiSerializer(proto_serializers.ProtoSerializer):
    notification_id = serializers.CharField()
    status = serializers.CharField()
    noti_type = serializers.CharField()
    reference_id = serializers.CharField()
    title = serializers.CharField()
    message = serializers.CharField()
    sended_at = serializers.DateTimeField()

    class Meta:
        proto_class = NotificationMessage


class ListNotiRequestSerializer(proto_serializers.ProtoSerializer):
    offset = serializers.IntegerField(allow_null=True, required=False)
    limit = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        proto_class = ListNotiRequest


@extend_schema_serializer(many=False)
class ListNotiSerializer(proto_serializers.ProtoSerializer):
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    notis = NotiSerializer(many=True)

    class Meta:
        proto_class = ListNotiResponse


class CreateNotiSerializer(proto_serializers.ProtoSerializer):
    noti_type = serializers.CharField()
    reference_id = serializers.CharField()
    title = serializers.CharField()
    message = serializers.CharField()

    class Meta:
        proto_class = CreateNotiRequest


class SendNotiSerializer(proto_serializers.ProtoSerializer):
    notification_id = serializers.CharField()

    class Meta:
        proto_class = SendNotiRequest
