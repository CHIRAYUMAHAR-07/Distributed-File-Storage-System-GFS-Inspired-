"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'storage.proto'
)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rstorage.proto\x12\x07storage\")\n\x14\x41llocateChunkRequest\x12\x11\n\tfile_path\x18\x01 \x01(\t\"@\n\x15\x41llocateChunkResponse\x12\x10\n\x08\x63hunk_id\x18\x01 \x01(\t\x12\x15\n\rreplica_nodes\x18\x02 \x03(\t\",\n\x18GetChunkLocationsRequest\x12\x10\n\x08\x63hunk_id\x18\x01 \x01(\t\"2\n\x19GetChunkLocationsResponse\x12\x15\n\rreplica_nodes\x18\x01 \x03(\t\"#\n\x10HeartbeatRequest\x12\x0f\n\x07node_id\x18\x01 \x01(\t\"\x1f\n\x11HeartbeatResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x32\x81\x02\n\x0fMetadataService\x12N\n\rAllocateChunk\x12\x1d.storage.AllocateChunkRequest\x1a\x1e.storage.AllocateChunkResponse\x12Z\n\x11GetChunkLocations\x12!.storage.GetChunkLocationsRequest\x1a\".storage.GetChunkLocationsResponse\x12\x42\n\tHeartbeat\x12\x19.storage.HeartbeatRequest\x1a\x1a.storage.HeartbeatResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'storage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ALLOCATECHUNKREQUEST']._serialized_start=26
  _globals['_ALLOCATECHUNKREQUEST']._serialized_end=67
  _globals['_ALLOCATECHUNKRESPONSE']._serialized_start=69
  _globals['_ALLOCATECHUNKRESPONSE']._serialized_end=133
  _globals['_GETCHUNKLOCATIONSREQUEST']._serialized_start=135
  _globals['_GETCHUNKLOCATIONSREQUEST']._serialized_end=179
  _globals['_GETCHUNKLOCATIONSRESPONSE']._serialized_start=181
  _globals['_GETCHUNKLOCATIONSRESPONSE']._serialized_end=231
  _globals['_HEARTBEATREQUEST']._serialized_start=233
  _globals['_HEARTBEATREQUEST']._serialized_end=268
  _globals['_HEARTBEATRESPONSE']._serialized_start=270
  _globals['_HEARTBEATRESPONSE']._serialized_end=301
  _globals['_METADATASERVICE']._serialized_start=304
  _globals['_METADATASERVICE']._serialized_end=561
