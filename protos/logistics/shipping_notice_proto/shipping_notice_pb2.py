# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logistics/protos/shipping_notice_proto/shipping_notice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.logistics.shipping_notice_item_proto import (
    shipping_notice_item_pb2 as logistics_dot_protos_dot_shipping__notice__item__proto_dot_shipping__notice__item__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="logistics/protos/shipping_notice_proto/shipping_notice.proto",
    package="shipping_notice",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n<logistics/protos/shipping_notice_proto/shipping_notice.proto\x12\x0fshipping_notice\x1a\x1bgoogle/protobuf/empty.proto\x1a\x46logistics/protos/shipping_notice_item_proto/shipping_notice_item.proto"\xbb\x03\n\x0eShippingNotice\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x44\n\x06status\x18\x03 \x01(\x0e\x32\x34.shipping_notice.ShippingNotice.ShippingNoticeStatus\x12\x19\n\x0ctemplate_url\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tlocked_at\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tsealed_at\x18\x06 \x01(\tH\x02\x88\x01\x01\x12\x17\n\nshipped_at\x18\x07 \x01(\tH\x03\x88\x01\x01\x12\x12\n\ncreated_at\x18\x08 \x01(\t\x12\x12\n\nupdated_at\x18\t \x01(\t\x12\x37\n\x05items\x18\n \x03(\x0b\x32(.shipping_notice_item.ShippingNoticeItem"H\n\x14ShippingNoticeStatus\x12\x0b\n\x07\x43REATED\x10\x00\x12\n\n\x06LOCKED\x10\x01\x12\n\n\x06SEALED\x10\x02\x12\x0b\n\x07SHIPPED\x10\x03\x42\x0f\n\r_template_urlB\x0c\n\n_locked_atB\x0c\n\n_sealed_atB\r\n\x0b_shipped_at"\x1b\n\x19ShippingNoticeListRequest"+\n\x1dShippingNoticeRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xb4\x03\n\x18ShippingNoticeController\x12W\n\x04List\x12*.shipping_notice.ShippingNoticeListRequest\x1a\x1f.shipping_notice.ShippingNotice"\x00\x30\x01\x12L\n\x06\x43reate\x12\x1f.shipping_notice.ShippingNotice\x1a\x1f.shipping_notice.ShippingNotice"\x00\x12]\n\x08Retrieve\x12..shipping_notice.ShippingNoticeRetrieveRequest\x1a\x1f.shipping_notice.ShippingNotice"\x00\x12L\n\x06Update\x12\x1f.shipping_notice.ShippingNotice\x1a\x1f.shipping_notice.ShippingNotice"\x00\x12\x44\n\x07\x44\x65stroy\x12\x1f.shipping_notice.ShippingNotice\x1a\x16.google.protobuf.Empty"\x00\x62\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        logistics_dot_protos_dot_shipping__notice__item__proto_dot_shipping__notice__item__pb2.DESCRIPTOR,
    ],
)


_SHIPPINGNOTICE_SHIPPINGNOTICESTATUS = _descriptor.EnumDescriptor(
    name="ShippingNoticeStatus",
    full_name="shipping_notice.ShippingNotice.ShippingNoticeStatus",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CREATED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOCKED",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEALED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SHIPPED",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=494,
    serialized_end=566,
)
_sym_db.RegisterEnumDescriptor(_SHIPPINGNOTICE_SHIPPINGNOTICESTATUS)


_SHIPPINGNOTICE = _descriptor.Descriptor(
    name="ShippingNotice",
    full_name="shipping_notice.ShippingNotice",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="shipping_notice.ShippingNotice.id",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="code",
            full_name="shipping_notice.ShippingNotice.code",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="status",
            full_name="shipping_notice.ShippingNotice.status",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="template_url",
            full_name="shipping_notice.ShippingNotice.template_url",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="locked_at",
            full_name="shipping_notice.ShippingNotice.locked_at",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="sealed_at",
            full_name="shipping_notice.ShippingNotice.sealed_at",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="shipped_at",
            full_name="shipping_notice.ShippingNotice.shipped_at",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="created_at",
            full_name="shipping_notice.ShippingNotice.created_at",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="updated_at",
            full_name="shipping_notice.ShippingNotice.updated_at",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="items",
            full_name="shipping_notice.ShippingNotice.items",
            index=9,
            number=10,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _SHIPPINGNOTICE_SHIPPINGNOTICESTATUS,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="_template_url",
            full_name="shipping_notice.ShippingNotice._template_url",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_locked_at",
            full_name="shipping_notice.ShippingNotice._locked_at",
            index=1,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_sealed_at",
            full_name="shipping_notice.ShippingNotice._sealed_at",
            index=2,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_shipped_at",
            full_name="shipping_notice.ShippingNotice._shipped_at",
            index=3,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=183,
    serialized_end=626,
)


_SHIPPINGNOTICELISTREQUEST = _descriptor.Descriptor(
    name="ShippingNoticeListRequest",
    full_name="shipping_notice.ShippingNoticeListRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=628,
    serialized_end=655,
)


_SHIPPINGNOTICERETRIEVEREQUEST = _descriptor.Descriptor(
    name="ShippingNoticeRetrieveRequest",
    full_name="shipping_notice.ShippingNoticeRetrieveRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="shipping_notice.ShippingNoticeRetrieveRequest.id",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=657,
    serialized_end=700,
)

