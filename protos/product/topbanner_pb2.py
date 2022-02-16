# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/product/topbanner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/product/topbanner.proto',
  package='grpcServer',
  syntax='proto3',
  serialized_options=b'Z/github.com/lessbutter/alloff-api/api/grpcServer',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eprotos/product/topbanner.proto\x12\ngrpcServer\"(\n\x13GetTopBannerRequest\x12\x11\n\tbanner_id\x18\x01 \x01(\t\"6\n\x15ListTopBannersRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"\x87\x02\n\x14\x45\x64itTopBannerRequest\x12\x11\n\tbanner_id\x18\x01 \x01(\t\x12\x19\n\x0c\x62\x61nner_image\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rexhibition_id\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05title\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08subtitle\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07is_live\x18\x06 \x01(\x08H\x04\x88\x01\x01\x12\x13\n\x06weight\x18\x07 \x01(\x05H\x05\x88\x01\x01\x42\x0f\n\r_banner_imageB\x10\n\x0e_exhibition_idB\x08\n\x06_titleB\x0b\n\t_subtitleB\n\n\x08_is_liveB\t\n\x07_weight\"\x87\x01\n\x16\x43reateTopBannerRequest\x12\x14\n\x0c\x62\x61nner_image\x18\x01 \x01(\t\x12\x15\n\rexhibition_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x10\n\x08subtitle\x18\x04 \x01(\t\x12\x0f\n\x07is_live\x18\x05 \x01(\x08\x12\x0e\n\x06weight\x18\x06 \x01(\x05\"D\n\x14GetTopBannerResponse\x12,\n\x06\x62\x61nner\x18\x01 \x01(\x0b\x32\x1c.grpcServer.TopBannerMessage\"|\n\x16ListTopBannersResponse\x12-\n\x07\x62\x61nners\x18\x01 \x03(\x0b\x32\x1c.grpcServer.TopBannerMessage\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\x14\n\x0ctotal_counts\x18\x04 \x01(\x05\"E\n\x15\x45\x64itTopBannerResponse\x12,\n\x06\x62\x61nner\x18\x01 \x01(\x0b\x32\x1c.grpcServer.TopBannerMessage\"G\n\x17\x43reateTopBannerResponse\x12,\n\x06\x62\x61nner\x18\x01 \x01(\x0b\x32\x1c.grpcServer.TopBannerMessage\"\x94\x01\n\x10TopBannerMessage\x12\x11\n\tbanner_id\x18\x01 \x01(\t\x12\x14\n\x0c\x62\x61nner_image\x18\x02 \x01(\t\x12\x15\n\rexhibition_id\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x10\n\x08subtitle\x18\x05 \x01(\t\x12\x0f\n\x07is_live\x18\x06 \x01(\x08\x12\x0e\n\x06weight\x18\x07 \x01(\x05\x32\xe9\x02\n\tTopBanner\x12Q\n\x0cGetTopBanner\x12\x1f.grpcServer.GetTopBannerRequest\x1a .grpcServer.GetTopBannerResponse\x12W\n\x0eListTopBanners\x12!.grpcServer.ListTopBannersRequest\x1a\".grpcServer.ListTopBannersResponse\x12T\n\rEditTopBanner\x12 .grpcServer.EditTopBannerRequest\x1a!.grpcServer.EditTopBannerResponse\x12Z\n\x0f\x43reateTopBanner\x12\".grpcServer.CreateTopBannerRequest\x1a#.grpcServer.CreateTopBannerResponseB1Z/github.com/lessbutter/alloff-api/api/grpcServerb\x06proto3'
)




_GETTOPBANNERREQUEST = _descriptor.Descriptor(
  name='GetTopBannerRequest',
  full_name='grpcServer.GetTopBannerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='banner_id', full_name='grpcServer.GetTopBannerRequest.banner_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  ],
  serialized_start=46,
  serialized_end=86,
)


_LISTTOPBANNERSREQUEST = _descriptor.Descriptor(
  name='ListTopBannersRequest',
  full_name='grpcServer.ListTopBannersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='grpcServer.ListTopBannersRequest.offset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='grpcServer.ListTopBannersRequest.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=88,
  serialized_end=142,
)


_EDITTOPBANNERREQUEST = _descriptor.Descriptor(
  name='EditTopBannerRequest',
  full_name='grpcServer.EditTopBannerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='banner_id', full_name='grpcServer.EditTopBannerRequest.banner_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='banner_image', full_name='grpcServer.EditTopBannerRequest.banner_image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exhibition_id', full_name='grpcServer.EditTopBannerRequest.exhibition_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='grpcServer.EditTopBannerRequest.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtitle', full_name='grpcServer.EditTopBannerRequest.subtitle', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_live', full_name='grpcServer.EditTopBannerRequest.is_live', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weight', full_name='grpcServer.EditTopBannerRequest.weight', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
    _descriptor.OneofDescriptor(
      name='_banner_image', full_name='grpcServer.EditTopBannerRequest._banner_image',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_exhibition_id', full_name='grpcServer.EditTopBannerRequest._exhibition_id',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_title', full_name='grpcServer.EditTopBannerRequest._title',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_subtitle', full_name='grpcServer.EditTopBannerRequest._subtitle',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_is_live', full_name='grpcServer.EditTopBannerRequest._is_live',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_weight', full_name='grpcServer.EditTopBannerRequest._weight',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=145,
  serialized_end=408,
)


_CREATETOPBANNERREQUEST = _descriptor.Descriptor(
  name='CreateTopBannerRequest',
  full_name='grpcServer.CreateTopBannerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='banner_image', full_name='grpcServer.CreateTopBannerRequest.banner_image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exhibition_id', full_name='grpcServer.CreateTopBannerRequest.exhibition_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='grpcServer.CreateTopBannerRequest.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtitle', full_name='grpcServer.CreateTopBannerRequest.subtitle', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_live', full_name='grpcServer.CreateTopBannerRequest.is_live', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weight', full_name='grpcServer.CreateTopBannerRequest.weight', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=411,
  serialized_end=546,
)


_GETTOPBANNERRESPONSE = _descriptor.Descriptor(
  name='GetTopBannerResponse',
  full_name='grpcServer.GetTopBannerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='banner', full_name='grpcServer.GetTopBannerResponse.banner', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=548,
  serialized_end=616,
)


_LISTTOPBANNERSRESPONSE = _descriptor.Descriptor(
  name='ListTopBannersResponse',
  full_name='grpcServer.ListTopBannersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='banners', full_name='grpcServer.ListTopBannersResponse.banners', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='grpcServer.ListTopBannersResponse.offset', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='grpcServer.ListTopBannersResponse.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_counts', full_name='grpcServer.ListTopBannersResponse.total_counts', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=618,
  serialized_end=742,
)


_EDITTOPBANNERRESPONSE = _descriptor.Descriptor(
  name='EditTopBannerResponse',
  full_name='grpcServer.EditTopBannerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='banner', full_name='grpcServer.EditTopBannerResponse.banner', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=744,
  serialized_end=813,
)


_CREATETOPBANNERRESPONSE = _descriptor.Descriptor(
  name='CreateTopBannerResponse',
  full_name='grpcServer.CreateTopBannerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='banner', full_name='grpcServer.CreateTopBannerResponse.banner', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=815,
  serialized_end=886,
)


_TOPBANNERMESSAGE = _descriptor.Descriptor(
  name='TopBannerMessage',
  full_name='grpcServer.TopBannerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='banner_id', full_name='grpcServer.TopBannerMessage.banner_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='banner_image', full_name='grpcServer.TopBannerMessage.banner_image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exhibition_id', full_name='grpcServer.TopBannerMessage.exhibition_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='grpcServer.TopBannerMessage.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtitle', full_name='grpcServer.TopBannerMessage.subtitle', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_live', full_name='grpcServer.TopBannerMessage.is_live', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weight', full_name='grpcServer.TopBannerMessage.weight', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=889,
  serialized_end=1037,
)

_EDITTOPBANNERREQUEST.oneofs_by_name['_banner_image'].fields.append(
  _EDITTOPBANNERREQUEST.fields_by_name['banner_image'])
_EDITTOPBANNERREQUEST.fields_by_name['banner_image'].containing_oneof = _EDITTOPBANNERREQUEST.oneofs_by_name['_banner_image']
_EDITTOPBANNERREQUEST.oneofs_by_name['_exhibition_id'].fields.append(
  _EDITTOPBANNERREQUEST.fields_by_name['exhibition_id'])
_EDITTOPBANNERREQUEST.fields_by_name['exhibition_id'].containing_oneof = _EDITTOPBANNERREQUEST.oneofs_by_name['_exhibition_id']
_EDITTOPBANNERREQUEST.oneofs_by_name['_title'].fields.append(
  _EDITTOPBANNERREQUEST.fields_by_name['title'])
_EDITTOPBANNERREQUEST.fields_by_name['title'].containing_oneof = _EDITTOPBANNERREQUEST.oneofs_by_name['_title']
_EDITTOPBANNERREQUEST.oneofs_by_name['_subtitle'].fields.append(
  _EDITTOPBANNERREQUEST.fields_by_name['subtitle'])
_EDITTOPBANNERREQUEST.fields_by_name['subtitle'].containing_oneof = _EDITTOPBANNERREQUEST.oneofs_by_name['_subtitle']
_EDITTOPBANNERREQUEST.oneofs_by_name['_is_live'].fields.append(
  _EDITTOPBANNERREQUEST.fields_by_name['is_live'])
_EDITTOPBANNERREQUEST.fields_by_name['is_live'].containing_oneof = _EDITTOPBANNERREQUEST.oneofs_by_name['_is_live']
_EDITTOPBANNERREQUEST.oneofs_by_name['_weight'].fields.append(
  _EDITTOPBANNERREQUEST.fields_by_name['weight'])
_EDITTOPBANNERREQUEST.fields_by_name['weight'].containing_oneof = _EDITTOPBANNERREQUEST.oneofs_by_name['_weight']
_GETTOPBANNERRESPONSE.fields_by_name['banner'].message_type = _TOPBANNERMESSAGE
_LISTTOPBANNERSRESPONSE.fields_by_name['banners'].message_type = _TOPBANNERMESSAGE
_EDITTOPBANNERRESPONSE.fields_by_name['banner'].message_type = _TOPBANNERMESSAGE
_CREATETOPBANNERRESPONSE.fields_by_name['banner'].message_type = _TOPBANNERMESSAGE
DESCRIPTOR.message_types_by_name['GetTopBannerRequest'] = _GETTOPBANNERREQUEST
DESCRIPTOR.message_types_by_name['ListTopBannersRequest'] = _LISTTOPBANNERSREQUEST
DESCRIPTOR.message_types_by_name['EditTopBannerRequest'] = _EDITTOPBANNERREQUEST
DESCRIPTOR.message_types_by_name['CreateTopBannerRequest'] = _CREATETOPBANNERREQUEST
DESCRIPTOR.message_types_by_name['GetTopBannerResponse'] = _GETTOPBANNERRESPONSE
DESCRIPTOR.message_types_by_name['ListTopBannersResponse'] = _LISTTOPBANNERSRESPONSE
DESCRIPTOR.message_types_by_name['EditTopBannerResponse'] = _EDITTOPBANNERRESPONSE
DESCRIPTOR.message_types_by_name['CreateTopBannerResponse'] = _CREATETOPBANNERRESPONSE
DESCRIPTOR.message_types_by_name['TopBannerMessage'] = _TOPBANNERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTopBannerRequest = _reflection.GeneratedProtocolMessageType('GetTopBannerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTOPBANNERREQUEST,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:grpcServer.GetTopBannerRequest)
  })
_sym_db.RegisterMessage(GetTopBannerRequest)

ListTopBannersRequest = _reflection.GeneratedProtocolMessageType('ListTopBannersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOPBANNERSREQUEST,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:grpcServer.ListTopBannersRequest)
  })
