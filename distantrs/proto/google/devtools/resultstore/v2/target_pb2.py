# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/resultstore/v2/target.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from distantrs.proto.google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
from distantrs.proto.google.devtools.resultstore.v2 import file_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/resultstore/v2/target.proto',
  package='google.devtools.resultstore.v2',
  syntax='proto3',
  serialized_options=b'\n\"com.google.devtools.resultstore.v2P\001ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+google/devtools/resultstore/v2/target.proto\x12\x1egoogle.devtools.resultstore.v2\x1a+google/devtools/resultstore/v2/common.proto\x1a)google/devtools/resultstore/v2/file.proto\"\x9c\x04\n\x06Target\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x02id\x18\x02 \x01(\x0b\x32).google.devtools.resultstore.v2.Target.Id\x12K\n\x11status_attributes\x18\x03 \x01(\x0b\x32\x30.google.devtools.resultstore.v2.StatusAttributes\x12\x36\n\x06timing\x18\x04 \x01(\x0b\x32&.google.devtools.resultstore.v2.Timing\x12K\n\x11target_attributes\x18\x05 \x01(\x0b\x32\x30.google.devtools.resultstore.v2.TargetAttributes\x12G\n\x0ftest_attributes\x18\x06 \x01(\x0b\x32..google.devtools.resultstore.v2.TestAttributes\x12<\n\nproperties\x18\x07 \x03(\x0b\x32(.google.devtools.resultstore.v2.Property\x12\x33\n\x05\x66iles\x18\x08 \x03(\x0b\x32$.google.devtools.resultstore.v2.File\x12\x0f\n\x07visible\x18\n \x01(\x08\x1a.\n\x02Id\x12\x15\n\rinvocation_id\x18\x01 \x01(\t\x12\x11\n\ttarget_id\x18\x02 \x01(\t\"\x96\x01\n\x10TargetAttributes\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.google.devtools.resultstore.v2.TargetType\x12:\n\x08language\x18\x02 \x01(\x0e\x32(.google.devtools.resultstore.v2.Language\x12\x0c\n\x04tags\x18\x03 \x03(\t\"H\n\x0eTestAttributes\x12\x36\n\x04size\x18\x01 \x01(\x0e\x32(.google.devtools.resultstore.v2.TestSize*j\n\nTargetType\x12\x1b\n\x17TARGET_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x41PPLICATION\x10\x01\x12\n\n\x06\x42INARY\x10\x02\x12\x0b\n\x07LIBRARY\x10\x03\x12\x0b\n\x07PACKAGE\x10\x04\x12\x08\n\x04TEST\x10\x05*e\n\x08TestSize\x12\x19\n\x15TEST_SIZE_UNSPECIFIED\x10\x00\x12\t\n\x05SMALL\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\t\n\x05LARGE\x10\x03\x12\x0c\n\x08\x45NORMOUS\x10\x04\x12\x0e\n\nOTHER_SIZE\x10\x05\x42q\n\"com.google.devtools.resultstore.v2P\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3'
  ,
  dependencies=[google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2.DESCRIPTOR,google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2.DESCRIPTOR,])

_TARGETTYPE = _descriptor.EnumDescriptor(
  name='TargetType',
  full_name='google.devtools.resultstore.v2.TargetType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TARGET_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPLICATION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BINARY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LIBRARY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEST', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=937,
  serialized_end=1043,
)
_sym_db.RegisterEnumDescriptor(_TARGETTYPE)

TargetType = enum_type_wrapper.EnumTypeWrapper(_TARGETTYPE)
_TESTSIZE = _descriptor.EnumDescriptor(
  name='TestSize',
  full_name='google.devtools.resultstore.v2.TestSize',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEST_SIZE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SMALL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LARGE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENORMOUS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTHER_SIZE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1045,
  serialized_end=1146,
)
_sym_db.RegisterEnumDescriptor(_TESTSIZE)

TestSize = enum_type_wrapper.EnumTypeWrapper(_TESTSIZE)
TARGET_TYPE_UNSPECIFIED = 0
APPLICATION = 1
BINARY = 2
LIBRARY = 3
PACKAGE = 4
TEST = 5
TEST_SIZE_UNSPECIFIED = 0
SMALL = 1
MEDIUM = 2
LARGE = 3
ENORMOUS = 4
OTHER_SIZE = 5



