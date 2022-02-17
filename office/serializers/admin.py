from django.contrib.auth.models import User
from office.models.profile import Profile
from office.serializers.company import CompanySerializer
from rest_framework import fields, serializers


class ProfileSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    is_admin = fields.BooleanField()

    class Meta:
        model = Profile
        exclude = ["uuid", "user", "profile_type", "id"]


class AdminSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        exclude = [
            "password",
            "is_staff",
            "is_superuser",
            "is_active",
            "date_joined",
            "username",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        ]
