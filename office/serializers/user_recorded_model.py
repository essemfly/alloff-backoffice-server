from django.forms import fields
from django_grpc_framework import proto_serializers

class UserRecordedSerializer(proto_serializers.ProtoSerializer):
    user_uuid = fields.UUIDField()
    user_username = fields.CharField()