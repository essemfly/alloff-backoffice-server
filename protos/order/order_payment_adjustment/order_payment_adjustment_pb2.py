# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/order/order_payment_adjustment/order_payment_adjustment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/order/order_payment_adjustment/order_payment_adjustment.proto',
  package='orderpaymentadjustment',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDprotos/order/order_payment_adjustment/order_payment_adjustment.proto\x12\x16orderpaymentadjustment\x1a\x1bgoogle/protobuf/empty.proto\"\x9a\x02\n\x16OrderPaymentAdjustment\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tuser_uuid\x18\x02 \x01(\t\x12\x15\n\ruser_username\x18\x03 \x01(\t\x12\x0e\n\x06method\x18\x04 \x01(\t\x12\x18\n\x10previous_balance\x18\x05 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x06 \x01(\x05\x12\x19\n\x11resulting_balance\x18\x07 \x01(\x05\x12\x13\n\x0bpg_response\x18\x08 \x01(\t\x12\x19\n\x11\x62\x61nk_account_info\x18\t \x01(\t\x12\x0e\n\x06reason\x18\n \x01(\t\x12\x12\n\ncreated_at\x18\x0b \x01(\t\x12\x12\n\nupdated_at\x18\x0c \x01(\t\x12\r\n\x05order\x18\r \x01(\x03\"#\n!OrderPaymentAdjustmentListRequest\"3\n%OrderPaymentAdjustmentRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xc3\x04\n OrderPaymentAdjustmentController\x12u\n\x04List\x12\x39.orderpaymentadjustment.OrderPaymentAdjustmentListRequest\x1a..orderpaymentadjustment.OrderPaymentAdjustment\"\x00\x30\x01\x12j\n\x06\x43reate\x12..orderpaymentadjustment.OrderPaymentAdjustment\x1a..orderpaymentadjustment.OrderPaymentAdjustment\"\x00\x12{\n\x08Retrieve\x12=.orderpaymentadjustment.OrderPaymentAdjustmentRetrieveRequest\x1a..orderpaymentadjustment.OrderPaymentAdjustment\"\x00\x12j\n\x06Update\x12..orderpaymentadjustment.OrderPaymentAdjustment\x1a..orderpaymentadjustment.OrderPaymentAdjustment\"\x00\x12S\n\x07\x44\x65stroy\x12..orderpaymentadjustment.OrderPaymentAdjustment\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_ORDERPAYMENTADJUSTMENT = _descriptor.Descriptor(
  name='OrderPaymentAdjustment',
  full_name='orderpaymentadjustment.OrderPaymentAdjustment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orderpaymentadjustment.OrderPaymentAdjustment.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_uuid', full_name='orderpaymentadjustment.OrderPaymentAdjustment.user_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_username', full_name='orderpaymentadjustment.OrderPaymentAdjustment.user_username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='method', full_name='orderpaymentadjustment.OrderPaymentAdjustment.method', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previous_balance', full_name='orderpaymentadjustment.OrderPaymentAdjustment.previous_balance', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='orderpaymentadjustment.OrderPaymentAdjustment.amount', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resulting_balance', full_name='orderpaymentadjustment.OrderPaymentAdjustment.resulting_balance', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pg_response', full_name='orderpaymentadjustment.OrderPaymentAdjustment.pg_response', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bank_account_info', full_name='orderpaymentadjustment.OrderPaymentAdjustment.bank_account_info', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='orderpaymentadjustment.OrderPaymentAdjustment.reason', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='orderpaymentadjustment.OrderPaymentAdjustment.created_at', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='orderpaymentadjustment.OrderPaymentAdjustment.updated_at', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='orderpaymentadjustment.OrderPaymentAdjustment.order', index=12,
      number=13, type=3, cpp_type=2, label=1,
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
  serialized_start=126,
  serialized_end=408,
)


_ORDERPAYMENTADJUSTMENTLISTREQUEST = _descriptor.Descriptor(
  name='OrderPaymentAdjustmentListRequest',
  full_name='orderpaymentadjustment.OrderPaymentAdjustmentListRequest',
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
  serialized_start=410,
  serialized_end=445,
)


