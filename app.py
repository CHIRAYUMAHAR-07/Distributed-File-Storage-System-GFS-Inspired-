import grpc
from concurrent import futures

import storage_pb2
import storage_pb2_grpc

from placement import PlacementManager
from failure_detector import FailureDetector


class MetadataService(storage_pb2_grpc.MetadataServiceServicer):
    def __init__(self):
        self.placement = PlacementManager()
        self.failure_detector = FailureDetector()

    def RegisterChunk(self, request, context):
        self.placement.register_chunk(request.chunk_id, request.server_id)
        return storage_pb2.Ack(ok=True)

    def GetChunkLocations(self, request, context):
        locations = self.placement.get_chunk_locations(request.chunk_id)
        return storage_pb2.ChunkLocations(servers=locations)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    storage_pb2_grpc.add_MetadataServiceServicer_to_server(
        MetadataService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Metadata service running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
