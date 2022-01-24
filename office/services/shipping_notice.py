from typing import List

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from logistics.protos.shipping_notice_proto import (
    shipping_notice_pb2,
    shipping_notice_pb2_grpc,
)
from office.services.base import GrpcService


class ShippingNoticeService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL

    @classmethod
    def list(cls) -> List[dict]:
        request = shipping_notice_pb2.ShippingNoticeListRequest()
        with cls.channel:
            stub = shipping_notice_pb2_grpc.ShippingNoticeControllerStub(cls.channel)
            response = stub.List(request)
            return cls.to_array(response)
