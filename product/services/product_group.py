from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from gen.pyalloff import productGroup_pb2, productGroup_pb2_grpc
from office.services.base import GrpcService


class ProductGroupService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def get(cls, request: productGroup_pb2.GetProductGroupRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.ProductGroupMessage = stub.GetProductGroup(
                request
            )
            return response

    @classmethod
    def create(cls, request: productGroup_pb2.CreateProductGroupRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.ProductGroupMessage = (
                stub.CreateProductGroup(request)
            )
            return response

    @classmethod
    def list(cls, request: productGroup_pb2.ListProductGroupsRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.ListProductGroupsResponse = (
                stub.ListProductGroups(request)
            )
            return response

    @classmethod
    def edit(cls, request: productGroup_pb2.EditProductGroupRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.ProductGroupMessage = stub.EditProductGroup(
                request
            )
            return response

    @classmethod
    def push(cls, request: productGroup_pb2.PushProductInPgRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.ProductGroupMessage = (
                stub.PushProductsInProductGroup(request)
            )
            return response

    @classmethod
    def update(cls, request: productGroup_pb2.UpdateProductsInPgRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.ProductGroupMessage = (
                stub.UpdateProductsInProductGroup(request)
            )
            return response

    @classmethod
    def remove(cls, request: productGroup_pb2.RemoveProductInPgRequest):
        with cls.channel:
            stub = productGroup_pb2_grpc.ProductGroupStub(cls.channel)
            response: productGroup_pb2.ProductGroupMessage = (
                stub.RemoveProductInProductGroup(request)
            )
            return response
