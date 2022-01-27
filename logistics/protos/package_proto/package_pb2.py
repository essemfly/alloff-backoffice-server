# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logistics/protos/package_proto/package.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from logistics.protos.courier_proto import courier_pb2 as logistics_dot_protos_dot_courier__proto_dot_courier__pb2
from logistics.protos.inventory_proto import inventory_pb2 as logistics_dot_protos_dot_inventory__proto_dot_inventory__pb2
from logistics.protos.package_remark_record_proto import package_remark_record_pb2 as logistics_dot_protos_dot_package__remark__record__proto_dot_package__remark__record__pb2
from logistics.protos.package_log_proto import package_log_pb2 as logistics_dot_protos_dot_package__log__proto_dot_package__log__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='logistics/protos/package_proto/package.proto',
  package='package',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,logistics/protos/package_proto/package.proto\x12\x07package\x1a\x1bgoogle/protobuf/empty.proto\x1a,logistics/protos/courier_proto/courier.proto\x1a\x30logistics/protos/inventory_proto/inventory.proto\x1aHlogistics/protos/package_remark_record_proto/package_remark_record.proto\x1a\x34logistics/protos/package_log_proto/package_log.proto\"\xec\x06\n\x07Package\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03key\x18\x02 \x01(\t\x12.\n\x06status\x18\x03 \x01(\x0e\x32\x1e.package.Package.PackageStatus\x12\x1e\n\x16related_order_item_ids\x18\x04 \x03(\t\x12\x15\n\rcustomer_name\x18\x05 \x01(\t\x12\x18\n\x10\x63ustomer_contact\x18\x06 \x01(\t\x12\x14\n\x0c\x62\x61se_address\x18\x07 \x01(\t\x12\x1b\n\x0e\x64\x65tail_address\x18\x08 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0bpostal_code\x18\t \x01(\t\x12\x1a\n\rdelivery_note\x18\n \x01(\tH\x01\x88\x01\x01\x12\x1c\n\x0ftracking_number\x18\x0b \x01(\tH\x02\x88\x01\x01\x12\x12\n\ncreated_at\x18\x0c \x01(\t\x12\x12\n\nupdated_at\x18\r \x01(\t\x12\x17\n\ndeleted_at\x18\x0e \x01(\tH\x03\x88\x01\x01\x12)\n\x0binventories\x18\x0f \x03(\x0b\x32\x14.inventory.Inventory\x12\x42\n\x0eremark_records\x18\x10 \x03(\x0b\x32*.package_remark_record.PackageRemarkRecord\x12*\n\x04logs\x18\x11 \x01(\x0b\x32\x17.package_log.PackageLogH\x04\x88\x01\x01\x12/\n\x10tracking_courier\x18\x12 \x01(\x0b\x32\x10.courier.CourierH\x05\x88\x01\x01\"\xd1\x01\n\rPackageStatus\x12\x16\n\x12\x44\x45LIVERY_PREPARING\x10\x00\x12\x14\n\x10\x44\x45LIVERY_STARTED\x10\x01\x12\x15\n\x11\x44\x45LIVERY_FINISHED\x10\x02\x12\x1e\n\x1aOVERSEA_SHIPMENT_PREPARING\x10\x03\x12\x1c\n\x18OVERSEA_SHIPMENT_STARTED\x10\x04\x12\x14\n\x10\x43\x41NCEL_REQUESTED\x10\x05\x12\x12\n\x0e\x43\x41NCEL_PENDING\x10\x06\x12\x13\n\x0f\x43\x41NCEL_FINISHED\x10\x07\x42\x11\n\x0f_detail_addressB\x10\n\x0e_delivery_noteB\x12\n\x10_tracking_numberB\r\n\x0b_deleted_atB\x07\n\x05_logsB\x13\n\x11_tracking_courier\"\x14\n\x12PackageListRequest\"$\n\x16PackageRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xa6\x02\n\x11PackageController\x12\x39\n\x04List\x12\x1b.package.PackageListRequest\x1a\x10.package.Package\"\x00\x30\x01\x12.\n\x06\x43reate\x12\x10.package.Package\x1a\x10.package.Package\"\x00\x12?\n\x08Retrieve\x12\x1f.package.PackageRetrieveRequest\x1a\x10.package.Package\"\x00\x12.\n\x06Update\x12\x10.package.Package\x1a\x10.package.Package\"\x00\x12\x35\n\x07\x44\x65stroy\x12\x10.package.Package\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,logistics_dot_protos_dot_courier__proto_dot_courier__pb2.DESCRIPTOR,logistics_dot_protos_dot_inventory__proto_dot_inventory__pb2.DESCRIPTOR,logistics_dot_protos_dot_package__remark__record__proto_dot_package__remark__record__pb2.DESCRIPTOR,logistics_dot_protos_dot_package__log__proto_dot_package__log__pb2.DESCRIPTOR,])