_TARGET_ID = _descriptor.Descriptor(
  name='Id',
  full_name='google.devtools.resultstore.v2.Target.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='invocation_id', full_name='google.devtools.resultstore.v2.Target.Id.invocation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='google.devtools.resultstore.v2.Target.Id.target_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=662,
  serialized_end=708,
)

_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='google.devtools.resultstore.v2.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.resultstore.v2.Target.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.devtools.resultstore.v2.Target.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_attributes', full_name='google.devtools.resultstore.v2.Target.status_attributes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timing', full_name='google.devtools.resultstore.v2.Target.timing', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_attributes', full_name='google.devtools.resultstore.v2.Target.target_attributes', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_attributes', full_name='google.devtools.resultstore.v2.Target.test_attributes', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='google.devtools.resultstore.v2.Target.properties', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='files', full_name='google.devtools.resultstore.v2.Target.files', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visible', full_name='google.devtools.resultstore.v2.Target.visible', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TARGET_ID, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=708,
)


_TARGETATTRIBUTES = _descriptor.Descriptor(
  name='TargetAttributes',
  full_name='google.devtools.resultstore.v2.TargetAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='google.devtools.resultstore.v2.TargetAttributes.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='google.devtools.resultstore.v2.TargetAttributes.language', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='google.devtools.resultstore.v2.TargetAttributes.tags', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=711,
  serialized_end=861,
)


_TESTATTRIBUTES = _descriptor.Descriptor(
  name='TestAttributes',
  full_name='google.devtools.resultstore.v2.TestAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='google.devtools.resultstore.v2.TestAttributes.size', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=863,
  serialized_end=935,
)

_TARGET_ID.containing_type = _TARGET
_TARGET.fields_by_name['id'].message_type = _TARGET_ID
_TARGET.fields_by_name['status_attributes'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2._STATUSATTRIBUTES
_TARGET.fields_by_name['timing'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2._TIMING
_TARGET.fields_by_name['target_attributes'].message_type = _TARGETATTRIBUTES
_TARGET.fields_by_name['test_attributes'].message_type = _TESTATTRIBUTES
_TARGET.fields_by_name['properties'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2._PROPERTY
_TARGET.fields_by_name['files'].message_type = google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2._FILE
_TARGETATTRIBUTES.fields_by_name['type'].enum_type = _TARGETTYPE
_TARGETATTRIBUTES.fields_by_name['language'].enum_type = google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2._LANGUAGE
_TESTATTRIBUTES.fields_by_name['size'].enum_type = _TESTSIZE
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
DESCRIPTOR.message_types_by_name['TargetAttributes'] = _TARGETATTRIBUTES
DESCRIPTOR.message_types_by_name['TestAttributes'] = _TESTATTRIBUTES
DESCRIPTOR.enum_types_by_name['TargetType'] = _TARGETTYPE
DESCRIPTOR.enum_types_by_name['TestSize'] = _TESTSIZE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {

  'Id' : _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
    'DESCRIPTOR' : _TARGET_ID,
    '__module__' : 'google.devtools.resultstore.v2.target_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.Target.Id)
    })
  ,
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'google.devtools.resultstore.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.Target)
  })
_sym_db.RegisterMessage(Target)
_sym_db.RegisterMessage(Target.Id)

TargetAttributes = _reflection.GeneratedProtocolMessageType('TargetAttributes', (_message.Message,), {
  'DESCRIPTOR' : _TARGETATTRIBUTES,
  '__module__' : 'google.devtools.resultstore.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.TargetAttributes)
  })
_sym_db.RegisterMessage(TargetAttributes)

TestAttributes = _reflection.GeneratedProtocolMessageType('TestAttributes', (_message.Message,), {
  'DESCRIPTOR' : _TESTATTRIBUTES,
  '__module__' : 'google.devtools.resultstore.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.TestAttributes)
  })
_sym_db.RegisterMessage(TestAttributes)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
