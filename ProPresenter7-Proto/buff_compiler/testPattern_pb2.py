# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: testPattern.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11testPattern.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\"\xec\x04\n\x0bTestPattern\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.rv.data.TestPattern.Type\x12\x34\n\nblend_grid\x18\x02 \x01(\x0b\x32\x1e.rv.data.TestPattern.BlendGridH\x00\x12\x38\n\x0c\x63ustom_color\x18\x03 \x01(\x0b\x32 .rv.data.TestPattern.CustomColorH\x00\x12\x38\n\tintensity\x18\x04 \x01(\x0b\x32#.rv.data.TestPattern.IntensityColorH\x00\x1au\n\tBlendGrid\x12\x11\n\tdraw_grid\x18\x01 \x01(\x08\x12\x14\n\x0c\x64raw_circles\x18\x02 \x01(\x08\x12\x12\n\ndraw_lines\x18\x03 \x01(\x08\x12\x15\n\rinvert_colors\x18\x04 \x01(\x08\x12\x14\n\x0cgrid_spacing\x18\x05 \x01(\x01\x1a,\n\x0b\x43ustomColor\x12\x1d\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x0e.rv.data.Color\x1a#\n\x0eIntensityColor\x12\x11\n\tintensity\x18\x01 \x01(\x01\"\xaa\x01\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x13\n\x0fTYPE_BLEND_GRID\x10\x01\x12\x13\n\x0fTYPE_COLOR_BARS\x10\x02\x12\x0e\n\nTYPE_FOCUS\x10\x03\x12\x13\n\x0fTYPE_GRAY_SCALE\x10\x04\x12\x14\n\x10TYPE_BLACK_COLOR\x10\x05\x12\x14\n\x10TYPE_WHITE_COLOR\x10\x06\x12\x15\n\x11TYPE_CUSTOM_COLOR\x10\x07\x42\x13\n\x11PatternPropertiesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'testPattern_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TESTPATTERN']._serialized_start=49
  _globals['_TESTPATTERN']._serialized_end=669
  _globals['_TESTPATTERN_BLENDGRID']._serialized_start=275
  _globals['_TESTPATTERN_BLENDGRID']._serialized_end=392
  _globals['_TESTPATTERN_CUSTOMCOLOR']._serialized_start=394
  _globals['_TESTPATTERN_CUSTOMCOLOR']._serialized_end=438
  _globals['_TESTPATTERN_INTENSITYCOLOR']._serialized_start=440
  _globals['_TESTPATTERN_INTENSITYCOLOR']._serialized_end=475
  _globals['_TESTPATTERN_TYPE']._serialized_start=478
  _globals['_TESTPATTERN_TYPE']._serialized_end=648
# @@protoc_insertion_point(module_scope)