_PACKAGE_PACKAGESTATUS = _descriptor.EnumDescriptor(
  name='PackageStatus',
  full_name='package.Package.PackageStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DELIVERY_PREPARING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELIVERY_STARTED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELIVERY_FINISHED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OVERSEA_SHIPMENT_PREPARING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OVERSEA_SHIPMENT_STARTED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_REQUESTED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_PENDING', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_FINISHED', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=876,
  serialized_end=1085,
)
_sym_db.RegisterEnumDescriptor(_PACKAGE_PACKAGESTATUS)


_PACKAGE = _descriptor.Descriptor(
  name='Package',
  full_name='package.Package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='package.Package.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='package.Package.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='package.Package.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='related_order_item_ids', full_name='package.Package.related_order_item_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_name', full_name='package.Package.customer_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_contact', full_name='package.Package.customer_contact', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_address', full_name='package.Package.base_address', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detail_address', full_name='package.Package.detail_address', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postal_code', full_name='package.Package.postal_code', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_note', full_name='package.Package.delivery_note', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tracking_number', full_name='package.Package.tracking_number', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='package.Package.created_at', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='package.Package.updated_at', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted_at', full_name='package.Package.deleted_at', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inventories', full_name='package.Package.inventories', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remark_records', full_name='package.Package.remark_records', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs', full_name='package.Package.logs', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tracking_courier', full_name='package.Package.tracking_courier', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PACKAGE_PACKAGESTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_detail_address', full_name='package.Package._detail_address',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_delivery_note', full_name='package.Package._delivery_note',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_tracking_number', full_name='package.Package._tracking_number',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_deleted_at', full_name='package.Package._deleted_at',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_logs', full_name='package.Package._logs',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_tracking_courier', full_name='package.Package._tracking_courier',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=311,
  serialized_end=1187,
)


_PACKAGELISTREQUEST = _descriptor.Descriptor(
  name='PackageListRequest',
  full_name='package.PackageListRequest',
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
  serialized_start=1189,
  serialized_end=1209,
)


_PACKAGERETRIEVEREQUEST = _descriptor.Descriptor(
  name='PackageRetrieveRequest',
  full_name='package.PackageRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='package.PackageRetrieveRequest.id', index=0,
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
  serialized_start=1211,
  serialized_end=1247,
)

_PACKAGE.fields_by_name['status'].enum_type = _PACKAGE_PACKAGESTATUS
_PACKAGE.fields_by_name['inventories'].message_type = logistics_dot_protos_dot_inventory__proto_dot_inventory__pb2._INVENTORY
_PACKAGE.fields_by_name['remark_records'].message_type = logistics_dot_protos_dot_package__remark__record__proto_dot_package__remark__record__pb2._PACKAGEREMARKRECORD
_PACKAGE.fields_by_name['logs'].message_type = logistics_dot_protos_dot_package__log__proto_dot_package__log__pb2._PACKAGELOG
_PACKAGE.fields_by_name['tracking_courier'].message_type = logistics_dot_protos_dot_courier__proto_dot_courier__pb2._COURIER
_PACKAGE_PACKAGESTATUS.containing_type = _PACKAGE
_PACKAGE.oneofs_by_name['_detail_address'].fields.append(
  _PACKAGE.fields_by_name['detail_address'])
