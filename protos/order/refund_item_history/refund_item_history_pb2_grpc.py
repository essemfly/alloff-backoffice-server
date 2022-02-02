# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.order.refund_item_history import refund_item_history_pb2 as protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2


class RefundItemHistoryControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/refunditemhistory.RefundItemHistoryController/List',
                request_serializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistoryListRequest.SerializeToString,
                response_deserializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
                )
        self.Create = channel.unary_unary(
                '/refunditemhistory.RefundItemHistoryController/Create',
                request_serializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
                response_deserializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/refunditemhistory.RefundItemHistoryController/Retrieve',
                request_serializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistoryRetrieveRequest.SerializeToString,
                response_deserializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
                )
        self.Update = channel.unary_unary(
                '/refunditemhistory.RefundItemHistoryController/Update',
                request_serializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
                response_deserializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/refunditemhistory.RefundItemHistoryController/Destroy',
                request_serializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class RefundItemHistoryControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RefundItemHistoryControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistoryListRequest.FromString,
                    response_serializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
                    response_serializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistoryRetrieveRequest.FromString,
                    response_serializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
                    response_serializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'refunditemhistory.RefundItemHistoryController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RefundItemHistoryController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/refunditemhistory.RefundItemHistoryController/List',
            protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistoryListRequest.SerializeToString,
            protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/refunditemhistory.RefundItemHistoryController/Create',
            protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
            protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/refunditemhistory.RefundItemHistoryController/Retrieve',
            protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistoryRetrieveRequest.SerializeToString,
            protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/refunditemhistory.RefundItemHistoryController/Update',
            protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
            protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/refunditemhistory.RefundItemHistoryController/Destroy',
            protos_dot_order_dot_refund__item__history_dot_refund__item__history__pb2.RefundItemHistory.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