_sym_db.RegisterMessage(ListTopBannersRequest)

EditTopBannerRequest = _reflection.GeneratedProtocolMessageType('EditTopBannerRequest', (_message.Message,), {
  'DESCRIPTOR' : _EDITTOPBANNERREQUEST,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:grpcServer.EditTopBannerRequest)
  })
_sym_db.RegisterMessage(EditTopBannerRequest)

CreateTopBannerRequest = _reflection.GeneratedProtocolMessageType('CreateTopBannerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOPBANNERREQUEST,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:grpcServer.CreateTopBannerRequest)
  })
_sym_db.RegisterMessage(CreateTopBannerRequest)

GetTopBannerResponse = _reflection.GeneratedProtocolMessageType('GetTopBannerResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTOPBANNERRESPONSE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:grpcServer.GetTopBannerResponse)
  })
_sym_db.RegisterMessage(GetTopBannerResponse)

ListTopBannersResponse = _reflection.GeneratedProtocolMessageType('ListTopBannersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOPBANNERSRESPONSE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:grpcServer.ListTopBannersResponse)
  })
_sym_db.RegisterMessage(ListTopBannersResponse)

EditTopBannerResponse = _reflection.GeneratedProtocolMessageType('EditTopBannerResponse', (_message.Message,), {
  'DESCRIPTOR' : _EDITTOPBANNERRESPONSE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:grpcServer.EditTopBannerResponse)
  })