_PACKAGE.fields_by_name['detail_address'].containing_oneof = _PACKAGE.oneofs_by_name['_detail_address']
_PACKAGE.oneofs_by_name['_delivery_note'].fields.append(
  _PACKAGE.fields_by_name['delivery_note'])
_PACKAGE.fields_by_name['delivery_note'].containing_oneof = _PACKAGE.oneofs_by_name['_delivery_note']
_PACKAGE.oneofs_by_name['_tracking_number'].fields.append(
  _PACKAGE.fields_by_name['tracking_number'])
_PACKAGE.fields_by_name['tracking_number'].containing_oneof = _PACKAGE.oneofs_by_name['_tracking_number']
_PACKAGE.oneofs_by_name['_deleted_at'].fields.append(
  _PACKAGE.fields_by_name['deleted_at'])
_PACKAGE.fields_by_name['deleted_at'].containing_oneof = _PACKAGE.oneofs_by_name['_deleted_at']
_PACKAGE.oneofs_by_name['_logs'].fields.append(
  _PACKAGE.fields_by_name['logs'])
_PACKAGE.fields_by_name['logs'].containing_oneof = _PACKAGE.oneofs_by_name['_logs']
_PACKAGE.oneofs_by_name['_tracking_courier'].fields.append(
  _PACKAGE.fields_by_name['tracking_courier'])
_PACKAGE.fields_by_name['tracking_courier'].containing_oneof = _PACKAGE.oneofs_by_name['_tracking_courier']
DESCRIPTOR.message_types_by_name['Package'] = _PACKAGE
DESCRIPTOR.message_types_by_name['PackageListRequest'] = _PACKAGELISTREQUEST
DESCRIPTOR.message_types_by_name['PackageRetrieveRequest'] = _PACKAGERETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Package = _reflection.GeneratedProtocolMessageType('Package', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGE,
  '__module__' : 'logistics.protos.package_proto.package_pb2'
  # @@protoc_insertion_point(class_scope:package.Package)
  })
_sym_db.RegisterMessage(Package)

PackageListRequest = _reflection.GeneratedProtocolMessageType('PackageListRequest', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGELISTREQUEST,
  '__module__' : 'logistics.protos.package_proto.package_pb2'
  # @@protoc_insertion_point(class_scope:package.PackageListRequest)
  })
_sym_db.RegisterMessage(PackageListRequest)

PackageRetrieveRequest = _reflection.GeneratedProtocolMessageType('PackageRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGERETRIEVEREQUEST,
  '__module__' : 'logistics.protos.package_proto.package_pb2'
  # @@protoc_insertion_point(class_scope:package.PackageRetrieveRequest)
  })
_sym_db.RegisterMessage(PackageRetrieveRequest)



_PACKAGECONTROLLER = _descriptor.ServiceDescriptor(
  name='PackageController',
  full_name='package.PackageController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1250,
  serialized_end=1544,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='package.PackageController.List',
    index=0,
    containing_service=None,
    input_type=_PACKAGELISTREQUEST,
    output_type=_PACKAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='package.PackageController.Create',
    index=1,
    containing_service=None,
    input_type=_PACKAGE,
    output_type=_PACKAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='package.PackageController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_PACKAGERETRIEVEREQUEST,
    output_type=_PACKAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='package.PackageController.Update',
    index=3,
    containing_service=None,
    input_type=_PACKAGE,
    output_type=_PACKAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='package.PackageController.Destroy',
    index=4,
    containing_service=None,
    input_type=_PACKAGE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PACKAGECONTROLLER)

DESCRIPTOR.services_by_name['PackageController'] = _PACKAGECONTROLLER

# @@protoc_insertion_point(module_scope)
