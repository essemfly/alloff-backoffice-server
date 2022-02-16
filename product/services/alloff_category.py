from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService

from protos.product.alloffcategory_pb2 import (
    ListAlloffCategoryRequest,
    ListAlloffCategoryResponse,
)

from protos.product.alloffcategory_pb2_grpc import AlloffCategoryStub


class AlloffCategoryService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def list(cls, request: ListAlloffCategoryRequest):
        with cls.channel:
            stub = AlloffCategoryStub(cls.channel)
            response: ListAlloffCategoryResponse = stub.ListAlloffCategory(request)

            return response
