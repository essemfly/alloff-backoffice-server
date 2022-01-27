import grpc
from typing import List
from google.protobuf.json_format import MessageToDict


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
