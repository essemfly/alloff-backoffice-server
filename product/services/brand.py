from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService
from protos.product import brand_pb2, brand_pb2_grpc

from django_grpc_framework import generics


class BrandService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def list(cls):
        request = brand_pb2.ListBrandRequest()
        with cls.channel:
            stub = brand_pb2_grpc.BrandStub(cls.channel)
            response: brand_pb2.ListBrandResponse = stub.ListBrand(request)

            return response.brands

    @classmethod
    def create(cls, request: brand_pb2.CreateBrandRequest):
        with cls.channel:
            stub = brand_pb2_grpc.BrandStub(cls.channel)
            response: brand_pb2.CreateBrandResponse = stub.CreateBrand(request)

            return response.brand
