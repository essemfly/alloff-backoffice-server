from typing import List

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from gen.pyalloff import package_pb2, package_pb2_grpc
from office.services.base import GrpcService


class PackageService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(cls) -> List[dict]:
        request = package_pb2.PackageListRequest()
        with cls.channel:
            return package_pb2_grpc.PackageControllerStub(cls.channel).List(request)

    @classmethod
    def retrieve(cls, id):
        request = package_pb2.PackageRetrieveRequest(id=id)
        with cls.channel:
            return package_pb2_grpc.PackageControllerStub(cls.channel).Retrieve(request)
