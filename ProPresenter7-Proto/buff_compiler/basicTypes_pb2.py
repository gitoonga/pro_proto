# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basicTypes.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62\x61sicTypes.proto\x12\x07rv.data\"\xfb\x07\n\x03URL\x12\'\n\x08platform\x18\x03 \x01(\x0e\x32\x15.rv.data.URL.Platform\x12\x19\n\x0f\x61\x62solute_string\x18\x01 \x01(\tH\x00\x12\x17\n\rrelative_path\x18\x02 \x01(\tH\x00\x12/\n\x05local\x18\x04 \x01(\x0b\x32\x1e.rv.data.URL.LocalRelativePathH\x01\x12\x35\n\x08\x65xternal\x18\x05 \x01(\x0b\x32!.rv.data.URL.ExternalRelativePathH\x01\x1a\xfb\x02\n\x11LocalRelativePath\x12\x31\n\x04root\x18\x01 \x01(\x0e\x32#.rv.data.URL.LocalRelativePath.Root\x12\x0c\n\x04path\x18\x02 \x01(\t\"\xa4\x02\n\x04Root\x12\x10\n\x0cROOT_UNKNOWN\x10\x00\x12\x14\n\x10ROOT_BOOT_VOLUME\x10\x01\x12\x12\n\x0eROOT_USER_HOME\x10\x02\x12\x17\n\x13ROOT_USER_DOCUMENTS\x10\x03\x12\x17\n\x13ROOT_USER_DOWNLOADS\x10\x04\x12\x13\n\x0fROOT_USER_MUSIC\x10\x05\x12\x16\n\x12ROOT_USER_PICTURES\x10\x06\x12\x14\n\x10ROOT_USER_VIDEOS\x10\x07\x12\x15\n\x11ROOT_USER_DESKTOP\x10\x0b\x12\x19\n\x15ROOT_USER_APP_SUPPORT\x10\x08\x12\x0f\n\x0bROOT_SHARED\x10\t\x12\r\n\tROOT_SHOW\x10\n\x12\x19\n\x15ROOT_CURRENT_RESOURCE\x10\x0c\x1a\xb5\x02\n\x14\x45xternalRelativePath\x12\x44\n\x05macos\x18\x01 \x01(\x0b\x32\x35.rv.data.URL.ExternalRelativePath.MacOSExternalVolume\x12\x44\n\x05win32\x18\x02 \x01(\x0b\x32\x35.rv.data.URL.ExternalRelativePath.Win32ExternalVolume\x12\x0c\n\x04path\x18\x03 \x01(\t\x1a*\n\x13MacOSExternalVolume\x12\x13\n\x0bvolume_name\x18\x01 \x01(\t\x1aW\n\x13Win32ExternalVolume\x12\x14\n\x0c\x64rive_letter\x18\x01 \x01(\t\x12\x13\n\x0bvolume_name\x18\x02 \x01(\t\x12\x15\n\rnetwork_share\x18\x03 \x01(\x08\"Z\n\x08Platform\x12\x14\n\x10PLATFORM_UNKNOWN\x10\x00\x12\x12\n\x0ePLATFORM_MACOS\x10\x01\x12\x12\n\x0ePLATFORM_WIN32\x10\x02\x12\x10\n\x0cPLATFORM_WEB\x10\x03\x42\t\n\x07StorageB\x12\n\x10RelativeFilePath\"\"\n\x04URLs\x12\x1a\n\x04urls\x18\x01 \x03(\x0b\x32\x0c.rv.data.URL\"\x16\n\x04UUID\x12\x0e\n\x06string\x18\x01 \x01(\t\"&\n\x08IntRange\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\"@\n\x05\x43olor\x12\x0b\n\x03red\x18\x01 \x01(\x02\x12\r\n\x05green\x18\x02 \x01(\x02\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x02\x12\r\n\x05\x61lpha\x18\x04 \x01(\x02\"]\n\x07Version\x12\x15\n\rmajor_version\x18\x01 \x01(\r\x12\x15\n\rminor_version\x18\x02 \x01(\r\x12\x15\n\rpatch_version\x18\x03 \x01(\r\x12\r\n\x05\x62uild\x18\x04 \x01(\t\"\xc4\x03\n\x0f\x41pplicationInfo\x12\x33\n\x08platform\x18\x01 \x01(\x0e\x32!.rv.data.ApplicationInfo.Platform\x12*\n\x10platform_version\x18\x02 \x01(\x0b\x32\x10.rv.data.Version\x12\x39\n\x0b\x61pplication\x18\x03 \x01(\x0e\x32$.rv.data.ApplicationInfo.Application\x12-\n\x13\x61pplication_version\x18\x04 \x01(\x0b\x32\x10.rv.data.Version\"L\n\x08Platform\x12\x16\n\x12PLATFORM_UNDEFINED\x10\x00\x12\x12\n\x0ePLATFORM_MACOS\x10\x01\x12\x14\n\x10PLATFORM_WINDOWS\x10\x02\"\x97\x01\n\x0b\x41pplication\x12\x19\n\x15\x41PPLICATION_UNDEFINED\x10\x00\x12\x1c\n\x18\x41PPLICATION_PROPRESENTER\x10\x01\x12\x13\n\x0f\x41PPLICATION_PVP\x10\x02\x12\x1e\n\x1a\x41PPLICATION_PROVIDEOSERVER\x10\x03\x12\x1a\n\x16\x41PPLICATION_SCOREBOARD\x10\x04\"V\n\x15\x43ollectionElementType\x12%\n\x0eparameter_uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x16\n\x0eparameter_name\x18\x02 \x01(\t\"\xf6\x04\n\rMusicKeyScale\x12\x32\n\tmusic_key\x18\x01 \x01(\x0e\x32\x1f.rv.data.MusicKeyScale.MusicKey\x12\x36\n\x0bmusic_scale\x18\x02 \x01(\x0e\x32!.rv.data.MusicKeyScale.MusicScale\"\xbc\x03\n\x08MusicKey\x12\x14\n\x10MUSIC_KEY_A_FLAT\x10\x00\x12\x0f\n\x0bMUSIC_KEY_A\x10\x01\x12\x15\n\x11MUSIC_KEY_A_SHARP\x10\x02\x12\x14\n\x10MUSIC_KEY_B_FLAT\x10\x03\x12\x0f\n\x0bMUSIC_KEY_B\x10\x04\x12\x15\n\x11MUSIC_KEY_B_SHARP\x10\x05\x12\x14\n\x10MUSIC_KEY_C_FLAT\x10\x06\x12\x0f\n\x0bMUSIC_KEY_C\x10\x07\x12\x15\n\x11MUSIC_KEY_C_SHARP\x10\x08\x12\x14\n\x10MUSIC_KEY_D_FLAT\x10\t\x12\x0f\n\x0bMUSIC_KEY_D\x10\n\x12\x15\n\x11MUSIC_KEY_D_SHARP\x10\x0b\x12\x14\n\x10MUSIC_KEY_E_FLAT\x10\x0c\x12\x0f\n\x0bMUSIC_KEY_E\x10\r\x12\x15\n\x11MUSIC_KEY_E_SHARP\x10\x0e\x12\x14\n\x10MUSIC_KEY_F_FLAT\x10\x0f\x12\x0f\n\x0bMUSIC_KEY_F\x10\x10\x12\x15\n\x11MUSIC_KEY_F_SHARP\x10\x11\x12\x14\n\x10MUSIC_KEY_G_FLAT\x10\x12\x12\x0f\n\x0bMUSIC_KEY_G\x10\x13\x12\x15\n\x11MUSIC_KEY_G_SHARP\x10\x14\":\n\nMusicScale\x12\x15\n\x11MUSIC_SCALE_MAJOR\x10\x00\x12\x15\n\x11MUSIC_SCALE_MINOR\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'basicTypes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_URL']._serialized_start=30
  _globals['_URL']._serialized_end=1049
  _globals['_URL_LOCALRELATIVEPATH']._serialized_start=235
  _globals['_URL_LOCALRELATIVEPATH']._serialized_end=614
  _globals['_URL_LOCALRELATIVEPATH_ROOT']._serialized_start=322
  _globals['_URL_LOCALRELATIVEPATH_ROOT']._serialized_end=614
  _globals['_URL_EXTERNALRELATIVEPATH']._serialized_start=617
  _globals['_URL_EXTERNALRELATIVEPATH']._serialized_end=926
  _globals['_URL_EXTERNALRELATIVEPATH_MACOSEXTERNALVOLUME']._serialized_start=795
  _globals['_URL_EXTERNALRELATIVEPATH_MACOSEXTERNALVOLUME']._serialized_end=837
  _globals['_URL_EXTERNALRELATIVEPATH_WIN32EXTERNALVOLUME']._serialized_start=839
  _globals['_URL_EXTERNALRELATIVEPATH_WIN32EXTERNALVOLUME']._serialized_end=926
  _globals['_URL_PLATFORM']._serialized_start=928
  _globals['_URL_PLATFORM']._serialized_end=1018
  _globals['_URLS']._serialized_start=1051
  _globals['_URLS']._serialized_end=1085
  _globals['_UUID']._serialized_start=1087
  _globals['_UUID']._serialized_end=1109
  _globals['_INTRANGE']._serialized_start=1111
  _globals['_INTRANGE']._serialized_end=1149
  _globals['_COLOR']._serialized_start=1151
  _globals['_COLOR']._serialized_end=1215
  _globals['_VERSION']._serialized_start=1217
  _globals['_VERSION']._serialized_end=1310
  _globals['_APPLICATIONINFO']._serialized_start=1313
  _globals['_APPLICATIONINFO']._serialized_end=1765
  _globals['_APPLICATIONINFO_PLATFORM']._serialized_start=1535
  _globals['_APPLICATIONINFO_PLATFORM']._serialized_end=1611
  _globals['_APPLICATIONINFO_APPLICATION']._serialized_start=1614
  _globals['_APPLICATIONINFO_APPLICATION']._serialized_end=1765
  _globals['_COLLECTIONELEMENTTYPE']._serialized_start=1767
  _globals['_COLLECTIONELEMENTTYPE']._serialized_end=1853
  _globals['_MUSICKEYSCALE']._serialized_start=1856
  _globals['_MUSICKEYSCALE']._serialized_end=2486
  _globals['_MUSICKEYSCALE_MUSICKEY']._serialized_start=1982
  _globals['_MUSICKEYSCALE_MUSICKEY']._serialized_end=2426
  _globals['_MUSICKEYSCALE_MUSICSCALE']._serialized_start=2428
  _globals['_MUSICKEYSCALE_MUSICSCALE']._serialized_end=2486
# @@protoc_insertion_point(module_scope)
