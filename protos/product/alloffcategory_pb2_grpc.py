# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos.product import alloffcategory_pb2 as protos_dot_product_dot_alloffcategory__pb2


class AlloffCategoryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAlloffCategory = channel.unary_unary(
                '/grpcServer.AlloffCategory/ListAlloffCategory',
                request_serializer=protos_dot_product_dot_alloffcategory__pb2.ListAlloffCategoryRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_alloffcategory__pb2.ListAlloffCategoryResponse.FromString,
                )


class AlloffCategoryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListAlloffCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlloffCategoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListAlloffCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAlloffCategory,
                    request_deserializer=protos_dot_product_dot_alloffcategory__pb2.ListAlloffCategoryRequest.FromString,
                    response_serializer=protos_dot_product_dot_alloffcategory__pb2.ListAlloffCategoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcServer.AlloffCategory', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AlloffCategory(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListAlloffCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcServer.AlloffCategory/ListAlloffCategory',
            protos_dot_product_dot_alloffcategory__pb2.ListAlloffCategoryRequest.SerializeToString,
            protos_dot_product_dot_alloffcategory__pb2.ListAlloffCategoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
