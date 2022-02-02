# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.logistics.package_log import package_log_pb2 as protos_dot_logistics_dot_package__log_dot_package__log__pb2


class PackageLogControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/package_log.PackageLogController/List',
                request_serializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLogListRequest.SerializeToString,
                response_deserializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
                )
        self.Create = channel.unary_unary(
                '/package_log.PackageLogController/Create',
                request_serializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
                response_deserializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/package_log.PackageLogController/Retrieve',
                request_serializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLogRetrieveRequest.SerializeToString,
                response_deserializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
                )
        self.Update = channel.unary_unary(
                '/package_log.PackageLogController/Update',
                request_serializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
                response_deserializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/package_log.PackageLogController/Destroy',
                request_serializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class PackageLogControllerServicer(object):
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


def add_PackageLogControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLogListRequest.FromString,
                    response_serializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
                    response_serializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLogRetrieveRequest.FromString,
                    response_serializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
                    response_serializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'package_log.PackageLogController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PackageLogController(object):
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
        return grpc.experimental.unary_stream(request, target, '/package_log.PackageLogController/List',
            protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLogListRequest.SerializeToString,
            protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/package_log.PackageLogController/Create',
            protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
            protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/package_log.PackageLogController/Retrieve',
            protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLogRetrieveRequest.SerializeToString,
            protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/package_log.PackageLogController/Update',
            protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
            protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/package_log.PackageLogController/Destroy',
            protos_dot_logistics_dot_package__log_dot_package__log__pb2.PackageLog.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
