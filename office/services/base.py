import grpc
from typing import List
from google.protobuf.json_format import MessageToDict
from django.contrib.auth.models import User

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
    def get_userinfo(cls, user: User) -> dict:
        return {
            "user_uuid": str(user.profile.uuid),
            "user_username": user.username,
        }