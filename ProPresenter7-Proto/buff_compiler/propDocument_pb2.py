# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: propDocument.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2
import cue_pb2 as cue__pb2
import effects_pb2 as effects__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12propDocument.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\x1a\tcue.proto\x1a\reffects.proto\"\x87\x01\n\x0cPropDocument\x12\x32\n\x10\x61pplication_info\x18\x01 \x01(\x0b\x32\x18.rv.data.ApplicationInfo\x12\x1a\n\x04\x63ues\x18\x02 \x03(\x0b\x32\x0c.rv.data.Cue\x12\'\n\ntransition\x18\x03 \x01(\x0b\x32\x13.rv.data.Transitionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'propDocument_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PROPDOCUMENT']._serialized_start=76
  _globals['_PROPDOCUMENT']._serialized_end=211
# @@protoc_insertion_point(module_scope)
