from drf_spectacular.utils import extend_schema
from rest_framework import response, serializers, status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from alloff_backoffice_server.settings import SIMPLE_JWT


class TokenObtainPairRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @extend_schema(
        request=TokenObtainPairRequestSerializer,
        responses={status.HTTP_200_OK: TokenObtainPairResponseSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenRefreshRequestSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenRefreshView(TokenRefreshView):
    @extend_schema(
        request=TokenRefreshRequestSerializer,
        responses={status.HTTP_200_OK: TokenRefreshResponseSerializer},
    )
    def post(self, request, *args, **kwargs):
        refresh = request._request.COOKIES.get(SIMPLE_JWT["REFRESH_TOKEN_NAME"])
        if refresh is None:
            raise InvalidToken(
                "No valid token found in cookie " + SIMPLE_JWT["REFRESH_TOKEN_NAME"]
            )
        serializer = self.get_serializer(data={"refresh": refresh})
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return response.Response(serializer.validated_data, status=status.HTTP_200_OK)


class TokenVerifyResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenVerifyView(TokenVerifyView):
    # @swagger_auto_schema(responses={status.HTTP_200_OK: TokenVerifyResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
