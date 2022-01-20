# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from logistics.protos.package_proto import package_pb2 as logistics_dot_protos_dot_package__proto_dot_package__pb2


class PackageControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/package.PackageController/List',
                request_serializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.PackageListRequest.SerializeToString,
                response_deserializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
                )
        self.Create = channel.unary_unary(
                '/package.PackageController/Create',
                request_serializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
                response_deserializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/package.PackageController/Retrieve',
                request_serializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.PackageRetrieveRequest.SerializeToString,
                response_deserializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
                )
        self.Update = channel.unary_unary(
                '/package.PackageController/Update',
                request_serializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
                response_deserializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/package.PackageController/Destroy',
                request_serializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class PackageControllerServicer(object):
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


def add_PackageControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.PackageListRequest.FromString,
                    response_serializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
                    response_serializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.PackageRetrieveRequest.FromString,
                    response_serializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
                    response_serializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'package.PackageController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PackageController(object):
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
        return grpc.experimental.unary_stream(request, target, '/package.PackageController/List',
            logistics_dot_protos_dot_package__proto_dot_package__pb2.PackageListRequest.SerializeToString,
            logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/package.PackageController/Create',
            logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
            logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/package.PackageController/Retrieve',
            logistics_dot_protos_dot_package__proto_dot_package__pb2.PackageRetrieveRequest.SerializeToString,
            logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/package.PackageController/Update',
            logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
            logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/package.PackageController/Destroy',
            logistics_dot_protos_dot_package__proto_dot_package__pb2.Package.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
