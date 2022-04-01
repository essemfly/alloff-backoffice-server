from alloff_backoffice_server.settings import PRODUCT_SERVER_URL
from office.services.base import GrpcService
from gen.pyalloff import notification_pb2, notification_pb2_grpc


class NotificationService(GrpcService):
    url = PRODUCT_SERVER_URL

    @classmethod
    def list(cls, request: notification_pb2.ListNotiRequest):
        with cls.channel:
            stub = notification_pb2_grpc.NotificationStub(cls.channel)
            response: notification_pb2_grpc.ListProductGroupsResponse = stub.ListNoti(
                request
            )

            return response

    @classmethod
    def create(cls, request: notification_pb2.CreateNotiRequest):
        with cls.channel:
            stub = notification_pb2_grpc.NotificationStub(cls.channel)
            response: notification_pb2_grpc.CreateNotiResponse = stub.CreateNoti(
                request
            )

            return response.succeeded

    @classmethod
    def send(cls, request: notification_pb2.SendNotiRequest):
        with cls.channel:
            stub = notification_pb2_grpc.NotificationStub(cls.channel)
            response: notification_pb2.SendNotiResponse = stub.SendNoti(request)

            return response.is_sent
