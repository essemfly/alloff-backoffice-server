import grpc
from typing import List
from google.protobuf.json_format import MessageToDict


class GrpcServiceUrlNotDefinedException(Exception):
    pass


class GrpcService:
    url = ""
    null_if_empty = []

    @classmethod
    def to_dict(cls, data) -> dict:
        data = MessageToDict(
            data, preserving_proto_field_name=True, including_default_value_fields=True
        )
        for key in cls.null_if_empty:
            if key in data and data[key] == "":
                data[key] = None
        return data

    @classmethod
    def to_array(cls, data) -> List[dict]:
        return [cls.to_dict(x) for x in data]

    @classmethod
    @property
    def channel(cls) -> grpc.Channel:
        if cls.url == "":
            raise GrpcServiceUrlNotDefinedException
        return grpc.insecure_channel(cls.url)