_ORDERPAYMENTADJUSTMENTRETRIEVEREQUEST = _descriptor.Descriptor(
  name='OrderPaymentAdjustmentRetrieveRequest',
  full_name='orderpaymentadjustment.OrderPaymentAdjustmentRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orderpaymentadjustment.OrderPaymentAdjustmentRetrieveRequest.id', index=0,
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
  serialized_start=447,
  serialized_end=498,
)

DESCRIPTOR.message_types_by_name['OrderPaymentAdjustment'] = _ORDERPAYMENTADJUSTMENT
DESCRIPTOR.message_types_by_name['OrderPaymentAdjustmentListRequest'] = _ORDERPAYMENTADJUSTMENTLISTREQUEST
DESCRIPTOR.message_types_by_name['OrderPaymentAdjustmentRetrieveRequest'] = _ORDERPAYMENTADJUSTMENTRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderPaymentAdjustment = _reflection.GeneratedProtocolMessageType('OrderPaymentAdjustment', (_message.Message,), {
  'DESCRIPTOR' : _ORDERPAYMENTADJUSTMENT,
  '__module__' : 'protos.order.order_payment_adjustment.order_payment_adjustment_pb2'
  # @@protoc_insertion_point(class_scope:orderpaymentadjustment.OrderPaymentAdjustment)
  })
_sym_db.RegisterMessage(OrderPaymentAdjustment)

OrderPaymentAdjustmentListRequest = _reflection.GeneratedProtocolMessageType('OrderPaymentAdjustmentListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERPAYMENTADJUSTMENTLISTREQUEST,
  '__module__' : 'protos.order.order_payment_adjustment.order_payment_adjustment_pb2'
  # @@protoc_insertion_point(class_scope:orderpaymentadjustment.OrderPaymentAdjustmentListRequest)
  })
_sym_db.RegisterMessage(OrderPaymentAdjustmentListRequest)

OrderPaymentAdjustmentRetrieveRequest = _reflection.GeneratedProtocolMessageType('OrderPaymentAdjustmentRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERPAYMENTADJUSTMENTRETRIEVEREQUEST,
  '__module__' : 'protos.order.order_payment_adjustment.order_payment_adjustment_pb2'
  # @@protoc_insertion_point(class_scope:orderpaymentadjustment.OrderPaymentAdjustmentRetrieveRequest)
  })
_sym_db.RegisterMessage(OrderPaymentAdjustmentRetrieveRequest)



_ORDERPAYMENTADJUSTMENTCONTROLLER = _descriptor.ServiceDescriptor(
  name='OrderPaymentAdjustmentController',
  full_name='orderpaymentadjustment.OrderPaymentAdjustmentController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=501,
  serialized_end=1080,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='orderpaymentadjustment.OrderPaymentAdjustmentController.List',
    index=0,
    containing_service=None,
    input_type=_ORDERPAYMENTADJUSTMENTLISTREQUEST,
    output_type=_ORDERPAYMENTADJUSTMENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='orderpaymentadjustment.OrderPaymentAdjustmentController.Create',
    index=1,
    containing_service=None,
    input_type=_ORDERPAYMENTADJUSTMENT,
    output_type=_ORDERPAYMENTADJUSTMENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='orderpaymentadjustment.OrderPaymentAdjustmentController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_ORDERPAYMENTADJUSTMENTRETRIEVEREQUEST,
    output_type=_ORDERPAYMENTADJUSTMENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='orderpaymentadjustment.OrderPaymentAdjustmentController.Update',
    index=3,
    containing_service=None,
    input_type=_ORDERPAYMENTADJUSTMENT,
    output_type=_ORDERPAYMENTADJUSTMENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='orderpaymentadjustment.OrderPaymentAdjustmentController.Destroy',
    index=4,
    containing_service=None,
    input_type=_ORDERPAYMENTADJUSTMENT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDERPAYMENTADJUSTMENTCONTROLLER)

DESCRIPTOR.services_by_name['OrderPaymentAdjustmentController'] = _ORDERPAYMENTADJUSTMENTCONTROLLER

# @@protoc_insertion_point(module_scope)
