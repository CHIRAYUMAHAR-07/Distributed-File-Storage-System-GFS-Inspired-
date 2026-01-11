import grpc
import storage_pb2, storage_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = storage_pb2_grpc.MetadataServiceStub(channel)
resp = stub.AllocateChunk(storage_pb2.AllocateChunkRequest(file_path="/foo"))
print(resp.chunk_id, resp.replica_nodes)