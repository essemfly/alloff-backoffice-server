# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/order/inventory_receipt_log/inventory_receipt_log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/order/inventory_receipt_log/inventory_receipt_log.proto',
  package='inventoryreceiptlog',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>protos/order/inventory_receipt_log/inventory_receipt_log.proto\x12\x13inventoryreceiptlog\x1a\x1bgoogle/protobuf/empty.proto\"\xeb\x01\n\x13InventoryReceiptLog\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tuser_uuid\x18\x02 \x01(\t\x12\x15\n\ruser_username\x18\x03 \x01(\t\x12\x18\n\x10received_item_id\x18\x04 \x01(\x05\x12\x1a\n\x12received_item_code\x18\x05 \x01(\t\x12\x14\n\x0cinventory_id\x18\x06 \x01(\x05\x12\x16\n\x0einventory_code\x18\x07 \x01(\t\x12\x12\n\ncreated_at\x18\x08 \x01(\t\x12\x12\n\norder_item\x18\t \x01(\x03\x12\x12\n\naction_log\x18\n \x01(\x03\" \n\x1eInventoryReceiptLogListRequest\"0\n\"InventoryReceiptLogRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\x8a\x04\n\x1dInventoryReceiptLogController\x12i\n\x04List\x12\x33.inventoryreceiptlog.InventoryReceiptLogListRequest\x1a(.inventoryreceiptlog.InventoryReceiptLog\"\x00\x30\x01\x12^\n\x06\x43reate\x12(.inventoryreceiptlog.InventoryReceiptLog\x1a(.inventoryreceiptlog.InventoryReceiptLog\"\x00\x12o\n\x08Retrieve\x12\x37.inventoryreceiptlog.InventoryReceiptLogRetrieveRequest\x1a(.inventoryreceiptlog.InventoryReceiptLog\"\x00\x12^\n\x06Update\x12(.inventoryreceiptlog.InventoryReceiptLog\x1a(.inventoryreceiptlog.InventoryReceiptLog\"\x00\x12M\n\x07\x44\x65stroy\x12(.inventoryreceiptlog.InventoryReceiptLog\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_INVENTORYRECEIPTLOG = _descriptor.Descriptor(
  name='InventoryReceiptLog',
  full_name='inventoryreceiptlog.InventoryReceiptLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inventoryreceiptlog.InventoryReceiptLog.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_uuid', full_name='inventoryreceiptlog.InventoryReceiptLog.user_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_username', full_name='inventoryreceiptlog.InventoryReceiptLog.user_username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='received_item_id', full_name='inventoryreceiptlog.InventoryReceiptLog.received_item_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='received_item_code', full_name='inventoryreceiptlog.InventoryReceiptLog.received_item_code', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inventory_id', full_name='inventoryreceiptlog.InventoryReceiptLog.inventory_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inventory_code', full_name='inventoryreceiptlog.InventoryReceiptLog.inventory_code', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='inventoryreceiptlog.InventoryReceiptLog.created_at', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_item', full_name='inventoryreceiptlog.InventoryReceiptLog.order_item', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action_log', full_name='inventoryreceiptlog.InventoryReceiptLog.action_log', index=9,
      number=10, type=3, cpp_type=2, label=1,
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
  serialized_start=117,
  serialized_end=352,
)


_INVENTORYRECEIPTLOGLISTREQUEST = _descriptor.Descriptor(
  name='InventoryReceiptLogListRequest',
  full_name='inventoryreceiptlog.InventoryReceiptLogListRequest',
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
  serialized_start=354,
  serialized_end=386,
)


_INVENTORYRECEIPTLOGRETRIEVEREQUEST = _descriptor.Descriptor(
  name='InventoryReceiptLogRetrieveRequest',
  full_name='inventoryreceiptlog.InventoryReceiptLogRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inventoryreceiptlog.InventoryReceiptLogRetrieveRequest.id', index=0,
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
  serialized_start=388,
  serialized_end=436,
)

DESCRIPTOR.message_types_by_name['InventoryReceiptLog'] = _INVENTORYRECEIPTLOG
DESCRIPTOR.message_types_by_name['InventoryReceiptLogListRequest'] = _INVENTORYRECEIPTLOGLISTREQUEST
DESCRIPTOR.message_types_by_name['InventoryReceiptLogRetrieveRequest'] = _INVENTORYRECEIPTLOGRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InventoryReceiptLog = _reflection.GeneratedProtocolMessageType('InventoryReceiptLog', (_message.Message,), {
  'DESCRIPTOR' : _INVENTORYRECEIPTLOG,
  '__module__' : 'protos.order.inventory_receipt_log.inventory_receipt_log_pb2'
  # @@protoc_insertion_point(class_scope:inventoryreceiptlog.InventoryReceiptLog)
  })
_sym_db.RegisterMessage(InventoryReceiptLog)

InventoryReceiptLogListRequest = _reflection.GeneratedProtocolMessageType('InventoryReceiptLogListRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVENTORYRECEIPTLOGLISTREQUEST,
  '__module__' : 'protos.order.inventory_receipt_log.inventory_receipt_log_pb2'
  # @@protoc_insertion_point(class_scope:inventoryreceiptlog.InventoryReceiptLogListRequest)
  })
_sym_db.RegisterMessage(InventoryReceiptLogListRequest)

InventoryReceiptLogRetrieveRequest = _reflection.GeneratedProtocolMessageType('InventoryReceiptLogRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVENTORYRECEIPTLOGRETRIEVEREQUEST,
  '__module__' : 'protos.order.inventory_receipt_log.inventory_receipt_log_pb2'
  # @@protoc_insertion_point(class_scope:inventoryreceiptlog.InventoryReceiptLogRetrieveRequest)
  })
_sym_db.RegisterMessage(InventoryReceiptLogRetrieveRequest)



_INVENTORYRECEIPTLOGCONTROLLER = _descriptor.ServiceDescriptor(
  name='InventoryReceiptLogController',
  full_name='inventoryreceiptlog.InventoryReceiptLogController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=439,
  serialized_end=961,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='inventoryreceiptlog.InventoryReceiptLogController.List',
    index=0,
    containing_service=None,
    input_type=_INVENTORYRECEIPTLOGLISTREQUEST,
    output_type=_INVENTORYRECEIPTLOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='inventoryreceiptlog.InventoryReceiptLogController.Create',
    index=1,
    containing_service=None,
    input_type=_INVENTORYRECEIPTLOG,
    output_type=_INVENTORYRECEIPTLOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='inventoryreceiptlog.InventoryReceiptLogController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_INVENTORYRECEIPTLOGRETRIEVEREQUEST,
    output_type=_INVENTORYRECEIPTLOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='inventoryreceiptlog.InventoryReceiptLogController.Update',
    index=3,
    containing_service=None,
    input_type=_INVENTORYRECEIPTLOG,
    output_type=_INVENTORYRECEIPTLOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='inventoryreceiptlog.InventoryReceiptLogController.Destroy',
    index=4,
    containing_service=None,
    input_type=_INVENTORYRECEIPTLOG,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INVENTORYRECEIPTLOGCONTROLLER)

DESCRIPTOR.services_by_name['InventoryReceiptLogController'] = _INVENTORYRECEIPTLOGCONTROLLER

# @@protoc_insertion_point(module_scope)
