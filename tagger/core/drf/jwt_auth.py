from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request

from alloff_backoffice_server.settings import SIMPLE_JWT


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request: Request):
        access = request._request.COOKIES.get(SIMPLE_JWT["ACCESS_TOKEN_NAME"])
        # refresh = request._request.COOKIES.get(SIMPLE_JWT["REFRESH_TOKEN_NAME"])
        if access is None:
            return None
        validated_token = self.get_validated_token(access)
        return self.get_user(validated_token), validated_token
