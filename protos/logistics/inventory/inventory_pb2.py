# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/logistics/inventory/inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/logistics/inventory/inventory.proto',
  package='inventory',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*protos/logistics/inventory/inventory.proto\x12\tinventory\x1a\x1bgoogle/protobuf/empty.proto\"\xaf\x02\n\tInventory\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x12\n\nproduct_id\x18\x04 \x01(\t\x12\x14\n\x0cproduct_name\x18\x05 \x01(\t\x12\x15\n\rbrand_keyname\x18\x06 \x01(\t\x12\x15\n\rbrand_korname\x18\x07 \x01(\t\x12\x0c\n\x04size\x18\x08 \x01(\t\x12\r\n\x05\x63olor\x18\t \x01(\t\x12\x10\n\x08location\x18\n \x01(\t\x12\x0c\n\x04memo\x18\x0b \x01(\t\x12\x12\n\ncreated_at\x18\x0c \x01(\t\x12\x12\n\nupdated_at\x18\r \x01(\t\x12\x17\n\ndeleted_at\x18\x0e \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0bproduct_img\x18\x0f \x01(\tB\r\n\x0b_deleted_at\"\x80\x01\n\x14InventoryListRequest\x12\x11\n\x04page\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x11\n\x04size\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x13\n\x06search\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x10\n\x08statuses\x18\x04 \x03(\tB\x07\n\x05_pageB\x07\n\x05_sizeB\t\n\x07_search\"\x8d\x01\n\x15InventoryListResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\x11\n\x04next\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x15\n\x08previous\x18\x03 \x01(\x03H\x01\x88\x01\x01\x12%\n\x07results\x18\x04 \x03(\x0b\x32\x14.inventory.InventoryB\x07\n\x05_nextB\x0b\n\t_previous\"&\n\x18InventoryRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03*f\n\x0fInventoryStatus\x12\x0b\n\x07\x43REATED\x10\x00\x12\x0c\n\x08IN_STOCK\x10\x01\x12\x15\n\x11PROCESSING_NEEDED\x10\x02\x12\x0b\n\x07SHIPPED\x10\x03\x12\x14\n\x10SHIPPING_PENDING\x10\x04\x32\xe5\x02\n\x13InventoryController\x12K\n\x04List\x12\x1f.inventory.InventoryListRequest\x1a .inventory.InventoryListResponse\"\x00\x12\x36\n\x06\x43reate\x12\x14.inventory.Inventory\x1a\x14.inventory.Inventory\"\x00\x12G\n\x08Retrieve\x12#.inventory.InventoryRetrieveRequest\x1a\x14.inventory.Inventory\"\x00\x12\x36\n\x06Update\x12\x14.inventory.Inventory\x1a\x14.inventory.Inventory\"\x00\x12H\n\x07\x44\x65stroy\x12#.inventory.InventoryRetrieveRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_INVENTORYSTATUS = _descriptor.EnumDescriptor(
  name='InventoryStatus',
  full_name='inventory.InventoryStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_STOCK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROCESSING_NEEDED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHIPPED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHIPPING_PENDING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=707,
  serialized_end=809,
)
_sym_db.RegisterEnumDescriptor(_INVENTORYSTATUS)

InventoryStatus = enum_type_wrapper.EnumTypeWrapper(_INVENTORYSTATUS)
CREATED = 0
IN_STOCK = 1
PROCESSING_NEEDED = 2
SHIPPED = 3
SHIPPING_PENDING = 4



_INVENTORY = _descriptor.Descriptor(
  name='Inventory',
  full_name='inventory.Inventory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inventory.Inventory.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='inventory.Inventory.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='inventory.Inventory.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='inventory.Inventory.product_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_name', full_name='inventory.Inventory.product_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='brand_keyname', full_name='inventory.Inventory.brand_keyname', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='brand_korname', full_name='inventory.Inventory.brand_korname', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='inventory.Inventory.size', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='inventory.Inventory.color', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='inventory.Inventory.location', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memo', full_name='inventory.Inventory.memo', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='inventory.Inventory.created_at', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='inventory.Inventory.updated_at', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted_at', full_name='inventory.Inventory.deleted_at', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_img', full_name='inventory.Inventory.product_img', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
      name='_deleted_at', full_name='inventory.Inventory._deleted_at',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=87,
  serialized_end=390,
)


_INVENTORYLISTREQUEST = _descriptor.Descriptor(
  name='InventoryListRequest',
  full_name='inventory.InventoryListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='inventory.InventoryListRequest.page', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='inventory.InventoryListRequest.size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search', full_name='inventory.InventoryListRequest.search', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statuses', full_name='inventory.InventoryListRequest.statuses', index=3,
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
      name='_page', full_name='inventory.InventoryListRequest._page',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_size', full_name='inventory.InventoryListRequest._size',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_search', full_name='inventory.InventoryListRequest._search',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=393,
  serialized_end=521,
)


_INVENTORYLISTRESPONSE = _descriptor.Descriptor(
  name='InventoryListResponse',
  full_name='inventory.InventoryListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='inventory.InventoryListResponse.count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next', full_name='inventory.InventoryListResponse.next', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previous', full_name='inventory.InventoryListResponse.previous', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='inventory.InventoryListResponse.results', index=3,
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
      name='_next', full_name='inventory.InventoryListResponse._next',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_previous', full_name='inventory.InventoryListResponse._previous',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=524,
  serialized_end=665,
)


