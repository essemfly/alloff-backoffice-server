from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService
from gen.python.protos.topbanner_pb2 import (
    CreateTopBannerRequest,
    CreateTopBannerResponse,
    EditTopBannerRequest,
    EditTopBannerResponse,
    GetTopBannerRequest,
    GetTopBannerResponse,
    ListTopBannersRequest,
    ListTopBannersResponse,
)

from gen.python.protos.topbanner_pb2_grpc import TopBannerStub


class TopBannerService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def get(cls, request: GetTopBannerRequest):
        with cls.channel:
            stub = TopBannerStub(cls.channel)
            response: GetTopBannerResponse = stub.GetTopBanner(request)
            return response.banner

    @classmethod
    def list(cls, request: ListTopBannersRequest):
        with cls.channel:
            stub = TopBannerStub(cls.channel)
            response: ListTopBannersResponse = stub.ListTopBanners(request)

            return response

    @classmethod
    def edit(cls, request: EditTopBannerRequest):
        with cls.channel:
            stub = TopBannerStub(cls.channel)
            response: EditTopBannerResponse = stub.EditTopBanner(request)
            return response.banner

    @classmethod
    def create(cls, request: CreateTopBannerRequest):
        with cls.channel:
            stub = TopBannerStub(cls.channel)
            response: CreateTopBannerResponse = stub.CreateTopBanner(request)
            return response.banner
