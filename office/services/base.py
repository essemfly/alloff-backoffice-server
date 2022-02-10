import grpc
from alloff_backoffice_server.settings import COMPANY_GRPC_REQUEST_KEY
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class GrpcServiceUrlNotDefinedException(Exception):
    pass


class GrpcService:
    url = ""

    @classmethod
    @property
    def channel(cls) -> grpc.Channel:
        if cls.url == "":
            raise GrpcServiceUrlNotDefinedException
        return grpc.insecure_channel(cls.url)

    @classmethod
    def get_userinfo(cls, user: User, with_company: bool = False) -> dict:
        userinfo = {
            "user_uuid": str(user.profile.uuid),
            "user_username": user.username,
        }
        if not with_company:
            return userinfo
        return {
            **userinfo,
            COMPANY_GRPC_REQUEST_KEY: cls.get_companyinfo(user),
        }

    @classmethod
    def get_companyinfo(cls, user: User) -> dict:
        if user.is_anonymous or user.profile is None or user.profile.company is None:
            raise AuthenticationFailed("User is not authenticated as a company user.")
        return {
            COMPANY_GRPC_REQUEST_KEY: user.profile.company.keyname,
        }
