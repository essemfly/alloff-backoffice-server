from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from tagger.serializers.admin import AdminSerializer


class AdminUserViewSet(
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    serializer_class = AdminSerializer

    @action(methods=["GET"], detail=False)
    def me(self, request: Request):
        serializer = AdminSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
