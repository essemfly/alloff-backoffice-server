from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService
from protos.product import productGroup_pb2, productGroup_pb2_grpc


class ProductGroupService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def list(cls):
        request = productGroup_pb2.ListProductGroupsRequest()
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.ListProductGroupsResponse = (
                stub.ListProductGroups(request)
            )

            return response.pgs

    @classmethod
    def create(cls, request: productGroup_pb2.CreateProductGroupRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.CreateProductGroupResponse = (
                stub.CreateProductGroup(request)
            )

            return response.pg

    @classmethod
    def get(cls, request: productGroup_pb2.GetProductGroupRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.GetProductGroupResponse = stub.GetProductGroup(
                request
            )

            return response.pg

    @classmethod
    def edit(cls, request: productGroup_pb2.EditProductGroupRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.EditProductGroupResponse = stub.EditProductGroup(
                request
            )
            return response.pg

    @classmethod
    def push(cls, request: productGroup_pb2.PushProductsRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.PushProductsResponse = stub.PushProducts(request)
            return response.pg
