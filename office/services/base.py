import enum
from typing import List

import grpc
from alloff_backoffice_server.settings import COMPANY_GRPC_REQUEST_KEY
from django.contrib.auth.models import User
from rest_framework.exceptions import APIException, AuthenticationFailed


class GrpcAuthType(enum.Enum):
    COMPANY = "COMPANY"
    USER = "USER"
    ANONYMOUS = "ANONYMOUS"

    @staticmethod
    def all():
        return [
            GrpcAuthType.ANONYMOUS,
            GrpcAuthType.COMPANY,
            GrpcAuthType.USER,
        ]


def grpc_request(
    GrpcRequestClass,
    auth_types: List[GrpcAuthType] = [],
    is_stream: bool = False,
):
    def decorator(original_func):
        method_name = original_func.__name__

        def wrapper_func(cls, *args, **kwargs):
            with cls.channel as channel:
                stub = cls.stub(channel)
                try:
                    stub_function = getattr(stub, method_name)
                except AttributeError:
                    raise APIException(
                        f"{method_name} is not implemented in {stub.__module__}"
                    )
                if (
                    GrpcAuthType.COMPANY in auth_types
                    or GrpcAuthType.USER in auth_types
                ):
                    allow_anonymous = GrpcAuthType.ANONYMOUS in auth_types

                    if kwargs.get("user") is None:
                        raise APIException(
                            f"A user should be given to {original_func.__name__} in order to use company / user info."
                        )
                    if GrpcAuthType.COMPANY in auth_types:
                        kwargs = {
                            **kwargs,
                            **cls.get_companyinfo(
                                kwargs["user"],
                                allow_anonymous=allow_anonymous,
                            ),
                        }
                    if GrpcAuthType.USER in auth_types:
                        kwargs = {
                            **kwargs,
                            **cls.get_userinfo(
                                kwargs["user"],
                                allow_anonymous=allow_anonymous,
                            ),
                        }
                if "user" in kwargs:
                    del kwargs["user"]

                request = GrpcRequestClass(**kwargs)

                if is_stream:
                    return list(stub_function(request))
                return stub_function(request)

        return wrapper_func

    return decorator


class GrpcServiceUrlNotDefinedException(Exception):
    pass


class GrpcService:
    url = ""
    stub = None

    @classmethod
    @property
    def channel(cls) -> grpc.Channel:
        if cls.url == "":
            raise GrpcServiceUrlNotDefinedException
        return grpc.insecure_channel(cls.url)

    @classmethod
    def get_userinfo(cls, user: User, allow_anonymous: bool = False) -> dict:
        if user.is_anonymous:
            if allow_anonymous:
                return {}
            else:
                raise AuthenticationFailed("User is anonymous")

        return {
            "user_uuid": str(user.profile.uuid),
            "user_username": user.username,
        }

    @classmethod
    def get_companyinfo(
        cls,
        user: User,
        allow_anonymous: bool = False,
    ) -> dict:
        if user.is_anonymous:
            if allow_anonymous:
                return {}
            else:
                raise AuthenticationFailed("User is anonymous")
        return {
            COMPANY_GRPC_REQUEST_KEY: user.profile.company.keyname,
        }
