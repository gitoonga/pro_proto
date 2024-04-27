# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proApiV1BasicTypes.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2
import rvtimestamp_pb2 as rvtimestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proApiV1BasicTypes.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\x1a\x11rvtimestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\">\n\x11\x41PI_v1_Identifier\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\r\"W\n\x11\x41PI_v1_SlideIndex\x12\r\n\x05index\x18\x01 \x01(\r\x12\x33\n\x0fpresentation_id\x18\x02 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\"\xd1\x01\n\x0f\x41PI_v1_Playlist\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12:\n\x04type\x18\x02 \x01(\x0e\x32,.rv.data.API_v1_Playlist.API_v1_PlaylistType\x12*\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\x18.rv.data.API_v1_Playlist\".\n\x13\x41PI_v1_PlaylistType\x12\t\n\x05group\x10\x00\x12\x0c\n\x08playlist\x10\x01\"p\n\x16\x41PI_v1_PlaylistAndItem\x12,\n\x08playlist\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12(\n\x04item\x18\x02 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\"\xf3\x01\n\x18\x41PI_v1_MediaPlaylistItem\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12L\n\x04type\x18\x02 \x01(\x0e\x32>.rv.data.API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType\x12\x0e\n\x06\x61rtist\x18\x03 \x01(\t\x12\x10\n\x08\x64uration\x18\x04 \x01(\r\"?\n\x1c\x41PI_v1_MediaPlaylistItemType\x12\t\n\x05\x61udio\x10\x00\x12\t\n\x05image\x10\x01\x12\t\n\x05video\x10\x02\"\xf0\x02\n\x13\x41PI_v1_PlaylistItem\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x42\n\x04type\x18\x02 \x01(\x0e\x32\x34.rv.data.API_v1_PlaylistItem.API_v1_PlaylistItemType\x12\x11\n\tis_hidden\x18\x03 \x01(\x08\x12\x0e\n\x06is_pco\x18\x04 \x01(\x08\x12+\n\x0cheader_color\x18\x05 \x01(\x0b\x32\x15.rv.data.API_v1_Color\x12.\n\x08\x64uration\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"m\n\x17\x41PI_v1_PlaylistItemType\x12\x10\n\x0cpresentation\x10\x00\x12\x0f\n\x0bplaceholder\x10\x01\x12\n\n\x06header\x10\x02\x12\t\n\x05media\x10\x03\x12\t\n\x05\x61udio\x10\x04\x12\r\n\tlivevideo\x10\x05\"\xc3\x03\n\x11\x41PI_v1_ClearGroup\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12#\n\x04tint\x18\x03 \x01(\x0b\x32\x15.rv.data.API_v1_Color\x12\x45\n\x06layers\x18\x04 \x03(\x0e\x32\x35.rv.data.API_v1_ClearGroup.API_v1_ClearGroupLayerType\x12#\n\x1bstop_timeline_announcements\x18\x05 \x01(\x08\x12\"\n\x1astop_timeline_presentation\x18\x06 \x01(\x08\x12\x1f\n\x17\x63lear_next_presentation\x18\x07 \x01(\x08\"\xa1\x01\n\x1a\x41PI_v1_ClearGroupLayerType\x12\t\n\x05music\x10\x00\x12\x11\n\raudio_effects\x10\x01\x12\t\n\x05props\x10\x02\x12\x0c\n\x08messages\x10\x03\x12\x11\n\rannouncements\x10\x04\x12\x10\n\x0cpresentation\x10\x05\x12\x16\n\x12presentation_media\x10\x06\x12\x0f\n\x0bvideo_input\x10\x07\"\xa6\t\n\x0e\x41PI_v1_Message\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x0f\n\x07message\x18\x02 \x01(\t\x12;\n\x06tokens\x18\x03 \x03(\x0b\x32+.rv.data.API_v1_Message.API_v1_MessageToken\x12)\n\x05theme\x18\x04 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x1a\xf2\x07\n\x13\x41PI_v1_MessageToken\x12\x0c\n\x04name\x18\x01 \x01(\t\x12L\n\x04text\x18\x02 \x01(\x0b\x32<.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_TextTokenH\x00\x12N\n\x05timer\x18\x03 \x01(\x0b\x32=.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_TimerTokenH\x00\x12N\n\x05\x63lock\x18\x04 \x01(\x0b\x32=.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_ClockTokenH\x00\x1a \n\x10\x41PI_v1_TextToken\x12\x0c\n\x04text\x18\x01 \x01(\t\x1a\xea\x02\n\x11\x41PI_v1_TimerToken\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x16\n\x0e\x61llows_overrun\x18\x02 \x01(\x08\x12+\n\x06\x66ormat\x18\x06 \x01(\x0b\x32\x1b.rv.data.API_v1_TimerFormat\x12\x41\n\tcountdown\x18\x03 \x01(\x0b\x32,.rv.data.API_v1_Timer.API_v1_Timer_CountdownH\x00\x12P\n\x12\x63ount_down_to_time\x18\x04 \x01(\x0b\x32\x32.rv.data.API_v1_Timer.API_v1_Timer_CountdownToTimeH\x00\x12=\n\x07\x65lapsed\x18\x05 \x01(\x0b\x32*.rv.data.API_v1_Timer.API_v1_Timer_ElapsedH\x00\x42\x14\n\x12TimerConfiguration\x1a\xc2\x02\n\x11\x41PI_v1_ClockToken\x12\x63\n\x04\x64\x61te\x18\x01 \x01(\x0e\x32U.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat\x12\x63\n\x04time\x18\x02 \x01(\x0e\x32U.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat\x12\x13\n\x0bis_24_hours\x18\x03 \x01(\x08\"N\n\x17\x41PI_v1_ClockTokenFormat\x12\x08\n\x04none\x10\x00\x12\t\n\x05short\x10\x01\x12\n\n\x06medium\x10\x02\x12\x08\n\x04long\x10\x03\x12\x08\n\x04\x66ull\x10\x04\x42\x0b\n\tTokenType\"\xf9\x04\n\x0c\x41PI_v1_Timer\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x16\n\x0e\x61llows_overrun\x18\x02 \x01(\x08\x12\x41\n\tcountdown\x18\x03 \x01(\x0b\x32,.rv.data.API_v1_Timer.API_v1_Timer_CountdownH\x00\x12P\n\x12\x63ount_down_to_time\x18\x04 \x01(\x0b\x32\x32.rv.data.API_v1_Timer.API_v1_Timer_CountdownToTimeH\x00\x12=\n\x07\x65lapsed\x18\x05 \x01(\x0b\x32*.rv.data.API_v1_Timer.API_v1_Timer_ElapsedH\x00\x1a*\n\x16\x41PI_v1_Timer_Countdown\x12\x10\n\x08\x64uration\x18\x01 \x01(\x05\x1a\xbe\x01\n\x1c\x41PI_v1_Timer_CountdownToTime\x12\x13\n\x0btime_of_day\x18\x01 \x01(\x05\x12T\n\x06period\x18\x02 \x01(\x0e\x32\x44.rv.data.API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod\"3\n\x11\x41PI_v1_TimePeriod\x12\x06\n\x02\x61m\x10\x00\x12\x06\n\x02pm\x10\x01\x12\x0e\n\nis_24_hour\x10\x02\x1aR\n\x14\x41PI_v1_Timer_Elapsed\x12\x12\n\nstart_time\x18\x01 \x01(\x05\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x05\x12\x14\n\x0chas_end_time\x18\x03 \x01(\x08\x42\x14\n\x12TimerConfiguration\"\xa6\x03\n\x12\x41PI_v1_TimerFormat\x12G\n\x04hour\x18\x06 \x01(\x0e\x32\x39.rv.data.API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat\x12I\n\x06minute\x18\x07 \x01(\x0e\x32\x39.rv.data.API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat\x12I\n\x06second\x18\x08 \x01(\x0e\x32\x39.rv.data.API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat\x12N\n\x0bmillisecond\x18\t \x01(\x0e\x32\x39.rv.data.API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat\"a\n\x1d\x41PI_v1_TimerUnitDisplayFormat\x12\x08\n\x04none\x10\x00\x12\t\n\x05short\x10\x01\x12\x08\n\x04long\x10\x02\x12\x10\n\x0cremove_short\x10\x03\x12\x0f\n\x0bremove_long\x10\x04\"\xe1\x01\n\x11\x41PI_v1_TimerValue\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x0c\n\x04time\x18\x02 \x01(\t\x12;\n\x05state\x18\x03 \x01(\x0e\x32,.rv.data.API_v1_TimerValue.API_v1_TimerState\"Y\n\x11\x41PI_v1_TimerState\x12\x0b\n\x07stopped\x10\x00\x12\x0b\n\x07running\x10\x01\x12\x0c\n\x08\x63omplete\x10\x02\x12\x0f\n\x0boverrunning\x10\x03\x12\x0b\n\x07overran\x10\x04\"G\n\x0c\x41PI_v1_Color\x12\x0b\n\x03red\x18\x01 \x01(\x01\x12\r\n\x05green\x18\x02 \x01(\x01\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x01\x12\r\n\x05\x61lpha\x18\x04 \x01(\x01\"^\n\x0b\x41PI_v1_Look\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\'\n\x07screens\x18\x02 \x03(\x0b\x32\x16.rv.data.API_v1_Screen\"\x9e\x01\n\rAPI_v1_Screen\x12\x13\n\x0bvideo_input\x18\x01 \x01(\x08\x12\r\n\x05media\x18\x02 \x01(\x08\x12\r\n\x05slide\x18\x03 \x01(\x08\x12\x15\n\rannouncements\x18\x04 \x01(\x08\x12\r\n\x05props\x18\x05 \x01(\x08\x12\x10\n\x08messages\x18\x06 \x01(\x08\x12\x14\n\x0cpresentation\x18\x07 \x01(\t\x12\x0c\n\x04mask\x18\x08 \x01(\t\"\\\n\x0c\x41PI_v1_Macro\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12$\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x15.rv.data.API_v1_Color\".\n\x12\x41PI_v1_GroupMember\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\"\xcb\x04\n\x18\x41PI_v1_GroupMemberStatus\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12U\n\x08platform\x18\x04 \x01(\x0e\x32\x43.rv.data.API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform\x12\x12\n\nos_version\x18\x05 \x01(\t\x12\x18\n\x10host_description\x18\x06 \x01(\t\x12\x13\n\x0b\x61pi_version\x18\x07 \x01(\t\x12\x66\n\x11\x63onnection_status\x18\x08 \x01(\x0e\x32K.rv.data.API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus\"s\n!API_v1_GroupMemberStatus_Platform\x12\x14\n\x10PLATFORM_UNKNOWN\x10\x00\x12\x12\n\x0ePLATFORM_MACOS\x10\x01\x12\x12\n\x0ePLATFORM_WIN32\x10\x02\x12\x10\n\x0cPLATFORM_WEB\x10\x03\"\x8f\x01\n)API_v1_GroupMemberStatus_ConnectionStatus\x12\x1d\n\x19\x43ONNECTION_STATUS_UNKNOWN\x10\x00\x12\x1f\n\x1b\x43ONNECTION_STATUS_CONNECTED\x10\x01\x12\"\n\x1e\x43ONNECTION_STATUS_DISCONNECTED\x10\x02\"\xb4\x01\n\x16\x41PI_v1_GroupDefinition\x12%\n\ttimestamp\x18\x01 \x01(\x0b\x32\x12.rv.data.Timestamp\x12\x0e\n\x06secret\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12,\n\x07members\x18\x04 \x03(\x0b\x32\x1b.rv.data.API_v1_GroupMember\x12\'\n\x10group_identifier\x18\x05 \x01(\x0b\x32\r.rv.data.UUID\"\xb3\x01\n\x15\x41PI_v1_Error_Response\x12?\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x30.rv.data.API_v1_Error_Response.API_v1_Error_Type\"Y\n\x11\x41PI_v1_Error_Type\x12\r\n\tNOT_FOUND\x10\x00\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x10\n\x0cUNAUTHORIZED\x10\x03\"\x82\x02\n\x16\x41PI_v1_CaptureSettings\x12\x1d\n\x06source\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x33\n\raudio_routing\x18\x02 \x03(\x0b\x32\x1c.rv.data.API_v1_AudioRouting\x12+\n\x04\x64isk\x18\x03 \x01(\x0b\x32\x1b.rv.data.API_v1_DiskCaptureH\x00\x12+\n\x04rtmp\x18\x04 \x01(\x0b\x32\x1b.rv.data.API_v1_RTMPCaptureH\x00\x12+\n\x04resi\x18\x05 \x01(\x0b\x32\x1b.rv.data.API_v1_ResiCaptureH\x00\x42\r\n\x0b\x44\x65stination\",\n\x0b\x41PI_v1_Size\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\"\"\n\x13\x41PI_v1_AudioRouting\x12\x0b\n\x03map\x18\x01 \x03(\r\"x\n\x12\x41PI_v1_DiskCapture\x12\x15\n\rfile_location\x18\x01 \x01(\t\x12\r\n\x05\x63odec\x18\x02 \x01(\t\x12(\n\nresolution\x18\x03 \x01(\x0b\x32\x14.rv.data.API_v1_Size\x12\x12\n\nframe_rate\x18\x04 \x01(\x01\"n\n\x12\x41PI_v1_RTMPCapture\x12\x0e\n\x06server\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x10\n\x08\x65ncoding\x18\x03 \x01(\t\x12\x12\n\nsave_local\x18\x04 \x01(\x08\x12\x15\n\rfile_location\x18\x05 \x01(\t\"p\n\x12\x41PI_v1_ResiCapture\x12\x12\n\nevent_name\x18\x01 \x01(\t\x12\x19\n\x11\x65vent_description\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65stination_group\x18\x03 \x01(\t\x12\x10\n\x08\x65ncoding\x18\x04 \x01(\t\"\x86\x04\n\x13\x41PI_v1_Presentation\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x37\n\x06groups\x18\x02 \x03(\x0b\x32\'.rv.data.API_v1_Presentation.SlideGroup\x12\x14\n\x0chas_timeline\x18\x03 \x01(\x08\x12\x19\n\x11presentation_path\x18\x04 \x01(\t\x12=\n\x0b\x64\x65stination\x18\x05 \x01(\x0e\x32(.rv.data.API_v1_Presentation.Destination\x1a\xe9\x01\n\nSlideGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x15.rv.data.API_v1_Color\x12=\n\x06slides\x18\x03 \x03(\x0b\x32-.rv.data.API_v1_Presentation.SlideGroup.Slide\x1ah\n\x05Slide\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05notes\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\r\n\x05label\x18\x05 \x01(\t\x12\"\n\x04size\x18\x06 \x01(\x0b\x32\x14.rv.data.API_v1_Size\"2\n\x0b\x44\x65stination\x12\x10\n\x0cpresentation\x10\x00\x12\x11\n\rannouncements\x10\x01\"\xaf\x01\n\x15\x41PI_v1_StageLayoutMap\x12\x35\n\x07\x65ntries\x18\x01 \x03(\x0b\x32$.rv.data.API_v1_StageLayoutMap.Entry\x1a_\n\x05\x45ntry\x12*\n\x06screen\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12*\n\x06layout\x18\x02 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\"\x8e\x01\n\x11\x41PI_v1_ThemeGroup\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12*\n\x06groups\x18\x02 \x03(\x0b\x32\x1a.rv.data.API_v1_ThemeGroup\x12%\n\x06themes\x18\x03 \x03(\x0b\x32\x15.rv.data.API_v1_Theme\"b\n\x0c\x41PI_v1_Theme\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12*\n\x06slides\x18\x02 \x03(\x0b\x32\x1a.rv.data.API_v1_ThemeSlide\"\x8a\x01\n\x11\x41PI_v1_ThemeSlide\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\"\n\x04size\x18\x02 \x01(\x0b\x32\x14.rv.data.API_v1_Size\x12)\n\nbackground\x18\x03 \x01(\x0b\x32\x15.rv.data.API_v1_Color\"G\n\x1a\x41PI_v1_SlideDisplayDetails\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05notes\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\"\xd4\x01\n\x13\x41PI_v1_ScreenConfig\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\"\n\x04size\x18\x02 \x01(\x0b\x32\x14.rv.data.API_v1_Size\x12\x43\n\x0bscreen_type\x18\x03 \x01(\x0e\x32..rv.data.API_v1_ScreenConfig.API_v1_ScreenType\",\n\x11\x41PI_v1_ScreenType\x12\x0c\n\x08\x61udience\x10\x00\x12\t\n\x05stage\x10\x01\"L\n\x0f\x41PI_v1_PropData\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x11\n\tis_active\x18\x02 \x01(\x08\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1BasicTypes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_API_V1_IDENTIFIER']._serialized_start=106
  _globals['_API_V1_IDENTIFIER']._serialized_end=168
  _globals['_API_V1_SLIDEINDEX']._serialized_start=170
  _globals['_API_V1_SLIDEINDEX']._serialized_end=257
  _globals['_API_V1_PLAYLIST']._serialized_start=260
  _globals['_API_V1_PLAYLIST']._serialized_end=469
  _globals['_API_V1_PLAYLIST_API_V1_PLAYLISTTYPE']._serialized_start=423
  _globals['_API_V1_PLAYLIST_API_V1_PLAYLISTTYPE']._serialized_end=469
  _globals['_API_V1_PLAYLISTANDITEM']._serialized_start=471
  _globals['_API_V1_PLAYLISTANDITEM']._serialized_end=583
  _globals['_API_V1_MEDIAPLAYLISTITEM']._serialized_start=586
  _globals['_API_V1_MEDIAPLAYLISTITEM']._serialized_end=829
  _globals['_API_V1_MEDIAPLAYLISTITEM_API_V1_MEDIAPLAYLISTITEMTYPE']._serialized_start=766
  _globals['_API_V1_MEDIAPLAYLISTITEM_API_V1_MEDIAPLAYLISTITEMTYPE']._serialized_end=829
  _globals['_API_V1_PLAYLISTITEM']._serialized_start=832
  _globals['_API_V1_PLAYLISTITEM']._serialized_end=1200
  _globals['_API_V1_PLAYLISTITEM_API_V1_PLAYLISTITEMTYPE']._serialized_start=1091
  _globals['_API_V1_PLAYLISTITEM_API_V1_PLAYLISTITEMTYPE']._serialized_end=1200
  _globals['_API_V1_CLEARGROUP']._serialized_start=1203
  _globals['_API_V1_CLEARGROUP']._serialized_end=1654
  _globals['_API_V1_CLEARGROUP_API_V1_CLEARGROUPLAYERTYPE']._serialized_start=1493
  _globals['_API_V1_CLEARGROUP_API_V1_CLEARGROUPLAYERTYPE']._serialized_end=1654
  _globals['_API_V1_MESSAGE']._serialized_start=1657
  _globals['_API_V1_MESSAGE']._serialized_end=2847
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN']._serialized_start=1837
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN']._serialized_end=2847
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_TEXTTOKEN']._serialized_start=2112
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_TEXTTOKEN']._serialized_end=2144
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_TIMERTOKEN']._serialized_start=2147
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_TIMERTOKEN']._serialized_end=2509
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_CLOCKTOKEN']._serialized_start=2512
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_CLOCKTOKEN']._serialized_end=2834
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_CLOCKTOKEN_API_V1_CLOCKTOKENFORMAT']._serialized_start=2756
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_CLOCKTOKEN_API_V1_CLOCKTOKENFORMAT']._serialized_end=2834
  _globals['_API_V1_TIMER']._serialized_start=2850
  _globals['_API_V1_TIMER']._serialized_end=3483
  _globals['_API_V1_TIMER_API_V1_TIMER_COUNTDOWN']._serialized_start=3142
  _globals['_API_V1_TIMER_API_V1_TIMER_COUNTDOWN']._serialized_end=3184
  _globals['_API_V1_TIMER_API_V1_TIMER_COUNTDOWNTOTIME']._serialized_start=3187
  _globals['_API_V1_TIMER_API_V1_TIMER_COUNTDOWNTOTIME']._serialized_end=3377
  _globals['_API_V1_TIMER_API_V1_TIMER_COUNTDOWNTOTIME_API_V1_TIMEPERIOD']._serialized_start=3326
  _globals['_API_V1_TIMER_API_V1_TIMER_COUNTDOWNTOTIME_API_V1_TIMEPERIOD']._serialized_end=3377
  _globals['_API_V1_TIMER_API_V1_TIMER_ELAPSED']._serialized_start=3379
  _globals['_API_V1_TIMER_API_V1_TIMER_ELAPSED']._serialized_end=3461
  _globals['_API_V1_TIMERFORMAT']._serialized_start=3486
  _globals['_API_V1_TIMERFORMAT']._serialized_end=3908
  _globals['_API_V1_TIMERFORMAT_API_V1_TIMERUNITDISPLAYFORMAT']._serialized_start=3811
  _globals['_API_V1_TIMERFORMAT_API_V1_TIMERUNITDISPLAYFORMAT']._serialized_end=3908
  _globals['_API_V1_TIMERVALUE']._serialized_start=3911
  _globals['_API_V1_TIMERVALUE']._serialized_end=4136
  _globals['_API_V1_TIMERVALUE_API_V1_TIMERSTATE']._serialized_start=4047
  _globals['_API_V1_TIMERVALUE_API_V1_TIMERSTATE']._serialized_end=4136
  _globals['_API_V1_COLOR']._serialized_start=4138
  _globals['_API_V1_COLOR']._serialized_end=4209
  _globals['_API_V1_LOOK']._serialized_start=4211
  _globals['_API_V1_LOOK']._serialized_end=4305
  _globals['_API_V1_SCREEN']._serialized_start=4308
  _globals['_API_V1_SCREEN']._serialized_end=4466
  _globals['_API_V1_MACRO']._serialized_start=4468
  _globals['_API_V1_MACRO']._serialized_end=4560
  _globals['_API_V1_GROUPMEMBER']._serialized_start=4562
  _globals['_API_V1_GROUPMEMBER']._serialized_end=4608
  _globals['_API_V1_GROUPMEMBERSTATUS']._serialized_start=4611
  _globals['_API_V1_GROUPMEMBERSTATUS']._serialized_end=5198
  _globals['_API_V1_GROUPMEMBERSTATUS_API_V1_GROUPMEMBERSTATUS_PLATFORM']._serialized_start=4937
  _globals['_API_V1_GROUPMEMBERSTATUS_API_V1_GROUPMEMBERSTATUS_PLATFORM']._serialized_end=5052
  _globals['_API_V1_GROUPMEMBERSTATUS_API_V1_GROUPMEMBERSTATUS_CONNECTIONSTATUS']._serialized_start=5055
  _globals['_API_V1_GROUPMEMBERSTATUS_API_V1_GROUPMEMBERSTATUS_CONNECTIONSTATUS']._serialized_end=5198
  _globals['_API_V1_GROUPDEFINITION']._serialized_start=5201
  _globals['_API_V1_GROUPDEFINITION']._serialized_end=5381
  _globals['_API_V1_ERROR_RESPONSE']._serialized_start=5384
  _globals['_API_V1_ERROR_RESPONSE']._serialized_end=5563
  _globals['_API_V1_ERROR_RESPONSE_API_V1_ERROR_TYPE']._serialized_start=5474
  _globals['_API_V1_ERROR_RESPONSE_API_V1_ERROR_TYPE']._serialized_end=5563
  _globals['_API_V1_CAPTURESETTINGS']._serialized_start=5566
  _globals['_API_V1_CAPTURESETTINGS']._serialized_end=5824
  _globals['_API_V1_SIZE']._serialized_start=5826
  _globals['_API_V1_SIZE']._serialized_end=5870
  _globals['_API_V1_AUDIOROUTING']._serialized_start=5872
  _globals['_API_V1_AUDIOROUTING']._serialized_end=5906
  _globals['_API_V1_DISKCAPTURE']._serialized_start=5908
  _globals['_API_V1_DISKCAPTURE']._serialized_end=6028
  _globals['_API_V1_RTMPCAPTURE']._serialized_start=6030
  _globals['_API_V1_RTMPCAPTURE']._serialized_end=6140
  _globals['_API_V1_RESICAPTURE']._serialized_start=6142
  _globals['_API_V1_RESICAPTURE']._serialized_end=6254
  _globals['_API_V1_PRESENTATION']._serialized_start=6257
  _globals['_API_V1_PRESENTATION']._serialized_end=6775
  _globals['_API_V1_PRESENTATION_SLIDEGROUP']._serialized_start=6490
  _globals['_API_V1_PRESENTATION_SLIDEGROUP']._serialized_end=6723
  _globals['_API_V1_PRESENTATION_SLIDEGROUP_SLIDE']._serialized_start=6619
  _globals['_API_V1_PRESENTATION_SLIDEGROUP_SLIDE']._serialized_end=6723
  _globals['_API_V1_PRESENTATION_DESTINATION']._serialized_start=6725
  _globals['_API_V1_PRESENTATION_DESTINATION']._serialized_end=6775
  _globals['_API_V1_STAGELAYOUTMAP']._serialized_start=6778
  _globals['_API_V1_STAGELAYOUTMAP']._serialized_end=6953
  _globals['_API_V1_STAGELAYOUTMAP_ENTRY']._serialized_start=6858
  _globals['_API_V1_STAGELAYOUTMAP_ENTRY']._serialized_end=6953
  _globals['_API_V1_THEMEGROUP']._serialized_start=6956
  _globals['_API_V1_THEMEGROUP']._serialized_end=7098
  _globals['_API_V1_THEME']._serialized_start=7100
  _globals['_API_V1_THEME']._serialized_end=7198
  _globals['_API_V1_THEMESLIDE']._serialized_start=7201
  _globals['_API_V1_THEMESLIDE']._serialized_end=7339
  _globals['_API_V1_SLIDEDISPLAYDETAILS']._serialized_start=7341
  _globals['_API_V1_SLIDEDISPLAYDETAILS']._serialized_end=7412
  _globals['_API_V1_SCREENCONFIG']._serialized_start=7415
  _globals['_API_V1_SCREENCONFIG']._serialized_end=7627
  _globals['_API_V1_SCREENCONFIG_API_V1_SCREENTYPE']._serialized_start=7583
  _globals['_API_V1_SCREENCONFIG_API_V1_SCREENTYPE']._serialized_end=7627
  _globals['_API_V1_PROPDATA']._serialized_start=7629
  _globals['_API_V1_PROPDATA']._serialized_end=7705
# @@protoc_insertion_point(module_scope)
