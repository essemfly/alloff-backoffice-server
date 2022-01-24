from rest_framework import serializers
from django_grpc_framework import proto_serializers
from protos.product.notification_pb2 import NotificationMessage, ListNotiResponse


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


class ListNotiSerializer(proto_serializers.ProtoSerializer):
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    notis = NotiSerializer(many=True)

    class Meta:
        proto_class = ListNotiResponse
