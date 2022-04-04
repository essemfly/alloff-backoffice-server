from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService
from gen.pyalloff import product_pb2, product_pb2_grpc


class ProductService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def list(cls, request: product_pb2.ListProductsRequest):
        with cls.channel:
            stub = product_pb2_grpc.ProductStub(cls.channel)
            response: product_pb2.ListProductsResponse = stub.ListProducts(request)

            return response

    @classmethod
    def create(cls, request: product_pb2.CreateProductRequest):
        with cls.channel:
            stub = product_pb2_grpc.ProductStub(cls.channel)
            response: product_pb2.CreateProductResponse = stub.CreateProduct(request)

            return response.product

    @classmethod
    def get(cls, request: product_pb2.GetProductRequest):
        with cls.channel:
            stub = product_pb2_grpc.ProductStub(cls.channel)
            response: product_pb2.GetProductResponse = stub.GetProduct(request)

            return response.product

    @classmethod
    def edit(cls, request: product_pb2.EditProductRequest):
        with cls.channel:
            stub = product_pb2_grpc.ProductStub(cls.channel)
            response: product_pb2.EditProductResponse = stub.EditProduct(request)
            return response.product
