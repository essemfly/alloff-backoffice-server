# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos.product import brand_pb2 as protos_dot_product_dot_brand__pb2


class BrandStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListBrand = channel.unary_unary(
                '/grpcServer.Brand/ListBrand',
                request_serializer=protos_dot_product_dot_brand__pb2.ListBrandRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_brand__pb2.ListBrandResponse.FromString,
                )
        self.CreateBrand = channel.unary_unary(
                '/grpcServer.Brand/CreateBrand',
                request_serializer=protos_dot_product_dot_brand__pb2.CreateBrandRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_brand__pb2.CreateBrandResponse.FromString,
                )


class BrandServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListBrand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBrand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BrandServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListBrand': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBrand,
                    request_deserializer=protos_dot_product_dot_brand__pb2.ListBrandRequest.FromString,
                    response_serializer=protos_dot_product_dot_brand__pb2.ListBrandResponse.SerializeToString,
            ),
            'CreateBrand': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBrand,
                    request_deserializer=protos_dot_product_dot_brand__pb2.CreateBrandRequest.FromString,
                    response_serializer=protos_dot_product_dot_brand__pb2.CreateBrandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcServer.Brand', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Brand(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListBrand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcServer.Brand/ListBrand',
            protos_dot_product_dot_brand__pb2.ListBrandRequest.SerializeToString,
            protos_dot_product_dot_brand__pb2.ListBrandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateBrand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcServer.Brand/CreateBrand',
            protos_dot_product_dot_brand__pb2.CreateBrandRequest.SerializeToString,
            protos_dot_product_dot_brand__pb2.CreateBrandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
