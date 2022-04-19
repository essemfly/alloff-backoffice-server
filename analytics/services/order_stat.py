from typing import List

from alloff_backoffice_server.settings import GRPC_LOGISTICS_SERVER_URL
from gen.pyalloff import order_analytics_pb2, order_analytics_pb2_grpc
from office.services.base import GrpcService, grpc_request


class OrderStatService(GrpcService):
    url = GRPC_LOGISTICS_SERVER_URL
    stub = order_analytics_pb2_grpc.OrderAnalyticsControllerStub

    @classmethod
    @grpc_request(
        order_analytics_pb2.DailyOrderStatRequest,
    )
    def DailyOrderStat(
        cls,
        date_from: str = None,
        date_to: str = None,
    ) -> List[dict]:
        pass
