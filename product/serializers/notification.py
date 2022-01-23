from rest_framework import serializers
from django_grpc_framework import proto_serializers
from protos.product.notification_pb2 import NotificationMessage


class NotiSerializer(proto_serializers.ProtoSerializer):
    notification_id = serializers.CharField()
    status = serializers.CharField()
    type = serializers.CharField()
    reference_id = serializers.CharField()
    title = serializers.CharField()
    message = serializers.CharField()
    sended_at = serializers.DateTimeField()

    class Meta:
        proto_class = NotificationMessage
