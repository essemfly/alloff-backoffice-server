from django.contrib.auth.models import User
from office.serializers.user import UserSerializer
from rest_framework import mixins, viewsets


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
