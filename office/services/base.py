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
    stream_to_list: bool = False,
    keep_channel: bool = False,
):
    def decorator(original_func):
        method_name = original_func.__name__

        def wrapper_func(cls, *args, **kwargs):
            def _(channel):
                stub = cls.stub(channel)
                new_kwargs = {}
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
                        new_kwargs = {
                            **kwargs,
                            **cls.get_companyinfo(
                                kwargs["user"],
                                allow_anonymous=allow_anonymous,
                            ),
                        }
                    if GrpcAuthType.USER in auth_types:
                        new_kwargs = {
                            **kwargs,
                            **cls.get_userinfo(
                                kwargs["user"],
                                allow_anonymous=allow_anonymous,
                            ),
                        }
                if "user" in new_kwargs:
                    del new_kwargs["user"]

                request = GrpcRequestClass(**new_kwargs)
                if stream_to_list:
                    return list(stub_function(request))
                return stub_function(request)

            if keep_channel:
                return cls.channel, _(cls.channel)

            else:
                with cls.channel as channel:
                    return _(channel)

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
