# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/bazel_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from distantrs.proto.proto import context_pb2 as proto_dot_context__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/bazel_config.proto',
  package='bazel_config',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18proto/bazel_config.proto\x12\x0c\x62\x61zel_config\x1a\x13proto/context.proto\"]\n\x0c\x43onfigOption\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\x12\x18\n\x10option_lifecycle\x18\x02 \x01(\t\x12\x11\n\tflag_name\x18\x03 \x01(\t\x12\x12\n\nflag_value\x18\x04 \x01(\t\"i\n\x15GetBazelConfigRequest\x12\x30\n\x0frequest_context\x18\x01 \x01(\x0b\x32\x17.context.RequestContext\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x10\n\x08protocol\x18\x03 \x01(\t\"\x7f\n\x16GetBazelConfigResponse\x12\x32\n\x10response_context\x18\x01 \x01(\x0b\x32\x18.context.ResponseContext\x12\x31\n\rconfig_option\x18\x02 \x03(\x0b\x32\x1a.bazel_config.ConfigOptionb\x06proto3'
  ,
  dependencies=[proto_dot_context__pb2.DESCRIPTOR,])




_CONFIGOPTION = _descriptor.Descriptor(
  name='ConfigOption',
  full_name='bazel_config.ConfigOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='bazel_config.ConfigOption.body', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='option_lifecycle', full_name='bazel_config.ConfigOption.option_lifecycle', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flag_name', full_name='bazel_config.ConfigOption.flag_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flag_value', full_name='bazel_config.ConfigOption.flag_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=63,
  serialized_end=156,
)


_GETBAZELCONFIGREQUEST = _descriptor.Descriptor(
  name='GetBazelConfigRequest',
  full_name='bazel_config.GetBazelConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_context', full_name='bazel_config.GetBazelConfigRequest.request_context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='bazel_config.GetBazelConfigRequest.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='bazel_config.GetBazelConfigRequest.protocol', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=158,
  serialized_end=263,
)


_GETBAZELCONFIGRESPONSE = _descriptor.Descriptor(
  name='GetBazelConfigResponse',
  full_name='bazel_config.GetBazelConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_context', full_name='bazel_config.GetBazelConfigResponse.response_context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config_option', full_name='bazel_config.GetBazelConfigResponse.config_option', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  ],
  serialized_start=265,
  serialized_end=392,
)

_GETBAZELCONFIGREQUEST.fields_by_name['request_context'].message_type = proto_dot_context__pb2._REQUESTCONTEXT
_GETBAZELCONFIGRESPONSE.fields_by_name['response_context'].message_type = proto_dot_context__pb2._RESPONSECONTEXT
_GETBAZELCONFIGRESPONSE.fields_by_name['config_option'].message_type = _CONFIGOPTION
DESCRIPTOR.message_types_by_name['ConfigOption'] = _CONFIGOPTION
DESCRIPTOR.message_types_by_name['GetBazelConfigRequest'] = _GETBAZELCONFIGREQUEST
DESCRIPTOR.message_types_by_name['GetBazelConfigResponse'] = _GETBAZELCONFIGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigOption = _reflection.GeneratedProtocolMessageType('ConfigOption', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGOPTION,
  '__module__' : 'proto.bazel_config_pb2'
  # @@protoc_insertion_point(class_scope:bazel_config.ConfigOption)
  })
_sym_db.RegisterMessage(ConfigOption)

GetBazelConfigRequest = _reflection.GeneratedProtocolMessageType('GetBazelConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBAZELCONFIGREQUEST,
  '__module__' : 'proto.bazel_config_pb2'
  # @@protoc_insertion_point(class_scope:bazel_config.GetBazelConfigRequest)
  })
_sym_db.RegisterMessage(GetBazelConfigRequest)

GetBazelConfigResponse = _reflection.GeneratedProtocolMessageType('GetBazelConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBAZELCONFIGRESPONSE,
  '__module__' : 'proto.bazel_config_pb2'
  # @@protoc_insertion_point(class_scope:bazel_config.GetBazelConfigResponse)
  })
_sym_db.RegisterMessage(GetBazelConfigResponse)


# @@protoc_insertion_point(module_scope)