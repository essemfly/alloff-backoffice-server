# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos.product import exhibition_pb2 as protos_dot_product_dot_exhibition__pb2


class ExhibitionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetExhibition = channel.unary_unary(
                '/grpcServer.Exhibition/GetExhibition',
                request_serializer=protos_dot_product_dot_exhibition__pb2.GetExhibitionRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_exhibition__pb2.GetExhibitionResponse.FromString,
                )
        self.ListExhibitions = channel.unary_unary(
                '/grpcServer.Exhibition/ListExhibitions',
                request_serializer=protos_dot_product_dot_exhibition__pb2.ListExhibitionsRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_exhibition__pb2.ListExhibitionsResponse.FromString,
                )
        self.EditExhibition = channel.unary_unary(
                '/grpcServer.Exhibition/EditExhibition',
                request_serializer=protos_dot_product_dot_exhibition__pb2.EditExhibitionRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_exhibition__pb2.EditExhibitionResponse.FromString,
                )
        self.CreateExhibition = channel.unary_unary(
                '/grpcServer.Exhibition/CreateExhibition',
                request_serializer=protos_dot_product_dot_exhibition__pb2.CreateExhibitionRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_exhibition__pb2.CreateExhibitionResponse.FromString,
                )


class ExhibitionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetExhibition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExhibitions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditExhibition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateExhibition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExhibitionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetExhibition': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExhibition,
                    request_deserializer=protos_dot_product_dot_exhibition__pb2.GetExhibitionRequest.FromString,
                    response_serializer=protos_dot_product_dot_exhibition__pb2.GetExhibitionResponse.SerializeToString,
            ),
            'ListExhibitions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExhibitions,
                    request_deserializer=protos_dot_product_dot_exhibition__pb2.ListExhibitionsRequest.FromString,
                    response_serializer=protos_dot_product_dot_exhibition__pb2.ListExhibitionsResponse.SerializeToString,
            ),
            'EditExhibition': grpc.unary_unary_rpc_method_handler(
                    servicer.EditExhibition,
                    request_deserializer=protos_dot_product_dot_exhibition__pb2.EditExhibitionRequest.FromString,
                    response_serializer=protos_dot_product_dot_exhibition__pb2.EditExhibitionResponse.SerializeToString,
            ),
            'CreateExhibition': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateExhibition,
                    request_deserializer=protos_dot_product_dot_exhibition__pb2.CreateExhibitionRequest.FromString,
                    response_serializer=protos_dot_product_dot_exhibition__pb2.CreateExhibitionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcServer.Exhibition', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Exhibition(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetExhibition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcServer.Exhibition/GetExhibition',
            protos_dot_product_dot_exhibition__pb2.GetExhibitionRequest.SerializeToString,
            protos_dot_product_dot_exhibition__pb2.GetExhibitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListExhibitions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcServer.Exhibition/ListExhibitions',
            protos_dot_product_dot_exhibition__pb2.ListExhibitionsRequest.SerializeToString,
            protos_dot_product_dot_exhibition__pb2.ListExhibitionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EditExhibition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcServer.Exhibition/EditExhibition',
            protos_dot_product_dot_exhibition__pb2.EditExhibitionRequest.SerializeToString,
            protos_dot_product_dot_exhibition__pb2.EditExhibitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateExhibition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcServer.Exhibition/CreateExhibition',
            protos_dot_product_dot_exhibition__pb2.CreateExhibitionRequest.SerializeToString,
            protos_dot_product_dot_exhibition__pb2.CreateExhibitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
