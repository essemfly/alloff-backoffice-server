# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/product/topbanner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eprotos/product/topbanner.proto\x12\x06protos\"(\n\x13GetTopBannerRequest\x12\x11\n\tbanner_id\x18\x01 \x01(\t\"6\n\x15ListTopBannersRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"\x87\x02\n\x14\x45\x64itTopBannerRequest\x12\x11\n\tbanner_id\x18\x01 \x01(\t\x12\x19\n\x0c\x62\x61nner_image\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rexhibition_id\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05title\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08subtitle\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07is_live\x18\x06 \x01(\x08H\x04\x88\x01\x01\x12\x13\n\x06weight\x18\x07 \x01(\x05H\x05\x88\x01\x01\x42\x0f\n\r_banner_imageB\x10\n\x0e_exhibition_idB\x08\n\x06_titleB\x0b\n\t_subtitleB\n\n\x08_is_liveB\t\n\x07_weight\"\x87\x01\n\x16\x43reateTopBannerRequest\x12\x14\n\x0c\x62\x61nner_image\x18\x01 \x01(\t\x12\x15\n\rexhibition_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x10\n\x08subtitle\x18\x04 \x01(\t\x12\x0f\n\x07is_live\x18\x05 \x01(\x08\x12\x0e\n\x06weight\x18\x06 \x01(\x05\"@\n\x14GetTopBannerResponse\x12(\n\x06\x62\x61nner\x18\x01 \x01(\x0b\x32\x18.protos.TopBannerMessage\"x\n\x16ListTopBannersResponse\x12)\n\x07\x62\x61nners\x18\x01 \x03(\x0b\x32\x18.protos.TopBannerMessage\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\x14\n\x0ctotal_counts\x18\x04 \x01(\x05\"A\n\x15\x45\x64itTopBannerResponse\x12(\n\x06\x62\x61nner\x18\x01 \x01(\x0b\x32\x18.protos.TopBannerMessage\"C\n\x17\x43reateTopBannerResponse\x12(\n\x06\x62\x61nner\x18\x01 \x01(\x0b\x32\x18.protos.TopBannerMessage\"\x94\x01\n\x10TopBannerMessage\x12\x11\n\tbanner_id\x18\x01 \x01(\t\x12\x14\n\x0c\x62\x61nner_image\x18\x02 \x01(\t\x12\x15\n\rexhibition_id\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x10\n\x08subtitle\x18\x05 \x01(\t\x12\x0f\n\x07is_live\x18\x06 \x01(\x08\x12\x0e\n\x06weight\x18\x07 \x01(\x05\x32\xc9\x02\n\tTopBanner\x12I\n\x0cGetTopBanner\x12\x1b.protos.GetTopBannerRequest\x1a\x1c.protos.GetTopBannerResponse\x12O\n\x0eListTopBanners\x12\x1d.protos.ListTopBannersRequest\x1a\x1e.protos.ListTopBannersResponse\x12L\n\rEditTopBanner\x12\x1c.protos.EditTopBannerRequest\x1a\x1d.protos.EditTopBannerResponse\x12R\n\x0f\x43reateTopBanner\x12\x1e.protos.CreateTopBannerRequest\x1a\x1f.protos.CreateTopBannerResponseB1Z/github.com/lessbutter/alloff-api/api/grpcServerb\x06proto3')



_GETTOPBANNERREQUEST = DESCRIPTOR.message_types_by_name['GetTopBannerRequest']
_LISTTOPBANNERSREQUEST = DESCRIPTOR.message_types_by_name['ListTopBannersRequest']
_EDITTOPBANNERREQUEST = DESCRIPTOR.message_types_by_name['EditTopBannerRequest']
_CREATETOPBANNERREQUEST = DESCRIPTOR.message_types_by_name['CreateTopBannerRequest']
_GETTOPBANNERRESPONSE = DESCRIPTOR.message_types_by_name['GetTopBannerResponse']
_LISTTOPBANNERSRESPONSE = DESCRIPTOR.message_types_by_name['ListTopBannersResponse']
_EDITTOPBANNERRESPONSE = DESCRIPTOR.message_types_by_name['EditTopBannerResponse']
_CREATETOPBANNERRESPONSE = DESCRIPTOR.message_types_by_name['CreateTopBannerResponse']
_TOPBANNERMESSAGE = DESCRIPTOR.message_types_by_name['TopBannerMessage']
GetTopBannerRequest = _reflection.GeneratedProtocolMessageType('GetTopBannerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTOPBANNERREQUEST,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetTopBannerRequest)
  })
