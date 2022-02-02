# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/logistics/shipping_notice_log/shipping_notice_log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/logistics/shipping_notice_log/shipping_notice_log.proto',
  package='shippingnoticelog',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>protos/logistics/shipping_notice_log/shipping_notice_log.proto\x12\x11shippingnoticelog\x1a\x1bgoogle/protobuf/empty.proto\"\xb5\x01\n\x11ShippingNoticeLog\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tuser_uuid\x18\x02 \x01(\t\x12\x15\n\ruser_username\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\t\x12\x12\n\nfield_name\x18\x06 \x01(\t\x12\x0e\n\x06\x62\x65\x66ore\x18\x07 \x01(\t\x12\r\n\x05\x61\x66ter\x18\x08 \x01(\t\x12\x0e\n\x06notice\x18\t \x01(\x03\"\x1e\n\x1cShippingNoticeLogListRequest\".\n ShippingNoticeLogRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xe4\x03\n\x1bShippingNoticeLogController\x12\x61\n\x04List\x12/.shippingnoticelog.ShippingNoticeLogListRequest\x1a$.shippingnoticelog.ShippingNoticeLog\"\x00\x30\x01\x12V\n\x06\x43reate\x12$.shippingnoticelog.ShippingNoticeLog\x1a$.shippingnoticelog.ShippingNoticeLog\"\x00\x12g\n\x08Retrieve\x12\x33.shippingnoticelog.ShippingNoticeLogRetrieveRequest\x1a$.shippingnoticelog.ShippingNoticeLog\"\x00\x12V\n\x06Update\x12$.shippingnoticelog.ShippingNoticeLog\x1a$.shippingnoticelog.ShippingNoticeLog\"\x00\x12I\n\x07\x44\x65stroy\x12$.shippingnoticelog.ShippingNoticeLog\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SHIPPINGNOTICELOG = _descriptor.Descriptor(
  name='ShippingNoticeLog',
  full_name='shippingnoticelog.ShippingNoticeLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='shippingnoticelog.ShippingNoticeLog.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_uuid', full_name='shippingnoticelog.ShippingNoticeLog.user_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_username', full_name='shippingnoticelog.ShippingNoticeLog.user_username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='shippingnoticelog.ShippingNoticeLog.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='shippingnoticelog.ShippingNoticeLog.created_at', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_name', full_name='shippingnoticelog.ShippingNoticeLog.field_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='before', full_name='shippingnoticelog.ShippingNoticeLog.before', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='after', full_name='shippingnoticelog.ShippingNoticeLog.after', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notice', full_name='shippingnoticelog.ShippingNoticeLog.notice', index=8,
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
  serialized_start=115,
  serialized_end=296,
)


_SHIPPINGNOTICELOGLISTREQUEST = _descriptor.Descriptor(
  name='ShippingNoticeLogListRequest',
  full_name='shippingnoticelog.ShippingNoticeLogListRequest',
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
  serialized_start=298,
  serialized_end=328,
)


_SHIPPINGNOTICELOGRETRIEVEREQUEST = _descriptor.Descriptor(
  name='ShippingNoticeLogRetrieveRequest',
  full_name='shippingnoticelog.ShippingNoticeLogRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='shippingnoticelog.ShippingNoticeLogRetrieveRequest.id', index=0,
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
  serialized_start=330,
  serialized_end=376,
)

DESCRIPTOR.message_types_by_name['ShippingNoticeLog'] = _SHIPPINGNOTICELOG
DESCRIPTOR.message_types_by_name['ShippingNoticeLogListRequest'] = _SHIPPINGNOTICELOGLISTREQUEST
DESCRIPTOR.message_types_by_name['ShippingNoticeLogRetrieveRequest'] = _SHIPPINGNOTICELOGRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShippingNoticeLog = _reflection.GeneratedProtocolMessageType('ShippingNoticeLog', (_message.Message,), {
  'DESCRIPTOR' : _SHIPPINGNOTICELOG,
  '__module__' : 'protos.logistics.shipping_notice_log.shipping_notice_log_pb2'
  # @@protoc_insertion_point(class_scope:shippingnoticelog.ShippingNoticeLog)
  })
_sym_db.RegisterMessage(ShippingNoticeLog)

ShippingNoticeLogListRequest = _reflection.GeneratedProtocolMessageType('ShippingNoticeLogListRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHIPPINGNOTICELOGLISTREQUEST,
  '__module__' : 'protos.logistics.shipping_notice_log.shipping_notice_log_pb2'
  # @@protoc_insertion_point(class_scope:shippingnoticelog.ShippingNoticeLogListRequest)
  })
_sym_db.RegisterMessage(ShippingNoticeLogListRequest)

ShippingNoticeLogRetrieveRequest = _reflection.GeneratedProtocolMessageType('ShippingNoticeLogRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHIPPINGNOTICELOGRETRIEVEREQUEST,
  '__module__' : 'protos.logistics.shipping_notice_log.shipping_notice_log_pb2'
  # @@protoc_insertion_point(class_scope:shippingnoticelog.ShippingNoticeLogRetrieveRequest)
  })
_sym_db.RegisterMessage(ShippingNoticeLogRetrieveRequest)



_SHIPPINGNOTICELOGCONTROLLER = _descriptor.ServiceDescriptor(
  name='ShippingNoticeLogController',
  full_name='shippingnoticelog.ShippingNoticeLogController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=379,
  serialized_end=863,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='shippingnoticelog.ShippingNoticeLogController.List',
    index=0,
    containing_service=None,
    input_type=_SHIPPINGNOTICELOGLISTREQUEST,
    output_type=_SHIPPINGNOTICELOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='shippingnoticelog.ShippingNoticeLogController.Create',
    index=1,
    containing_service=None,
    input_type=_SHIPPINGNOTICELOG,
    output_type=_SHIPPINGNOTICELOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='shippingnoticelog.ShippingNoticeLogController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_SHIPPINGNOTICELOGRETRIEVEREQUEST,
    output_type=_SHIPPINGNOTICELOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='shippingnoticelog.ShippingNoticeLogController.Update',
    index=3,
    containing_service=None,
    input_type=_SHIPPINGNOTICELOG,
    output_type=_SHIPPINGNOTICELOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='shippingnoticelog.ShippingNoticeLogController.Destroy',
    index=4,
    containing_service=None,
    input_type=_SHIPPINGNOTICELOG,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHIPPINGNOTICELOGCONTROLLER)

DESCRIPTOR.services_by_name['ShippingNoticeLogController'] = _SHIPPINGNOTICELOGCONTROLLER

# @@protoc_insertion_point(module_scope)