_INVENTORYRETRIEVEREQUEST = _descriptor.Descriptor(
  name='InventoryRetrieveRequest',
  full_name='inventory.InventoryRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inventory.InventoryRetrieveRequest.id', index=0,
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
  serialized_start=667,
  serialized_end=705,
)

_INVENTORY.oneofs_by_name['_deleted_at'].fields.append(
  _INVENTORY.fields_by_name['deleted_at'])
_INVENTORY.fields_by_name['deleted_at'].containing_oneof = _INVENTORY.oneofs_by_name['_deleted_at']
_INVENTORYLISTREQUEST.oneofs_by_name['_page'].fields.append(
  _INVENTORYLISTREQUEST.fields_by_name['page'])
_INVENTORYLISTREQUEST.fields_by_name['page'].containing_oneof = _INVENTORYLISTREQUEST.oneofs_by_name['_page']
_INVENTORYLISTREQUEST.oneofs_by_name['_size'].fields.append(
  _INVENTORYLISTREQUEST.fields_by_name['size'])
_INVENTORYLISTREQUEST.fields_by_name['size'].containing_oneof = _INVENTORYLISTREQUEST.oneofs_by_name['_size']
_INVENTORYLISTREQUEST.oneofs_by_name['_search'].fields.append(
  _INVENTORYLISTREQUEST.fields_by_name['search'])
_INVENTORYLISTREQUEST.fields_by_name['search'].containing_oneof = _INVENTORYLISTREQUEST.oneofs_by_name['_search']
_INVENTORYLISTRESPONSE.fields_by_name['results'].message_type = _INVENTORY
_INVENTORYLISTRESPONSE.oneofs_by_name['_next'].fields.append(
  _INVENTORYLISTRESPONSE.fields_by_name['next'])
_INVENTORYLISTRESPONSE.fields_by_name['next'].containing_oneof = _INVENTORYLISTRESPONSE.oneofs_by_name['_next']
_INVENTORYLISTRESPONSE.oneofs_by_name['_previous'].fields.append(
  _INVENTORYLISTRESPONSE.fields_by_name['previous'])
_INVENTORYLISTRESPONSE.fields_by_name['previous'].containing_oneof = _INVENTORYLISTRESPONSE.oneofs_by_name['_previous']
DESCRIPTOR.message_types_by_name['Inventory'] = _INVENTORY
DESCRIPTOR.message_types_by_name['InventoryListRequest'] = _INVENTORYLISTREQUEST
DESCRIPTOR.message_types_by_name['InventoryListResponse'] = _INVENTORYLISTRESPONSE
DESCRIPTOR.message_types_by_name['InventoryRetrieveRequest'] = _INVENTORYRETRIEVEREQUEST
DESCRIPTOR.enum_types_by_name['InventoryStatus'] = _INVENTORYSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Inventory = _reflection.GeneratedProtocolMessageType('Inventory', (_message.Message,), {
  'DESCRIPTOR' : _INVENTORY,
  '__module__' : 'protos.logistics.inventory.inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.Inventory)
  })
_sym_db.RegisterMessage(Inventory)

InventoryListRequest = _reflection.GeneratedProtocolMessageType('InventoryListRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVENTORYLISTREQUEST,
  '__module__' : 'protos.logistics.inventory.inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.InventoryListRequest)
  })
_sym_db.RegisterMessage(InventoryListRequest)

InventoryListResponse = _reflection.GeneratedProtocolMessageType('InventoryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVENTORYLISTRESPONSE,
  '__module__' : 'protos.logistics.inventory.inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.InventoryListResponse)
  })
_sym_db.RegisterMessage(InventoryListResponse)

InventoryRetrieveRequest = _reflection.GeneratedProtocolMessageType('InventoryRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVENTORYRETRIEVEREQUEST,
  '__module__' : 'protos.logistics.inventory.inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.InventoryRetrieveRequest)
  })
_sym_db.RegisterMessage(InventoryRetrieveRequest)



_INVENTORYCONTROLLER = _descriptor.ServiceDescriptor(
  name='InventoryController',
  full_name='inventory.InventoryController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=812,
  serialized_end=1169,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='inventory.InventoryController.List',
    index=0,
    containing_service=None,
    input_type=_INVENTORYLISTREQUEST,
    output_type=_INVENTORYLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='inventory.InventoryController.Create',
    index=1,
    containing_service=None,
    input_type=_INVENTORY,
    output_type=_INVENTORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='inventory.InventoryController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_INVENTORYRETRIEVEREQUEST,
    output_type=_INVENTORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='inventory.InventoryController.Update',
    index=3,
    containing_service=None,
    input_type=_INVENTORY,
    output_type=_INVENTORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='inventory.InventoryController.Destroy',
    index=4,
    containing_service=None,
    input_type=_INVENTORYRETRIEVEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INVENTORYCONTROLLER)

DESCRIPTOR.services_by_name['InventoryController'] = _INVENTORYCONTROLLER

# @@protoc_insertion_point(module_scope)
