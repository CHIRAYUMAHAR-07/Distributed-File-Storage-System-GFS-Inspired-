"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import storage_pb2 as storage__pb2

GRPC_GENERATED_VERSION = '1.76.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + ' but the generated code in storage_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MetadataServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AllocateChunk = channel.unary_unary(
                '/storage.MetadataService/AllocateChunk',
                request_serializer=storage__pb2.AllocateChunkRequest.SerializeToString,
                response_deserializer=storage__pb2.AllocateChunkResponse.FromString,
                _registered_method=True)
        self.GetChunkLocations = channel.unary_unary(
                '/storage.MetadataService/GetChunkLocations',
                request_serializer=storage__pb2.GetChunkLocationsRequest.SerializeToString,
                response_deserializer=storage__pb2.GetChunkLocationsResponse.FromString,
                _registered_method=True)
        self.Heartbeat = channel.unary_unary(
                '/storage.MetadataService/Heartbeat',
                request_serializer=storage__pb2.HeartbeatRequest.SerializeToString,
                response_deserializer=storage__pb2.HeartbeatResponse.FromString,
                _registered_method=True)


class MetadataServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AllocateChunk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChunkLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Heartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetadataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AllocateChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.AllocateChunk,
                    request_deserializer=storage__pb2.AllocateChunkRequest.FromString,
                    response_serializer=storage__pb2.AllocateChunkResponse.SerializeToString,
            ),
            'GetChunkLocations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChunkLocations,
                    request_deserializer=storage__pb2.GetChunkLocationsRequest.FromString,
                    response_serializer=storage__pb2.GetChunkLocationsResponse.SerializeToString,
            ),
            'Heartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.Heartbeat,
                    request_deserializer=storage__pb2.HeartbeatRequest.FromString,
                    response_serializer=storage__pb2.HeartbeatResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'storage.MetadataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('storage.MetadataService', rpc_method_handlers)

    
class MetadataService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AllocateChunk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/storage.MetadataService/AllocateChunk',
            storage__pb2.AllocateChunkRequest.SerializeToString,
            storage__pb2.AllocateChunkResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetChunkLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/storage.MetadataService/GetChunkLocations',
            storage__pb2.GetChunkLocationsRequest.SerializeToString,
            storage__pb2.GetChunkLocationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Heartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/storage.MetadataService/Heartbeat',
            storage__pb2.HeartbeatRequest.SerializeToString,
            storage__pb2.HeartbeatResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