_sym_db.RegisterMessage(GetTopBannerRequest)

ListTopBannersRequest = _reflection.GeneratedProtocolMessageType('ListTopBannersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOPBANNERSREQUEST,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:protos.ListTopBannersRequest)
  })
_sym_db.RegisterMessage(ListTopBannersRequest)

EditTopBannerRequest = _reflection.GeneratedProtocolMessageType('EditTopBannerRequest', (_message.Message,), {
  'DESCRIPTOR' : _EDITTOPBANNERREQUEST,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:protos.EditTopBannerRequest)
  })
_sym_db.RegisterMessage(EditTopBannerRequest)

CreateTopBannerRequest = _reflection.GeneratedProtocolMessageType('CreateTopBannerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOPBANNERREQUEST,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:protos.CreateTopBannerRequest)
  })
_sym_db.RegisterMessage(CreateTopBannerRequest)

GetTopBannerResponse = _reflection.GeneratedProtocolMessageType('GetTopBannerResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTOPBANNERRESPONSE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetTopBannerResponse)
  })
_sym_db.RegisterMessage(GetTopBannerResponse)

ListTopBannersResponse = _reflection.GeneratedProtocolMessageType('ListTopBannersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOPBANNERSRESPONSE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:protos.ListTopBannersResponse)
  })
_sym_db.RegisterMessage(ListTopBannersResponse)

EditTopBannerResponse = _reflection.GeneratedProtocolMessageType('EditTopBannerResponse', (_message.Message,), {
  'DESCRIPTOR' : _EDITTOPBANNERRESPONSE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:protos.EditTopBannerResponse)
  })
_sym_db.RegisterMessage(EditTopBannerResponse)

CreateTopBannerResponse = _reflection.GeneratedProtocolMessageType('CreateTopBannerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOPBANNERRESPONSE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:protos.CreateTopBannerResponse)
  })
_sym_db.RegisterMessage(CreateTopBannerResponse)

TopBannerMessage = _reflection.GeneratedProtocolMessageType('TopBannerMessage', (_message.Message,), {
  'DESCRIPTOR' : _TOPBANNERMESSAGE,
  '__module__' : 'protos.product.topbanner_pb2'
  # @@protoc_insertion_point(class_scope:protos.TopBannerMessage)
  })
_sym_db.RegisterMessage(TopBannerMessage)

_TOPBANNER = DESCRIPTOR.services_by_name['TopBanner']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/lessbutter/alloff-api/api/grpcServer'
  _GETTOPBANNERREQUEST._serialized_start=42
  _GETTOPBANNERREQUEST._serialized_end=82
  _LISTTOPBANNERSREQUEST._serialized_start=84
  _LISTTOPBANNERSREQUEST._serialized_end=138
  _EDITTOPBANNERREQUEST._serialized_start=141
  _EDITTOPBANNERREQUEST._serialized_end=404
  _CREATETOPBANNERREQUEST._serialized_start=407
  _CREATETOPBANNERREQUEST._serialized_end=542
  _GETTOPBANNERRESPONSE._serialized_start=544
  _GETTOPBANNERRESPONSE._serialized_end=608
  _LISTTOPBANNERSRESPONSE._serialized_start=610
  _LISTTOPBANNERSRESPONSE._serialized_end=730
  _EDITTOPBANNERRESPONSE._serialized_start=732
  _EDITTOPBANNERRESPONSE._serialized_end=797
  _CREATETOPBANNERRESPONSE._serialized_start=799
  _CREATETOPBANNERRESPONSE._serialized_end=866
  _TOPBANNERMESSAGE._serialized_start=869
  _TOPBANNERMESSAGE._serialized_end=1017
  _TOPBANNER._serialized_start=1020
  _TOPBANNER._serialized_end=1349
# @@protoc_insertion_point(module_scope)
