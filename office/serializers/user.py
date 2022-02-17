from django.contrib.auth.models import User
from office.models.company_brand import CompanyBrand
from office.serializers.profile import ProfileSerializer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = "__all__"