_sym_db.RegisterMessage(EditTopBannerResponse)

CreateTopBannerResponse = _reflection.GeneratedProtocolMessageType('CreateTopBannerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOPBANNERRESPONSE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:grpcServer.CreateTopBannerResponse)
  })
_sym_db.RegisterMessage(CreateTopBannerResponse)

TopBannerMessage = _reflection.GeneratedProtocolMessageType('TopBannerMessage', (_message.Message,), {
  'DESCRIPTOR' : _TOPBANNERMESSAGE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:grpcServer.TopBannerMessage)
  })
_sym_db.RegisterMessage(TopBannerMessage)


DESCRIPTOR._options = None

_TOPBANNER = _descriptor.ServiceDescriptor(
  name='TopBanner',
  full_name='grpcServer.TopBanner',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1040,
  serialized_end=1401,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTopBanner',
    full_name='grpcServer.TopBanner.GetTopBanner',
    index=0,
    containing_service=None,
    input_type=_GETTOPBANNERREQUEST,
    output_type=_GETTOPBANNERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListTopBanners',
    full_name='grpcServer.TopBanner.ListTopBanners',
    index=1,
    containing_service=None,
    input_type=_LISTTOPBANNERSREQUEST,
    output_type=_LISTTOPBANNERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditTopBanner',
    full_name='grpcServer.TopBanner.EditTopBanner',
    index=2,
    containing_service=None,
    input_type=_EDITTOPBANNERREQUEST,
    output_type=_EDITTOPBANNERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTopBanner',
    full_name='grpcServer.TopBanner.CreateTopBanner',
    index=3,
    containing_service=None,
    input_type=_CREATETOPBANNERREQUEST,
    output_type=_CREATETOPBANNERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TOPBANNER)

DESCRIPTOR.services_by_name['TopBanner'] = _TOPBANNER

# @@protoc_insertion_point(module_scope)
