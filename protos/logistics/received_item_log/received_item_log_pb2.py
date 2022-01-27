# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/logistics/received_item_log/received_item_log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/logistics/received_item_log/received_item_log.proto',
  package='receiveditemlog',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:protos/logistics/received_item_log/received_item_log.proto\x12\x0freceiveditemlog\x1a\x1bgoogle/protobuf/empty.proto\"\xba\x01\n\x0fReceivedItemLog\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tuser_uuid\x18\x02 \x01(\t\x12\x15\n\ruser_username\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\t\x12\x12\n\nfield_name\x18\x06 \x01(\t\x12\x0e\n\x06\x62\x65\x66ore\x18\x07 \x01(\t\x12\r\n\x05\x61\x66ter\x18\x08 \x01(\t\x12\x15\n\rreceived_item\x18\t \x01(\x03\"\x1c\n\x1aReceivedItemLogListRequest\",\n\x1eReceivedItemLogRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xbe\x03\n\x19ReceivedItemLogController\x12Y\n\x04List\x12+.receiveditemlog.ReceivedItemLogListRequest\x1a .receiveditemlog.ReceivedItemLog\"\x00\x30\x01\x12N\n\x06\x43reate\x12 .receiveditemlog.ReceivedItemLog\x1a .receiveditemlog.ReceivedItemLog\"\x00\x12_\n\x08Retrieve\x12/.receiveditemlog.ReceivedItemLogRetrieveRequest\x1a .receiveditemlog.ReceivedItemLog\"\x00\x12N\n\x06Update\x12 .receiveditemlog.ReceivedItemLog\x1a .receiveditemlog.ReceivedItemLog\"\x00\x12\x45\n\x07\x44\x65stroy\x12 .receiveditemlog.ReceivedItemLog\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_RECEIVEDITEMLOG = _descriptor.Descriptor(
  name='ReceivedItemLog',
  full_name='receiveditemlog.ReceivedItemLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='receiveditemlog.ReceivedItemLog.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_uuid', full_name='receiveditemlog.ReceivedItemLog.user_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_username', full_name='receiveditemlog.ReceivedItemLog.user_username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='receiveditemlog.ReceivedItemLog.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='receiveditemlog.ReceivedItemLog.created_at', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_name', full_name='receiveditemlog.ReceivedItemLog.field_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='before', full_name='receiveditemlog.ReceivedItemLog.before', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='after', full_name='receiveditemlog.ReceivedItemLog.after', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='received_item', full_name='receiveditemlog.ReceivedItemLog.received_item', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=295,
)


_RECEIVEDITEMLOGLISTREQUEST = _descriptor.Descriptor(
  name='ReceivedItemLogListRequest',
  full_name='receiveditemlog.ReceivedItemLogListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=325,
)


_RECEIVEDITEMLOGRETRIEVEREQUEST = _descriptor.Descriptor(
  name='ReceivedItemLogRetrieveRequest',
  full_name='receiveditemlog.ReceivedItemLogRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='receiveditemlog.ReceivedItemLogRetrieveRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=371,
)

DESCRIPTOR.message_types_by_name['ReceivedItemLog'] = _RECEIVEDITEMLOG
DESCRIPTOR.message_types_by_name['ReceivedItemLogListRequest'] = _RECEIVEDITEMLOGLISTREQUEST
DESCRIPTOR.message_types_by_name['ReceivedItemLogRetrieveRequest'] = _RECEIVEDITEMLOGRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReceivedItemLog = _reflection.GeneratedProtocolMessageType('ReceivedItemLog', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDITEMLOG,
  '__module__' : 'protos.logistics.received_item_log.received_item_log_pb2'
  # @@protoc_insertion_point(class_scope:receiveditemlog.ReceivedItemLog)
  })
_sym_db.RegisterMessage(ReceivedItemLog)

ReceivedItemLogListRequest = _reflection.GeneratedProtocolMessageType('ReceivedItemLogListRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDITEMLOGLISTREQUEST,
  '__module__' : 'protos.logistics.received_item_log.received_item_log_pb2'
  # @@protoc_insertion_point(class_scope:receiveditemlog.ReceivedItemLogListRequest)
  })
_sym_db.RegisterMessage(ReceivedItemLogListRequest)

ReceivedItemLogRetrieveRequest = _reflection.GeneratedProtocolMessageType('ReceivedItemLogRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDITEMLOGRETRIEVEREQUEST,
  '__module__' : 'protos.logistics.received_item_log.received_item_log_pb2'
  # @@protoc_insertion_point(class_scope:receiveditemlog.ReceivedItemLogRetrieveRequest)
  })
_sym_db.RegisterMessage(ReceivedItemLogRetrieveRequest)



_RECEIVEDITEMLOGCONTROLLER = _descriptor.ServiceDescriptor(
  name='ReceivedItemLogController',
  full_name='receiveditemlog.ReceivedItemLogController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=374,
  serialized_end=820,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='receiveditemlog.ReceivedItemLogController.List',
    index=0,
    containing_service=None,
    input_type=_RECEIVEDITEMLOGLISTREQUEST,
    output_type=_RECEIVEDITEMLOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='receiveditemlog.ReceivedItemLogController.Create',
    index=1,
    containing_service=None,
    input_type=_RECEIVEDITEMLOG,
    output_type=_RECEIVEDITEMLOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='receiveditemlog.ReceivedItemLogController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_RECEIVEDITEMLOGRETRIEVEREQUEST,
    output_type=_RECEIVEDITEMLOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='receiveditemlog.ReceivedItemLogController.Update',
    index=3,
    containing_service=None,
    input_type=_RECEIVEDITEMLOG,
    output_type=_RECEIVEDITEMLOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='receiveditemlog.ReceivedItemLogController.Destroy',
    index=4,
    containing_service=None,
    input_type=_RECEIVEDITEMLOG,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECEIVEDITEMLOGCONTROLLER)

DESCRIPTOR.services_by_name['ReceivedItemLogController'] = _RECEIVEDITEMLOGCONTROLLER

# @@protoc_insertion_point(module_scope)
