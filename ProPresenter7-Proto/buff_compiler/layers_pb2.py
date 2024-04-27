# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: layers.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import hotKey_pb2 as hotKey__pb2
import effects_pb2 as effects__pb2
import basicTypes_pb2 as basicTypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0clayers.proto\x12\x07rv.data\x1a\x0chotKey.proto\x1a\reffects.proto\x1a\x10\x62\x61sicTypes.proto\"\x9d\x13\n\x05Layer\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1d\n\x05\x63olor\x18\x03 \x01(\x0b\x32\x0e.rv.data.Color\x12\r\n\x05muted\x18\x04 \x01(\x08\x12\x0e\n\x06hidden\x18\x05 \x01(\x08\x12,\n\nblend_mode\x18\x06 \x01(\x0e\x32\x18.rv.data.Layer.BlendMode\x12\x0f\n\x07opacity\x18\x07 \x01(\x01\x12/\n\x18selected_target_set_uuid\x18\x08 \x01(\x0b\x32\r.rv.data.UUID\x12*\n\x13\x65\x66\x66\x65\x63ts_preset_uuid\x18\t \x01(\x0b\x32\r.rv.data.UUID\x12\x1e\n\x16\x65\x66\x66\x65\x63ts_build_duration\x18\n \x01(\x01\x12(\n\x11layer_preset_uuid\x18\x0b \x01(\x0b\x32\r.rv.data.UUID\x12 \n\x07hot_key\x18\x0c \x01(\x0b\x32\x0f.rv.data.HotKey\x12\'\n\ntransition\x18\r \x01(\x0b\x32\x13.rv.data.Transition\x12 \n\x07\x65\x66\x66\x65\x63ts\x18\x0e \x03(\x0b\x32\x0f.rv.data.Effect\x12&\n\x05\x62lend\x18\x0f \x01(\x0b\x32\x17.rv.data.Layer.Blending\x1aR\n\x06Preset\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1d\n\x05layer\x18\x03 \x01(\x0b\x32\x0e.rv.data.Layer\x1a\x94\t\n\x08\x42lending\x12\x34\n\x08standard\x18\x01 \x01(\x0b\x32 .rv.data.Layer.Blending.StandardH\x00\x12.\n\x05matte\x18\x02 \x01(\x0b\x32\x1d.rv.data.Layer.Blending.MatteH\x00\x1a\x9c\x06\n\x08Standard\x12\x38\n\x04mode\x18\x01 \x01(\x0e\x32*.rv.data.Layer.Blending.Standard.BlendMode\x12\x0f\n\x07opacity\x18\x02 \x01(\x01\"\xc4\x05\n\tBlendMode\x12\x15\n\x11\x42LEND_MODE_NORMAL\x10\x00\x12\x17\n\x13\x42LEND_MODE_DISSOLVE\x10\x01\x12\x15\n\x11\x42LEND_MODE_DARKEN\x10\x02\x12\x17\n\x13\x42LEND_MODE_MULTIPLY\x10\x03\x12\x19\n\x15\x42LEND_MODE_COLOR_BURN\x10\x04\x12\x1a\n\x16\x42LEND_MODE_LINEAR_BURN\x10\x05\x12\x1b\n\x17\x42LEND_MODE_DARKER_COLOR\x10\x06\x12\x16\n\x12\x42LEND_MODE_LIGHTEN\x10\x07\x12\x15\n\x11\x42LEND_MODE_SCREEN\x10\x08\x12\x1a\n\x16\x42LEND_MODE_COLOR_DODGE\x10\t\x12\x1b\n\x17\x42LEND_MODE_LINEAR_DODGE\x10\n\x12\x1c\n\x18\x42LEND_MODE_LIGHTER_COLOR\x10\x0b\x12\x16\n\x12\x42LEND_MODE_OVERLAY\x10\x0c\x12\x19\n\x15\x42LEND_MODE_SOFT_LIGHT\x10\r\x12\x19\n\x15\x42LEND_MODE_HARD_LIGHT\x10\x0e\x12\x1a\n\x16\x42LEND_MODE_VIVID_LIGHT\x10\x0f\x12\x1b\n\x17\x42LEND_MODE_LINEAR_LIGHT\x10\x10\x12\x18\n\x14\x42LEND_MODE_PIN_LIGHT\x10\x11\x12\x17\n\x13\x42LEND_MODE_HARD_MIX\x10\x12\x12\x19\n\x15\x42LEND_MODE_DIFFERENCE\x10\x13\x12\x18\n\x14\x42LEND_MODE_EXCLUSION\x10\x14\x12\x17\n\x13\x42LEND_MODE_SUBTRACT\x10\x15\x12\x15\n\x11\x42LEND_MODE_DIVIDE\x10\x16\x12\x12\n\x0e\x42LEND_MODE_HUE\x10\x17\x12\x19\n\x15\x42LEND_MODE_SATURATION\x10\x18\x12\x14\n\x10\x42LEND_MODE_COLOR\x10\x19\x12\x19\n\x15\x42LEND_MODE_LUMINOSITY\x10\x1a\x1a\xf2\x01\n\x05Matte\x12\x34\n\x05\x61lpha\x18\x01 \x01(\x0b\x32#.rv.data.Layer.Blending.Matte.AlphaH\x00\x12\x32\n\x04luma\x18\x02 \x01(\x0b\x32\".rv.data.Layer.Blending.Matte.LumaH\x00\x12\x34\n\x05white\x18\x04 \x01(\x0b\x32#.rv.data.Layer.Blending.Matte.WhiteH\x00\x1a\x19\n\x05\x41lpha\x12\x10\n\x08inverted\x18\x01 \x01(\x08\x1a\x18\n\x04Luma\x12\x10\n\x08inverted\x18\x01 \x01(\x08\x1a\x07\n\x05WhiteB\x0b\n\tMatteTypeB\x0e\n\x0c\x42lendingType\"\xc4\x05\n\tBlendMode\x12\x15\n\x11\x42LEND_MODE_NORMAL\x10\x00\x12\x17\n\x13\x42LEND_MODE_DISSOLVE\x10\x01\x12\x15\n\x11\x42LEND_MODE_DARKEN\x10\x02\x12\x17\n\x13\x42LEND_MODE_MULTIPLY\x10\x03\x12\x19\n\x15\x42LEND_MODE_COLOR_BURN\x10\x04\x12\x1a\n\x16\x42LEND_MODE_LINEAR_BURN\x10\x05\x12\x1b\n\x17\x42LEND_MODE_DARKER_COLOR\x10\x06\x12\x16\n\x12\x42LEND_MODE_LIGHTEN\x10\x07\x12\x15\n\x11\x42LEND_MODE_SCREEN\x10\x08\x12\x1a\n\x16\x42LEND_MODE_COLOR_DODGE\x10\t\x12\x1b\n\x17\x42LEND_MODE_LINEAR_DODGE\x10\n\x12\x1c\n\x18\x42LEND_MODE_LIGHTER_COLOR\x10\x0b\x12\x16\n\x12\x42LEND_MODE_OVERLAY\x10\x0c\x12\x19\n\x15\x42LEND_MODE_SOFT_LIGHT\x10\r\x12\x19\n\x15\x42LEND_MODE_HARD_LIGHT\x10\x0e\x12\x1a\n\x16\x42LEND_MODE_VIVID_LIGHT\x10\x0f\x12\x1b\n\x17\x42LEND_MODE_LINEAR_LIGHT\x10\x10\x12\x18\n\x14\x42LEND_MODE_PIN_LIGHT\x10\x11\x12\x17\n\x13\x42LEND_MODE_HARD_MIX\x10\x12\x12\x19\n\x15\x42LEND_MODE_DIFFERENCE\x10\x13\x12\x18\n\x14\x42LEND_MODE_EXCLUSION\x10\x14\x12\x17\n\x13\x42LEND_MODE_SUBTRACT\x10\x15\x12\x15\n\x11\x42LEND_MODE_DIVIDE\x10\x16\x12\x12\n\x0e\x42LEND_MODE_HUE\x10\x17\x12\x19\n\x15\x42LEND_MODE_SATURATION\x10\x18\x12\x14\n\x10\x42LEND_MODE_COLOR\x10\x19\x12\x19\n\x15\x42LEND_MODE_LUMINOSITY\x10\x1a\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'layers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LAYER']._serialized_start=73
  _globals['_LAYER']._serialized_end=2534
  _globals['_LAYER_PRESET']._serialized_start=566
  _globals['_LAYER_PRESET']._serialized_end=648
  _globals['_LAYER_BLENDING']._serialized_start=651
  _globals['_LAYER_BLENDING']._serialized_end=1823
  _globals['_LAYER_BLENDING_STANDARD']._serialized_start=766
  _globals['_LAYER_BLENDING_STANDARD']._serialized_end=1562
  _globals['_LAYER_BLENDING_STANDARD_BLENDMODE']._serialized_start=854
  _globals['_LAYER_BLENDING_STANDARD_BLENDMODE']._serialized_end=1562
  _globals['_LAYER_BLENDING_MATTE']._serialized_start=1565
  _globals['_LAYER_BLENDING_MATTE']._serialized_end=1807
  _globals['_LAYER_BLENDING_MATTE_ALPHA']._serialized_start=1734
  _globals['_LAYER_BLENDING_MATTE_ALPHA']._serialized_end=1759
  _globals['_LAYER_BLENDING_MATTE_LUMA']._serialized_start=1761
  _globals['_LAYER_BLENDING_MATTE_LUMA']._serialized_end=1785
  _globals['_LAYER_BLENDING_MATTE_WHITE']._serialized_start=1787
  _globals['_LAYER_BLENDING_MATTE_WHITE']._serialized_end=1794
  _globals['_LAYER_BLENDMODE']._serialized_start=854
  _globals['_LAYER_BLENDMODE']._serialized_end=1562
# @@protoc_insertion_point(module_scope)