_SHIPPINGNOTICE.fields_by_name[
    "status"
].enum_type = _SHIPPINGNOTICE_SHIPPINGNOTICESTATUS
_SHIPPINGNOTICE.fields_by_name[
    "items"
].message_type = (
    logistics_dot_protos_dot_shipping__notice__item__proto_dot_shipping__notice__item__pb2._SHIPPINGNOTICEITEM
)
_SHIPPINGNOTICE_SHIPPINGNOTICESTATUS.containing_type = _SHIPPINGNOTICE
_SHIPPINGNOTICE.oneofs_by_name["_template_url"].fields.append(
    _SHIPPINGNOTICE.fields_by_name["template_url"]
)
_SHIPPINGNOTICE.fields_by_name[
    "template_url"
].containing_oneof = _SHIPPINGNOTICE.oneofs_by_name["_template_url"]
_SHIPPINGNOTICE.oneofs_by_name["_locked_at"].fields.append(
    _SHIPPINGNOTICE.fields_by_name["locked_at"]
)
_SHIPPINGNOTICE.fields_by_name[
    "locked_at"
].containing_oneof = _SHIPPINGNOTICE.oneofs_by_name["_locked_at"]
_SHIPPINGNOTICE.oneofs_by_name["_sealed_at"].fields.append(
    _SHIPPINGNOTICE.fields_by_name["sealed_at"]
)
_SHIPPINGNOTICE.fields_by_name[
    "sealed_at"
].containing_oneof = _SHIPPINGNOTICE.oneofs_by_name["_sealed_at"]
_SHIPPINGNOTICE.oneofs_by_name["_shipped_at"].fields.append(
    _SHIPPINGNOTICE.fields_by_name["shipped_at"]
)
_SHIPPINGNOTICE.fields_by_name[
    "shipped_at"
].containing_oneof = _SHIPPINGNOTICE.oneofs_by_name["_shipped_at"]
DESCRIPTOR.message_types_by_name["ShippingNotice"] = _SHIPPINGNOTICE
DESCRIPTOR.message_types_by_name[
    "ShippingNoticeListRequest"
] = _SHIPPINGNOTICELISTREQUEST
DESCRIPTOR.message_types_by_name[
    "ShippingNoticeRetrieveRequest"
] = _SHIPPINGNOTICERETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShippingNotice = _reflection.GeneratedProtocolMessageType(
    "ShippingNotice",
    (_message.Message,),
    {
        "DESCRIPTOR": _SHIPPINGNOTICE,
        "__module__": "protos.logistics.shipping_notice_proto.shipping_notice_pb2"
        # @@protoc_insertion_point(class_scope:shipping_notice.ShippingNotice)
    },
)
_sym_db.RegisterMessage(ShippingNotice)

ShippingNoticeListRequest = _reflection.GeneratedProtocolMessageType(
    "ShippingNoticeListRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SHIPPINGNOTICELISTREQUEST,
        "__module__": "protos.logistics.shipping_notice_proto.shipping_notice_pb2"
        # @@protoc_insertion_point(class_scope:shipping_notice.ShippingNoticeListRequest)
    },
)
_sym_db.RegisterMessage(ShippingNoticeListRequest)

ShippingNoticeRetrieveRequest = _reflection.GeneratedProtocolMessageType(
    "ShippingNoticeRetrieveRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SHIPPINGNOTICERETRIEVEREQUEST,
        "__module__": "protos.logistics.shipping_notice_proto.shipping_notice_pb2"
        # @@protoc_insertion_point(class_scope:shipping_notice.ShippingNoticeRetrieveRequest)
    },
)
_sym_db.RegisterMessage(ShippingNoticeRetrieveRequest)


_SHIPPINGNOTICECONTROLLER = _descriptor.ServiceDescriptor(
    name="ShippingNoticeController",
    full_name="shipping_notice.ShippingNoticeController",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=703,
    serialized_end=1139,
    methods=[
        _descriptor.MethodDescriptor(
            name="List",
            full_name="shipping_notice.ShippingNoticeController.List",
            index=0,
            containing_service=None,
            input_type=_SHIPPINGNOTICELISTREQUEST,
            output_type=_SHIPPINGNOTICE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Create",
            full_name="shipping_notice.ShippingNoticeController.Create",
            index=1,
            containing_service=None,
            input_type=_SHIPPINGNOTICE,
            output_type=_SHIPPINGNOTICE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Retrieve",
            full_name="shipping_notice.ShippingNoticeController.Retrieve",
            index=2,
            containing_service=None,
            input_type=_SHIPPINGNOTICERETRIEVEREQUEST,
            output_type=_SHIPPINGNOTICE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Update",
            full_name="shipping_notice.ShippingNoticeController.Update",
            index=3,
            containing_service=None,
            input_type=_SHIPPINGNOTICE,
            output_type=_SHIPPINGNOTICE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Destroy",
            full_name="shipping_notice.ShippingNoticeController.Destroy",
            index=4,
            containing_service=None,
            input_type=_SHIPPINGNOTICE,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SHIPPINGNOTICECONTROLLER)

DESCRIPTOR.services_by_name["ShippingNoticeController"] = _SHIPPINGNOTICECONTROLLER

# @@protoc_insertion_point(module_scope)
