# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos.product import hometab_pb2 as protos_dot_product_dot_hometab__pb2


class HomeTabItemStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetHomeTabItem = channel.unary_unary(
                '/protos.HomeTabItem/GetHomeTabItem',
                request_serializer=protos_dot_product_dot_hometab__pb2.GetHomeTabItemRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_hometab__pb2.GetHomeTabItemResponse.FromString,
                )
        self.ListHomeTabItems = channel.unary_unary(
                '/protos.HomeTabItem/ListHomeTabItems',
                request_serializer=protos_dot_product_dot_hometab__pb2.ListHomeTabItemsRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_hometab__pb2.ListHomeTabItemsResponse.FromString,
                )
        self.EditHomeTabItem = channel.unary_unary(
                '/protos.HomeTabItem/EditHomeTabItem',
                request_serializer=protos_dot_product_dot_hometab__pb2.EditHomeTabItemRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_hometab__pb2.EditHomeTabItemResponse.FromString,
                )
        self.CreateHomeTabItem = channel.unary_unary(
                '/protos.HomeTabItem/CreateHomeTabItem',
                request_serializer=protos_dot_product_dot_hometab__pb2.CreateHomeTabItemRequest.SerializeToString,
                response_deserializer=protos_dot_product_dot_hometab__pb2.CreateHomeTabItemResponse.FromString,
                )


class HomeTabItemServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetHomeTabItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListHomeTabItems(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditHomeTabItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateHomeTabItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HomeTabItemServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetHomeTabItem': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHomeTabItem,
                    request_deserializer=protos_dot_product_dot_hometab__pb2.GetHomeTabItemRequest.FromString,
                    response_serializer=protos_dot_product_dot_hometab__pb2.GetHomeTabItemResponse.SerializeToString,
            ),
            'ListHomeTabItems': grpc.unary_unary_rpc_method_handler(
                    servicer.ListHomeTabItems,
                    request_deserializer=protos_dot_product_dot_hometab__pb2.ListHomeTabItemsRequest.FromString,
                    response_serializer=protos_dot_product_dot_hometab__pb2.ListHomeTabItemsResponse.SerializeToString,
            ),
            'EditHomeTabItem': grpc.unary_unary_rpc_method_handler(
                    servicer.EditHomeTabItem,
                    request_deserializer=protos_dot_product_dot_hometab__pb2.EditHomeTabItemRequest.FromString,
                    response_serializer=protos_dot_product_dot_hometab__pb2.EditHomeTabItemResponse.SerializeToString,
            ),
            'CreateHomeTabItem': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateHomeTabItem,
                    request_deserializer=protos_dot_product_dot_hometab__pb2.CreateHomeTabItemRequest.FromString,
                    response_serializer=protos_dot_product_dot_hometab__pb2.CreateHomeTabItemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.HomeTabItem', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HomeTabItem(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetHomeTabItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.HomeTabItem/GetHomeTabItem',
            protos_dot_product_dot_hometab__pb2.GetHomeTabItemRequest.SerializeToString,
            protos_dot_product_dot_hometab__pb2.GetHomeTabItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListHomeTabItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.HomeTabItem/ListHomeTabItems',
            protos_dot_product_dot_hometab__pb2.ListHomeTabItemsRequest.SerializeToString,
            protos_dot_product_dot_hometab__pb2.ListHomeTabItemsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EditHomeTabItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.HomeTabItem/EditHomeTabItem',
            protos_dot_product_dot_hometab__pb2.EditHomeTabItemRequest.SerializeToString,
            protos_dot_product_dot_hometab__pb2.EditHomeTabItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateHomeTabItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.HomeTabItem/CreateHomeTabItem',
            protos_dot_product_dot_hometab__pb2.CreateHomeTabItemRequest.SerializeToString,
            protos_dot_product_dot_hometab__pb2.CreateHomeTabItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
