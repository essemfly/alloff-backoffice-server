from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from alloff_backoffice_server.settings import SIMPLE_JWT
from drf_yasg.utils import swagger_auto_schema
from rest_framework import response, serializers, status, views, mixins
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


class LogoutResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()


class DecoratedLogoutView(views.APIView):
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: LogoutResponseSerializer},
    )
    def post(self, request):
        return response.Response(status=status.HTTP_200_OK)

    def finalize_response(self, request, response, *args, **kwargs):
        print("adsmaksdasd")
        response.delete_cookie(SIMPLE_JWT["ACCESS_TOKEN_NAME"])
        response.delete_cookie(SIMPLE_JWT["REFRESH_TOKEN_NAME"])
        return super().finalize_response(request, response, *args, **kwargs)


class TokenObtainPairResponseSerializer(serializers.Serializer):
    # access = serializers.CharField()
    # refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: TokenObtainPairResponseSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                SIMPLE_JWT["ACCESS_TOKEN_NAME"],
                response.data.get("access"),
                max_age=SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds(),
                httponly=True,
            )
            response.set_cookie(
                SIMPLE_JWT["REFRESH_TOKEN_NAME"],
                response.data.get("refresh"),
                max_age=SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds(),
                httponly=True,
            )
            del response.data["refresh"]
            del response.data["access"]
        return super().finalize_response(request, response, *args, **kwargs)


class TokenRefreshResponseSerializer(serializers.Serializer):
    # access = serializers.CharField()
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        request_body=TokenRefreshResponseSerializer,
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

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("access"):
            response.set_cookie(
                SIMPLE_JWT["ACCESS_TOKEN_NAME"],
                response.data.get("access"),
                max_age=SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds(),
                httponly=True,
            )
            response.set_cookie(
                SIMPLE_JWT["REFRESH_TOKEN_NAME"],
                response.data.get("refresh"),
                max_age=SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds(),
                httponly=True,
            )
            del response.data["refresh"]
            del response.data["access"]
        return super().finalize_response(request, response, *args, **kwargs)


class TokenVerifyResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenVerifyView(TokenVerifyView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: TokenVerifyResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
