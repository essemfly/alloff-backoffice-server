from django.contrib.auth.models import User
from django.forms import fields
from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_field
from office.serializers.admin import AdminSerializer
from rest_framework import fields


class WithUserSerializer(proto_serializers.ProtoSerializer):
    user_uuid = fields.UUIDField()
    user_username = fields.CharField()
    admin = fields.SerializerMethodField()

    @extend_schema_field(AdminSerializer)
    def get_admin(self, obj):
        return AdminSerializer(User.objects.get(profile__uuid=obj.user_uuid)).data
