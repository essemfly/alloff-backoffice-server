from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService
from gen.python.protos.exhibition_pb2 import (
    CreateExhibitionRequest,
    CreateExhibitionResponse,
    EditExhibitionRequest,
    EditExhibitionResponse,
    GetExhibitionRequest,
    GetExhibitionResponse,
    ListExhibitionsRequest,
    ListExhibitionsResponse,
)
from gen.python.protos.exhibition_pb2_grpc import ExhibitionStub


class ExhibitionService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def get(cls, request: GetExhibitionRequest):
        with cls.channel:
            stub = ExhibitionStub(cls.channel)
            response: GetExhibitionResponse = stub.GetExhibition(request)
            return response.exhibition

    @classmethod
    def list(cls, request: ListExhibitionsRequest):
        with cls.channel:
            stub = ExhibitionStub(cls.channel)
            response: ListExhibitionsResponse = stub.ListExhibitions(request)

            return response

    @classmethod
    def edit(cls, request: EditExhibitionRequest):
        with cls.channel:
            stub = ExhibitionStub(cls.channel)
            response: EditExhibitionResponse = stub.EditExhibition(request)
            return response.exhibition

    @classmethod
    def create(cls, request: CreateExhibitionRequest):
        with cls.channel:
            stub = ExhibitionStub(cls.channel)
            response: CreateExhibitionResponse = stub.CreateExhibition(request)
            return response.exhibition