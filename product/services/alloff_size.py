from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService

from gen.pyalloff.alloff_size_pb2 import (
    ListAlloffSizeRequest,
    ListAlloffSizeResponse,
    CreateAlloffSizeRequest,
    EditAlloffSizeRequest,
    GetAlloffSizeRequest,
)
from gen.pyalloff.alloff_size_pb2_grpc import AlloffSizeStub


class AlloffSizeService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def get(cls, request: GetAlloffSizeRequest):
        with cls.channel:
            stub = AlloffSizeStub(cls.channel)
            response = stub.GetAlloffSize(request)

            return response

    @classmethod
    def list(cls, request: ListAlloffSizeRequest):
        with cls.channel:
            stub = AlloffSizeStub(cls.channel)
            response: ListAlloffSizeResponse = stub.ListAlloffSize(request)

            return response

    @classmethod
    def create(cls, request: CreateAlloffSizeRequest):
        with cls.channel:
            stub = AlloffSizeStub(cls.channel)
            response = stub.CreateAlloffSize(request)

            return response

    @classmethod
    def edit(cls, request: EditAlloffSizeRequest):
        with cls.channel:
            stub = AlloffSizeStub(cls.channel)
            response = stub.EditAlloffSize(request)

            return response
