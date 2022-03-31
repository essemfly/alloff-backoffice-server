# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos.product import notification_pb2 as protos_dot_product_dot_notification__pb2


class NotificationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListNoti = channel.unary_unary(
                '/protos.Notification/ListNoti',
                request_serializer=protos_dot_product_dot_notification__pb2.ListNotiRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_notification__pb2.ListNotiResponse.FromString,
                )
        self.CreateNoti = channel.unary_unary(
                '/protos.Notification/CreateNoti',
                request_serializer=protos_dot_product_dot_notification__pb2.CreateNotiRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_notification__pb2.CreateNotiResponse.FromString,
                )
        self.SendNoti = channel.unary_unary(
                '/protos.Notification/SendNoti',
                request_serializer=protos_dot_product_dot_notification__pb2.SendNotiRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_notification__pb2.SendNotiResponse.FromString,
                )


class NotificationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListNoti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNoti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendNoti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotificationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListNoti': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNoti,
                    request_deserializer=protos_dot_product_dot_notification__pb2.ListNotiRequest.FromString,
                    response_serializer=protos_dot_product_dot_notification__pb2.ListNotiResponse.SerializeToString,
            ),
            'CreateNoti': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNoti,
                    request_deserializer=protos_dot_product_dot_notification__pb2.CreateNotiRequest.FromString,
                    response_serializer=protos_dot_product_dot_notification__pb2.CreateNotiResponse.SerializeToString,
            ),
            'SendNoti': grpc.unary_unary_rpc_method_handler(
                    servicer.SendNoti,
                    request_deserializer=protos_dot_product_dot_notification__pb2.SendNotiRequest.FromString,
                    response_serializer=protos_dot_product_dot_notification__pb2.SendNotiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.Notification', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Notification(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListNoti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Notification/ListNoti',
            protos_dot_product_dot_notification__pb2.ListNotiRequest.SerializeToString,
            protos_dot_product_dot_notification__pb2.ListNotiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateNoti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Notification/CreateNoti',
            protos_dot_product_dot_notification__pb2.CreateNotiRequest.SerializeToString,
            protos_dot_product_dot_notification__pb2.CreateNotiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendNoti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Notification/SendNoti',
            protos_dot_product_dot_notification__pb2.SendNotiRequest.SerializeToString,
            protos_dot_product_dot_notification__pb2.SendNotiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
