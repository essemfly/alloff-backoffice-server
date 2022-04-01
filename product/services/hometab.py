from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService
from gen.python.protos.hometab_pb2 import (
    CreateHomeTabItemRequest,
    CreateHomeTabItemResponse,
    EditHomeTabItemRequest,
    EditHomeTabItemResponse,
    GetHomeTabItemRequest,
    GetHomeTabItemResponse,
    ListHomeTabItemsRequest,
    ListHomeTabItemsResponse,
)

from gen.python.protos.hometab_pb2_grpc import HomeTabItemStub


class HometabService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def get(cls, request: GetHomeTabItemRequest):
        with cls.channel:
            stub = HomeTabItemStub(cls.channel)
            response: GetHomeTabItemResponse = stub.GetHomeTabItem(request)
            return response.item

    @classmethod
    def list(cls, request: ListHomeTabItemsRequest):
        with cls.channel:
            stub = HomeTabItemStub(cls.channel)
            response: ListHomeTabItemsResponse = stub.ListHomeTabItems(request)

            return response

    @classmethod
    def edit(cls, request: EditHomeTabItemRequest):
        with cls.channel:
            stub = HomeTabItemStub(cls.channel)
            response: EditHomeTabItemResponse = stub.EditHomeTabItem(request)
            return response.item

    @classmethod
    def create(cls, request: CreateHomeTabItemRequest):
        with cls.channel:
            stub = HomeTabItemStub(cls.channel)
            response: CreateHomeTabItemResponse = stub.CreateHomeTabItem(request)
            return response.item
