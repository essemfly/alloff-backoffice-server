# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/order/order_item/order_item.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.order.order import order_pb2 as protos_dot_order_dot_order_dot_order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/order/order_item/order_item.proto',
  package='orderitem',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(protos/order/order_item/order_item.proto\x12\torderitem\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1eprotos/order/order/order.proto\"\xca\x07\n\tOrderItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x17\n\x0forder_item_code\x18\x02 \x01(\t\x12\x17\n\x0forder_item_type\x18\x03 \x01(\t\x12\x19\n\x11order_item_status\x18\x04 \x01(\t\x12\x15\n\rbrand_keyname\x18\x05 \x01(\t\x12\x15\n\rbrand_korname\x18\x06 \x01(\t\x12\x12\n\nproduct_id\x18\x07 \x01(\t\x12\x13\n\x0bproduct_url\x18\x08 \x01(\t\x12\x13\n\x0bproduct_img\x18\t \x01(\t\x12\x14\n\x0cproduct_name\x18\n \x01(\t\x12\x1a\n\x12\x63\x61ncel_description\x18\x0b \x01(\t\x12\x1c\n\x14\x64\x65livery_description\x18\x0c \x01(\t\x12\x13\n\x0bsales_price\x18\r \x01(\x05\x12\x0c\n\x04size\x18\x0e \x01(\t\x12\r\n\x05\x63olor\x18\x0f \x01(\t\x12\x10\n\x08quantity\x18\x10 \x01(\x05\x12\x14\n\x0ctracking_url\x18\x11 \x01(\t\x12\x17\n\x0ftracking_number\x18\x12 \x01(\t\x12\x12\n\ncreated_at\x18\x13 \x01(\t\x12\x12\n\nupdated_at\x18\x14 \x01(\t\x12\x12\n\nordered_at\x18\x15 \x01(\t\x12\x1b\n\x13payment_finished_at\x18\x16 \x01(\t\x12\x1c\n\x14product_preparing_at\x18\x17 \x01(\t\x12%\n\x1d\x66oreign_product_inspecting_at\x18\x18 \x01(\t\x12\x1d\n\x15\x64\x65livery_preparing_at\x18\x19 \x01(\t\x12#\n\x1b\x66oreign_delivery_started_at\x18\x1a \x01(\t\x12\x1b\n\x13\x64\x65livery_started_at\x18\x1b \x01(\t\x12\x1c\n\x14\x64\x65livery_finished_at\x18\x1c \x01(\t\x12\x14\n\x0c\x63onfirmed_at\x18\x1d \x01(\t\x12\x1b\n\x13\x63\x61ncel_requested_at\x18\x1e \x01(\t\x12\x1a\n\x12\x63\x61ncel_finished_at\x18\x1f \x01(\t\x12\x1d\n\x15\x65xchange_requested_at\x18  \x01(\t\x12\x1b\n\x13\x65xchange_started_at\x18! \x01(\t\x12\x1c\n\x14\x65xchange_finished_at\x18\" \x01(\t\x12\x1b\n\x13return_requested_at\x18# \x01(\t\x12\x19\n\x11return_started_at\x18$ \x01(\t\x12\x1a\n\x12return_finished_at\x18% \x01(\t\x12\x1b\n\x05order\x18& \x01(\x0b\x32\x0c.order.Order\"d\n\x14OrderItemListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x13\n\x06search\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08statuses\x18\x04 \x03(\tB\t\n\x07_search\"\x8d\x01\n\x15OrderItemListResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\x11\n\x04next\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x15\n\x08previous\x18\x03 \x01(\x03H\x01\x88\x01\x01\x12%\n\x07results\x18\x04 \x03(\x0b\x32\x14.orderitem.OrderItemB\x07\n\x05_nextB\x0b\n\t_previous\"&\n\x18OrderItemRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xd6\x02\n\x13OrderItemController\x12K\n\x04List\x12\x1f.orderitem.OrderItemListRequest\x1a .orderitem.OrderItemListResponse\"\x00\x12\x36\n\x06\x43reate\x12\x14.orderitem.OrderItem\x1a\x14.orderitem.OrderItem\"\x00\x12G\n\x08Retrieve\x12#.orderitem.OrderItemRetrieveRequest\x1a\x14.orderitem.OrderItem\"\x00\x12\x36\n\x06Update\x12\x14.orderitem.OrderItem\x1a\x14.orderitem.OrderItem\"\x00\x12\x39\n\x07\x44\x65stroy\x12\x14.orderitem.OrderItem\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,protos_dot_order_dot_order_dot_order__pb2.DESCRIPTOR,])




_ORDERITEM = _descriptor.Descriptor(
  name='OrderItem',
  full_name='orderitem.OrderItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orderitem.OrderItem.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_item_code', full_name='orderitem.OrderItem.order_item_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_item_type', full_name='orderitem.OrderItem.order_item_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_item_status', full_name='orderitem.OrderItem.order_item_status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='brand_keyname', full_name='orderitem.OrderItem.brand_keyname', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='brand_korname', full_name='orderitem.OrderItem.brand_korname', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='orderitem.OrderItem.product_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_url', full_name='orderitem.OrderItem.product_url', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_img', full_name='orderitem.OrderItem.product_img', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_name', full_name='orderitem.OrderItem.product_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cancel_description', full_name='orderitem.OrderItem.cancel_description', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_description', full_name='orderitem.OrderItem.delivery_description', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sales_price', full_name='orderitem.OrderItem.sales_price', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='orderitem.OrderItem.size', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='orderitem.OrderItem.color', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='orderitem.OrderItem.quantity', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tracking_url', full_name='orderitem.OrderItem.tracking_url', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tracking_number', full_name='orderitem.OrderItem.tracking_number', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='orderitem.OrderItem.created_at', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='orderitem.OrderItem.updated_at', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ordered_at', full_name='orderitem.OrderItem.ordered_at', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payment_finished_at', full_name='orderitem.OrderItem.payment_finished_at', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_preparing_at', full_name='orderitem.OrderItem.product_preparing_at', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='foreign_product_inspecting_at', full_name='orderitem.OrderItem.foreign_product_inspecting_at', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_preparing_at', full_name='orderitem.OrderItem.delivery_preparing_at', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='foreign_delivery_started_at', full_name='orderitem.OrderItem.foreign_delivery_started_at', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_started_at', full_name='orderitem.OrderItem.delivery_started_at', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_finished_at', full_name='orderitem.OrderItem.delivery_finished_at', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confirmed_at', full_name='orderitem.OrderItem.confirmed_at', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cancel_requested_at', full_name='orderitem.OrderItem.cancel_requested_at', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cancel_finished_at', full_name='orderitem.OrderItem.cancel_finished_at', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchange_requested_at', full_name='orderitem.OrderItem.exchange_requested_at', index=31,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchange_started_at', full_name='orderitem.OrderItem.exchange_started_at', index=32,
      number=33, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchange_finished_at', full_name='orderitem.OrderItem.exchange_finished_at', index=33,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='return_requested_at', full_name='orderitem.OrderItem.return_requested_at', index=34,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='return_started_at', full_name='orderitem.OrderItem.return_started_at', index=35,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='return_finished_at', full_name='orderitem.OrderItem.return_finished_at', index=36,
      number=37, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='orderitem.OrderItem.order', index=37,
      number=38, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_end=1087,
)


_ORDERITEMLISTREQUEST = _descriptor.Descriptor(
  name='OrderItemListRequest',
  full_name='orderitem.OrderItemListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='orderitem.OrderItemListRequest.page', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='orderitem.OrderItemListRequest.size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search', full_name='orderitem.OrderItemListRequest.search', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statuses', full_name='orderitem.OrderItemListRequest.statuses', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
    _descriptor.OneofDescriptor(
      name='_search', full_name='orderitem.OrderItemListRequest._search',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1089,
  serialized_end=1189,
)


_ORDERITEMLISTRESPONSE = _descriptor.Descriptor(
  name='OrderItemListResponse',
  full_name='orderitem.OrderItemListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='orderitem.OrderItemListResponse.count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next', full_name='orderitem.OrderItemListResponse.next', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previous', full_name='orderitem.OrderItemListResponse.previous', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='orderitem.OrderItemListResponse.results', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
    _descriptor.OneofDescriptor(
      name='_next', full_name='orderitem.OrderItemListResponse._next',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_previous', full_name='orderitem.OrderItemListResponse._previous',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1192,
  serialized_end=1333,
)


_ORDERITEMRETRIEVEREQUEST = _descriptor.Descriptor(
  name='OrderItemRetrieveRequest',
  full_name='orderitem.OrderItemRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orderitem.OrderItemRetrieveRequest.id', index=0,
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
  serialized_start=1335,
  serialized_end=1373,
)

_ORDERITEM.fields_by_name['order'].message_type = protos_dot_order_dot_order_dot_order__pb2._ORDER
_ORDERITEMLISTREQUEST.oneofs_by_name['_search'].fields.append(
  _ORDERITEMLISTREQUEST.fields_by_name['search'])
_ORDERITEMLISTREQUEST.fields_by_name['search'].containing_oneof = _ORDERITEMLISTREQUEST.oneofs_by_name['_search']
_ORDERITEMLISTRESPONSE.fields_by_name['results'].message_type = _ORDERITEM
_ORDERITEMLISTRESPONSE.oneofs_by_name['_next'].fields.append(
  _ORDERITEMLISTRESPONSE.fields_by_name['next'])
_ORDERITEMLISTRESPONSE.fields_by_name['next'].containing_oneof = _ORDERITEMLISTRESPONSE.oneofs_by_name['_next']
_ORDERITEMLISTRESPONSE.oneofs_by_name['_previous'].fields.append(
  _ORDERITEMLISTRESPONSE.fields_by_name['previous'])
_ORDERITEMLISTRESPONSE.fields_by_name['previous'].containing_oneof = _ORDERITEMLISTRESPONSE.oneofs_by_name['_previous']
DESCRIPTOR.message_types_by_name['OrderItem'] = _ORDERITEM
DESCRIPTOR.message_types_by_name['OrderItemListRequest'] = _ORDERITEMLISTREQUEST
DESCRIPTOR.message_types_by_name['OrderItemListResponse'] = _ORDERITEMLISTRESPONSE
DESCRIPTOR.message_types_by_name['OrderItemRetrieveRequest'] = _ORDERITEMRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderItem = _reflection.GeneratedProtocolMessageType('OrderItem', (_message.Message,), {
  'DESCRIPTOR' : _ORDERITEM,
  '__module__' : 'protos.order.order_item.order_item_pb2'
  # @@protoc_insertion_point(class_scope:orderitem.OrderItem)
  })
_sym_db.RegisterMessage(OrderItem)

OrderItemListRequest = _reflection.GeneratedProtocolMessageType('OrderItemListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERITEMLISTREQUEST,
  '__module__' : 'protos.order.order_item.order_item_pb2'
  # @@protoc_insertion_point(class_scope:orderitem.OrderItemListRequest)
  })
_sym_db.RegisterMessage(OrderItemListRequest)

OrderItemListResponse = _reflection.GeneratedProtocolMessageType('OrderItemListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORDERITEMLISTRESPONSE,
  '__module__' : 'protos.order.order_item.order_item_pb2'
  # @@protoc_insertion_point(class_scope:orderitem.OrderItemListResponse)
  })
_sym_db.RegisterMessage(OrderItemListResponse)

OrderItemRetrieveRequest = _reflection.GeneratedProtocolMessageType('OrderItemRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERITEMRETRIEVEREQUEST,
  '__module__' : 'protos.order.order_item.order_item_pb2'
  # @@protoc_insertion_point(class_scope:orderitem.OrderItemRetrieveRequest)
  })
_sym_db.RegisterMessage(OrderItemRetrieveRequest)



_ORDERITEMCONTROLLER = _descriptor.ServiceDescriptor(
  name='OrderItemController',
  full_name='orderitem.OrderItemController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1376,
  serialized_end=1718,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='orderitem.OrderItemController.List',
    index=0,
    containing_service=None,
    input_type=_ORDERITEMLISTREQUEST,
    output_type=_ORDERITEMLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='orderitem.OrderItemController.Create',
    index=1,
    containing_service=None,
    input_type=_ORDERITEM,
    output_type=_ORDERITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='orderitem.OrderItemController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_ORDERITEMRETRIEVEREQUEST,
    output_type=_ORDERITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='orderitem.OrderItemController.Update',
    index=3,
    containing_service=None,
    input_type=_ORDERITEM,
    output_type=_ORDERITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='orderitem.OrderItemController.Destroy',
    index=4,
    containing_service=None,
    input_type=_ORDERITEM,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDERITEMCONTROLLER)

DESCRIPTOR.services_by_name['OrderItemController'] = _ORDERITEMCONTROLLER

# @@protoc_insertion_point(module_scope)
