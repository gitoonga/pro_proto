# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proApi.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2
import messages_pb2 as messages__pb2
import timers_pb2 as timers__pb2
import rvtimestamp_pb2 as rvtimestamp__pb2
import proApiV1_pb2 as proApiV1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cproApi.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\x1a\x0emessages.proto\x1a\x0ctimers.proto\x1a\x11rvtimestamp.proto\x1a\x0eproApiV1.proto\"\xa9\x01\n\x08ProApiIn\x12\x30\n\nhandler_in\x18\x01 \x01(\x0b\x32\x1a.rv.data.ProLink.HandlerInH\x00\x12*\n\x0bnetwork_api\x18\x02 \x01(\x0b\x32\x13.rv.data.NetworkAPIH\x00\x12\x30\n\x0enetwork_api_v1\x18\x03 \x01(\x0b\x32\x16.rv.data.NetworkAPI_v1H\x00\x42\r\n\x0bMessageType\"\xe4\x01\n\tProApiOut\x12\x32\n\x0bhandler_out\x18\x01 \x01(\x0b\x32\x1b.rv.data.ProLink.HandlerOutH\x00\x12\x36\n\rclient_action\x18\x02 \x01(\x0b\x32\x1d.rv.data.ProLink.ClientActionH\x00\x12*\n\x0bnetwork_api\x18\x03 \x01(\x0b\x32\x13.rv.data.NetworkAPIH\x00\x12\x30\n\x0enetwork_api_v1\x18\x04 \x01(\x0b\x32\x16.rv.data.NetworkAPI_v1H\x00\x42\r\n\x0bMessageType\"\xcd\x02\n\x1aProApiNetworkConfiguration\x12\x16\n\x0e\x65nable_network\x18\x01 \x01(\x08\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x14\n\x0cnetwork_name\x18\x03 \x01(\t\x12\x15\n\rremote_enable\x18\x04 \x01(\x08\x12\x1d\n\x15remote_control_enable\x18\x05 \x01(\x08\x12\x1f\n\x17remote_control_password\x18\x06 \x01(\t\x12\x1d\n\x15remote_observe_enable\x18\x07 \x01(\x08\x12\x1f\n\x17remote_observe_password\x18\x08 \x01(\t\x12\x14\n\x0cstage_enable\x18\t \x01(\x08\x12\x16\n\x0estage_password\x18\n \x01(\t\x12\x13\n\x0blink_enable\x18\x0b \x01(\x08\x12\x19\n\x11web_resource_root\x18\x0c \x01(\t\"\xc8.\n\x07ProLink\x1a\xdd\x01\n\x0fGroupDefinition\x12%\n\ttimestamp\x18\x01 \x01(\x0b\x32\x12.rv.data.Timestamp\x12\x0e\n\x06secret\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x38\n\x07members\x18\x04 \x03(\x0b\x32\'.rv.data.ProLink.GroupDefinition.Member\x12\'\n\x10group_identifier\x18\x05 \x01(\x0b\x32\r.rv.data.UUID\x1a\"\n\x06Member\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x1a\x8c\x02\n\nZeroConfig\x1a\x8a\x01\n\x12NetworkEnvironment\x12:\n\x10\x61vailable_groups\x18\x01 \x03(\x0b\x32 .rv.data.ProLink.GroupDefinition\x12\x38\n\x11\x61vailable_devices\x18\x02 \x03(\x0b\x32\x1d.rv.data.ProLink.MemberStatus\x1aq\n\x0fMulticastPacket\x12/\n\x05group\x18\x01 \x01(\x0b\x32 .rv.data.ProLink.GroupDefinition\x12-\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32\x1d.rv.data.ProLink.MemberStatus\x1a\xe3\x06\n\x0cTowerMessage\x1a\x14\n\x12TowerStatusRequest\x1at\n\x13TowerStatusResponse\x12\x13\n\x0bmember_name\x18\x02 \x01(\t\x12<\n\x10group_definition\x18\x01 \x01(\x0b\x32 .rv.data.ProLink.GroupDefinitionH\x00\x42\n\n\x08Response\x1a\xa3\x01\n\x15TowerAddMemberRequest\x12<\n\x10group_definition\x18\x01 \x01(\x0b\x32 .rv.data.ProLink.GroupDefinitionH\x00\x12\x41\n\x0ejoining_member\x18\x02 \x01(\x0b\x32\'.rv.data.ProLink.GroupDefinition.MemberH\x00\x42\t\n\x07Request\x1a\\\n\x18TowerRemoveMemberRequest\x12@\n\x0fremoving_member\x18\x01 \x01(\x0b\x32\'.rv.data.ProLink.GroupDefinition.Member\x1a\xd3\x02\n\x16TowerAddMemberResponse\x12<\n\x10group_definition\x18\x01 \x01(\x0b\x32 .rv.data.ProLink.GroupDefinitionH\x00\x12M\n\x06\x61\x63\x63\x65pt\x18\x02 \x01(\x0b\x32;.rv.data.ProLink.TowerMessage.TowerAddMemberResponse.AcceptH\x00\x12\\\n\x0e\x64\x65\x63line_reason\x18\x03 \x01(\x0e\x32\x42.rv.data.ProLink.TowerMessage.TowerAddMemberResponse.DeclineReasonH\x00\x1a\x08\n\x06\x41\x63\x63\x65pt\"8\n\rDeclineReason\x12\x14\n\x10\x41LREADY_IN_GROUP\x10\x00\x12\x11\n\rUSER_DECLINED\x10\x01\x42\n\n\x08Response\x1a\x17\n\x15TowerHeartbeatRequest\x1aT\n\x16TowerHeartbeatResponse\x12:\n\x10group_definition\x18\x01 \x01(\x0b\x32 .rv.data.ProLink.GroupDefinition\x1a\xc4\x03\n\x0cMemberStatus\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x38\n\x08platform\x18\x04 \x01(\x0e\x32&.rv.data.ProLink.MemberStatus.Platform\x12\x12\n\nos_version\x18\x05 \x01(\t\x12\x18\n\x10host_description\x18\x06 \x01(\t\x12\x13\n\x0b\x61pi_version\x18\x07 \x01(\t\x12I\n\x11\x63onnection_status\x18\x08 \x01(\x0e\x32..rv.data.ProLink.MemberStatus.ConnectionStatus\"L\n\x08Platform\x12\x16\n\x12PLATFORM_UNDEFINED\x10\x00\x12\x12\n\x0ePLATFORM_MACOS\x10\x01\x12\x14\n\x10PLATFORM_WINDOWS\x10\x02\"v\n\x10\x43onnectionStatus\x12\x1d\n\x19\x43ONNECTION_STATUS_UNKNOWN\x10\x00\x12\x1f\n\x1b\x43ONNECTION_STATUS_CONNECTED\x10\x01\x12\"\n\x1e\x43ONNECTION_STATUS_DISCONNECTED\x10\x02\x1a\xe7\x03\n\x0c\x43lientAction\x12\x45\n\x0e\x61\x64\x64_connection\x18\x01 \x01(\x0b\x32+.rv.data.ProLink.ClientAction.AddConnectionH\x00\x12K\n\x11remove_connection\x18\x02 \x01(\x0b\x32..rv.data.ProLink.ClientAction.RemoveConnectionH\x00\x12\x43\n\rcancel_action\x18\x03 \x01(\x0b\x32*.rv.data.ProLink.ClientAction.CancelActionH\x00\x12?\n\x0brender_time\x18\x04 \x01(\x0b\x32(.rv.data.ProLink.ClientAction.RenderTimeH\x00\x1a=\n\rAddConnection\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x12\n\ngroup_name\x18\x03 \x01(\t\x1a,\n\x10RemoveConnection\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x1a\x0e\n\x0c\x43\x61ncelAction\x1a\x32\n\nRenderTime\x12\x0f\n\x07latency\x18\x01 \x01(\x04\x12\x13\n\x0brender_time\x18\x02 \x01(\x04\x42\x0c\n\nActionType\x1a\xae\x16\n\tHandlerIn\x12:\n\ngroup_name\x18\x01 \x01(\x0b\x32$.rv.data.ProLink.HandlerIn.GroupNameH\x00\x12U\n\x18group_definition_request\x18\x02 \x01(\x0b\x32\x31.rv.data.ProLink.HandlerIn.GroupDefinitionRequestH\x00\x12S\n\x17group_join_confirmation\x18\x03 \x01(\x0b\x32\x30.rv.data.ProLink.HandlerIn.GroupJoinConfirmationH\x00\x12K\n\x13group_join_password\x18\x04 \x01(\x0b\x32,.rv.data.ProLink.HandlerIn.GroupJoinPasswordH\x00\x12O\n\x15\x61\x64\x64_connection_result\x18\x05 \x01(\x0b\x32..rv.data.ProLink.HandlerIn.AddConnectionResultH\x00\x12\x38\n\x0cgroup_update\x18\x06 \x01(\x0b\x32 .rv.data.ProLink.GroupDefinitionH\x00\x12M\n\x14member_status_change\x18\x07 \x01(\x0b\x32-.rv.data.ProLink.HandlerIn.MemberStatusChangeH\x00\x12H\n\x11propresenter_info\x18\x08 \x01(\x0b\x32+.rv.data.ProLink.HandlerIn.ProPresenterInfoH\x00\x12>\n\x0cserver_state\x18\t \x01(\x0b\x32&.rv.data.ProLink.HandlerIn.ServerStateH\x00\x12P\n\x15\x63onfiguration_request\x18\n \x01(\x0b\x32/.rv.data.ProLink.HandlerIn.ConfigurationRequestH\x00\x12_\n%zeroconfig_network_environment_change\x18\x0b \x01(\x0b\x32..rv.data.ProLink.ZeroConfig.NetworkEnvironmentH\x00\x12<\n\x0blog_request\x18\x0c \x01(\x0b\x32%.rv.data.ProLink.HandlerIn.LogRequestH\x00\x1a\x0b\n\tGroupName\x1a\x18\n\x16GroupDefinitionRequest\x1a%\n\x15GroupJoinConfirmation\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a!\n\x11GroupJoinPassword\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\xdf\n\n\x13\x41\x64\x64\x43onnectionResult\x12I\n\x07success\x18\x01 \x01(\x0b\x32\x36.rv.data.ProLink.HandlerIn.AddConnectionResult.SuccessH\x00\x12I\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x36.rv.data.ProLink.HandlerIn.AddConnectionResult.FailureH\x00\x1aI\n\x07Success\x12>\n\x14new_group_definition\x18\x01 \x01(\x0b\x32 .rv.data.ProLink.GroupDefinition\x1a\xdc\x08\n\x07\x46\x61ilure\x12W\n\nunexpected\x18\x01 \x01(\x0b\x32\x41.rv.data.ProLink.HandlerIn.AddConnectionResult.Failure.UnexpectedH\x00\x12S\n\x08\x64\x65\x63lined\x18\x02 \x01(\x0b\x32?.rv.data.ProLink.HandlerIn.AddConnectionResult.Failure.DeclinedH\x00\x12Q\n\x07timeout\x18\x03 \x01(\x0b\x32>.rv.data.ProLink.HandlerIn.AddConnectionResult.Failure.TimeoutH\x00\x12\\\n\rlink_disabled\x18\x04 \x01(\x0b\x32\x43.rv.data.ProLink.HandlerIn.AddConnectionResult.Failure.LinkDisabledH\x00\x12]\n\x0ein_other_group\x18\x05 \x01(\x0b\x32\x43.rv.data.ProLink.HandlerIn.AddConnectionResult.Failure.InOtherGroupH\x00\x12\x65\n\x12invalid_ip_address\x18\x06 \x01(\x0b\x32G.rv.data.ProLink.HandlerIn.AddConnectionResult.Failure.InvalidIpAddressH\x00\x12\x61\n\x10\x61lready_in_group\x18\x07 \x01(\x0b\x32\x45.rv.data.ProLink.HandlerIn.AddConnectionResult.Failure.AlreadyInGroupH\x00\x12[\n\rcould_not_add\x18\x08 \x01(\x0b\x32\x42.rv.data.ProLink.HandlerIn.AddConnectionResult.Failure.CouldNotAddH\x00\x12]\n\x0e\x63ould_not_join\x18\t \x01(\x0b\x32\x43.rv.data.ProLink.HandlerIn.AddConnectionResult.Failure.CouldNotJoinH\x00\x1a\x0c\n\nUnexpected\x1a\n\n\x08\x44\x65\x63lined\x1a\t\n\x07Timeout\x1a\x0e\n\x0cLinkDisabled\x1a\x37\n\x0cInOtherGroup\x12\x13\n\x0bmember_name\x18\x01 \x01(\t\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x1a\x12\n\x10InvalidIpAddress\x1a\x39\n\x0e\x41lreadyInGroup\x12\x13\n\x0bmember_name\x18\x01 \x01(\t\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x1a\"\n\x0b\x43ouldNotAdd\x12\x13\n\x0bmember_name\x18\x01 \x01(\t\x1a\"\n\x0c\x43ouldNotJoin\x12\x12\n\ngroup_name\x18\x01 \x01(\tB\x08\n\x06ReasonB\x08\n\x06Result\x1a\x44\n\x12MemberStatusChange\x12.\n\x07members\x18\x01 \x03(\x0b\x32\x1d.rv.data.ProLink.MemberStatus\x1a\x12\n\x10ProPresenterInfo\x1aQ\n\x0bServerState\x12\x10\n\x08local_ip\x18\x01 \x01(\t\x12\x11\n\tpublic_ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x0f\n\x07success\x18\x04 \x01(\x08\x1a\x16\n\x14\x43onfigurationRequest\x1a\xf3\x01\n\nLogRequest\x12@\n\x08severity\x18\x01 \x01(\x0e\x32..rv.data.ProLink.HandlerIn.LogRequest.Severity\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x91\x01\n\x08Severity\x12\x12\n\x0eSEVERITY_DEBUG\x10\x00\x12\x1a\n\x16SEVERITY_DEBUG_WARNING\x10\x01\x12\x11\n\rSEVERITY_INFO\x10\x02\x12\x14\n\x10SEVERITY_WARNING\x10\x03\x12\x12\n\x0eSEVERITY_ERROR\x10\x04\x12\x18\n\x14SEVERITY_FATAL_ERROR\x10\x05\x42\t\n\x07Request\x1a\x85\x06\n\nHandlerOut\x12;\n\ngroup_name\x18\x01 \x01(\x0b\x32%.rv.data.ProLink.HandlerOut.GroupNameH\x00\x12<\n\x10group_definition\x18\x02 \x01(\x0b\x32 .rv.data.ProLink.GroupDefinitionH\x00\x12T\n\x17group_join_confirmation\x18\x03 \x01(\x0b\x32\x31.rv.data.ProLink.HandlerOut.GroupJoinConfirmationH\x00\x12L\n\x13group_join_password\x18\x04 \x01(\x0b\x32-.rv.data.ProLink.HandlerOut.GroupJoinPasswordH\x00\x12I\n\x11propresenter_info\x18\x05 \x01(\x0b\x32,.rv.data.ProLink.HandlerOut.ProPresenterInfoH\x00\x12<\n\rconfiguration\x18\x06 \x01(\x0b\x32#.rv.data.ProApiNetworkConfigurationH\x00\x1a\x19\n\tGroupName\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\'\n\x15GroupJoinConfirmation\x12\x0e\n\x06\x61\x63\x63\x65pt\x18\x01 \x01(\x08\x1a%\n\x11GroupJoinPassword\x12\x10\n\x08password\x18\x01 \x01(\t\x1a\xd7\x01\n\x10ProPresenterInfo\x12G\n\x08platform\x18\x01 \x01(\x0e\x32\x35.rv.data.ProLink.HandlerOut.ProPresenterInfo.Platform\x12\x12\n\nos_version\x18\x02 \x01(\t\x12\x18\n\x10host_description\x18\x03 \x01(\t\"L\n\x08Platform\x12\x16\n\x12PLATFORM_UNDEFINED\x10\x00\x12\x12\n\x0ePLATFORM_MACOS\x10\x01\x12\x14\n\x10PLATFORM_WINDOWS\x10\x02\x42\n\n\x08Response\"\x86<\n\nNetworkAPI\x12,\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32\x1a.rv.data.NetworkAPI.ActionH\x00\x12\x37\n\x0cserver_state\x18\x02 \x01(\x0b\x32\x1f.rv.data.NetworkAPI.ServerStateH\x00\x12\x37\n\x0cgroup_change\x18\x05 \x01(\x0b\x32\x1f.rv.data.NetworkAPI.GroupChangeH\x00\x12;\n\x0egroup_response\x18\x06 \x01(\x0b\x32!.rv.data.NetworkAPI.GroupResponseH\x00\x1a\xfe\x01\n\nLinkStatus\x12\x39\n\x08platform\x18\x01 \x01(\x0e\x32\'.rv.data.NetworkAPI.LinkStatus.Platform\x12\x12\n\nos_version\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12-\n\ngroup_info\x18\x05 \x01(\x0b\x32\x19.rv.data.NetworkAPI.Group\"L\n\x08Platform\x12\x16\n\x12PLATFORM_UNDEFINED\x10\x00\x12\x12\n\x0ePLATFORM_MACOS\x10\x01\x12\x14\n\x10PLATFORM_WINDOWS\x10\x02\x1at\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x07members\x18\x02 \x03(\x0b\x32 .rv.data.NetworkAPI.Group.Member\x1a*\n\x06Member\x12\x12\n\nip_address\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x1a\xdb\x01\n\x0bGroupChange\x12\x31\n\x06invite\x18\x01 \x01(\x0b\x32\x1f.rv.data.NetworkAPI.GroupInviteH\x00\x12-\n\x04join\x18\x02 \x01(\x0b\x32\x1d.rv.data.NetworkAPI.GroupJoinH\x00\x12-\n\x04kick\x18\x03 \x01(\x0b\x32\x1d.rv.data.NetworkAPI.GroupKickH\x00\x12\x31\n\x06status\x18\x04 \x01(\x0b\x32\x1f.rv.data.NetworkAPI.GroupStatusH\x00\x42\x08\n\x06\x43hange\x1a\xd3\x01\n\rGroupResponse\x12<\n\x07success\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.GroupResponse.SuccessH\x00\x12:\n\x06status\x18\x02 \x01(\x0b\x32(.rv.data.NetworkAPI.GroupResponse.StatusH\x00\x1a\t\n\x07Success\x1a\x31\n\x06Status\x12\x13\n\x0bmember_name\x18\x01 \x01(\t\x12\x12\n\ngroup_name\x18\x02 \x01(\tB\n\n\x08Response\x1a?\n\x0bGroupStatus\x12\x30\n\x06member\x18\x01 \x01(\x0b\x32 .rv.data.NetworkAPI.Group.Member\x1a\x80\x01\n\x0bGroupInvite\x12-\n\ngroup_info\x18\x01 \x01(\x0b\x32\x19.rv.data.NetworkAPI.Group\x12\x0e\n\x06secret\x18\x02 \x01(\t\x12\x32\n\x08prospect\x18\x03 \x01(\x0b\x32 .rv.data.NetworkAPI.Group.Member\x1ar\n\tGroupJoin\x12\x31\n\x07sponsor\x18\x01 \x01(\x0b\x32 .rv.data.NetworkAPI.Group.Member\x12\x32\n\x08prospect\x18\x02 \x01(\x0b\x32 .rv.data.NetworkAPI.Group.Member\x1a=\n\tGroupKick\x12\x30\n\x06member\x18\x01 \x01(\x0b\x32 .rv.data.NetworkAPI.Group.Member\x1a@\n\x0bServerState\x12\x10\n\x08local_ip\x18\x01 \x01(\t\x12\x11\n\tpublic_ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x1a\xd4.\n\x06\x41\x63tion\x12\x35\n\x05\x63lear\x18\x01 \x01(\x0b\x32$.rv.data.NetworkAPI.Action.API_ClearH\x00\x12\x39\n\x07trigger\x18\x02 \x01(\x0b\x32&.rv.data.NetworkAPI.Action.API_TriggerH\x00\x12=\n\ttransport\x18\x03 \x01(\x0b\x32(.rv.data.NetworkAPI.Action.API_TransportH\x00\x12\x33\n\x04prop\x18\x04 \x01(\x0b\x32#.rv.data.NetworkAPI.Action.API_PropH\x00\x12\x35\n\x05timer\x18\x05 \x01(\x0b\x32$.rv.data.NetworkAPI.Action.API_TimerH\x00\x12:\n\x08message_\x18\x06 \x01(\x0b\x32&.rv.data.NetworkAPI.Action.API_MessageH\x00\x12\x35\n\x05macro\x18\x07 \x01(\x0b\x32$.rv.data.NetworkAPI.Action.API_MacroH\x00\x12\x33\n\x04look\x18\x08 \x01(\x0b\x32#.rv.data.NetworkAPI.Action.API_LookH\x00\x12\x35\n\x05stage\x18\t \x01(\x0b\x32$.rv.data.NetworkAPI.Action.API_StageH\x00\x12\x37\n\x06status\x18\n \x01(\x0b\x32%.rv.data.NetworkAPI.Action.API_StatusH\x00\x12H\n\x0fstatus_response\x18\x0b \x01(\x0b\x32-.rv.data.NetworkAPI.Action.API_StatusResponseH\x00\x12I\n\x10two_step_trigger\x18\x0c \x01(\x0b\x32-.rv.data.NetworkAPI.Action.API_TwoStepTriggerH\x00\x12J\n\x10preroll_complete\x18\r \x01(\x0b\x32..rv.data.NetworkAPI.Action.API_PrerollCompleteH\x00\x1a\xc5\x02\n\tAPI_Clear\x12;\n\x05layer\x18\x01 \x01(\x0e\x32*.rv.data.NetworkAPI.Action.API_Clear.LayerH\x00\x12\x45\n\x10group_identifier\x18\x02 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifierH\x00\"\xa6\x01\n\x05Layer\x12\x11\n\rLAYER_UNKNOWN\x10\x00\x12\x15\n\x11LAYER_VIDEO_INPUT\x10\x01\x12\x0f\n\x0bLAYER_MEDIA\x10\x02\x12\x16\n\x12LAYER_PRESENTATION\x10\x03\x12\x16\n\x12LAYER_ANNOUNCEMENT\x10\x04\x12\x0e\n\nLAYER_PROP\x10\x05\x12\x11\n\rLAYER_MESSAGE\x10\x06\x12\x0f\n\x0bLAYER_AUDIO\x10\x07\x42\x0b\n\tClearInfo\x1a\xec\x04\n\x12\x41PI_TwoStepTrigger\x12\n\n\x02id\x18\x01 \x01(\x04\x12J\n\toperation\x18\x02 \x01(\x0e\x32\x37.rv.data.NetworkAPI.Action.API_TwoStepTrigger.Operation\x12\x13\n\x0brender_time\x18\x03 \x01(\x04\x12K\n\x0cpresentation\x18\x04 \x01(\x0b\x32\x33.rv.data.NetworkAPI.Action.API_Trigger.PresentationH\x00\x12=\n\x05media\x18\x05 \x01(\x0b\x32,.rv.data.NetworkAPI.Action.API_Trigger.MediaH\x00\x12H\n\x0bvideo_input\x18\x06 \x01(\x0b\x32\x31.rv.data.NetworkAPI.Action.API_Trigger.VideoInputH\x00\x12=\n\x05\x61udio\x18\x07 \x01(\x0b\x32,.rv.data.NetworkAPI.Action.API_Trigger.AudioH\x00\x12?\n\x04prop\x18\x08 \x01(\x0b\x32/.rv.data.NetworkAPI.Action.API_Prop.TriggerPropH\x00\x12H\n\x07message\x18\t \x01(\x0b\x32\x35.rv.data.NetworkAPI.Action.API_Message.TriggerMessageH\x00\":\n\tOperation\x12\x15\n\x11OPERATION_PREROLL\x10\x00\x12\x16\n\x12OPERATION_ACTIVATE\x10\x01\x42\r\n\x0bTriggerData\x1a\x31\n\x13\x41PI_PrerollComplete\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06\x66\x61iled\x18\x02 \x01(\x08\x1a\x81\t\n\x0b\x41PI_Trigger\x12K\n\x0cpresentation\x18\x01 \x01(\x0b\x32\x33.rv.data.NetworkAPI.Action.API_Trigger.PresentationH\x00\x12=\n\x05media\x18\x02 \x01(\x0b\x32,.rv.data.NetworkAPI.Action.API_Trigger.MediaH\x00\x12H\n\x0bvideo_input\x18\x03 \x01(\x0b\x32\x31.rv.data.NetworkAPI.Action.API_Trigger.VideoInputH\x00\x12=\n\x05\x61udio\x18\x04 \x01(\x0b\x32,.rv.data.NetworkAPI.Action.API_Trigger.AudioH\x00\x1a\xd6\x04\n\x0cPresentation\x12\x13\n\tcue_index\x18\x01 \x01(\x05H\x00\x12g\n\x13playlist_index_path\x18\x02 \x01(\x0b\x32H.rv.data.NetworkAPI.Action.API_Trigger.Presentation.PlaylistPresentationH\x00\x12\x65\n\x12library_index_path\x18\x03 \x01(\x0b\x32G.rv.data.NetworkAPI.Action.API_Trigger.Presentation.LibraryPresentationH\x00\x1a`\n\x14PlaylistPresentation\x12H\n\x15index_path_components\x18\x01 \x03(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x1a\xe8\x01\n\x13LibraryPresentation\x12\x44\n\x11library_component\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x12I\n\x16presentation_component\x18\x02 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x12@\n\rcue_component\x18\x03 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifierB\x14\n\x12PresentationSource\x1aQ\n\x05Media\x12H\n\x15index_path_components\x18\x01 \x03(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x1aO\n\nVideoInput\x12\x41\n\x0evideo_input_id\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x1aQ\n\x05\x41udio\x12H\n\x15index_path_components\x18\x01 \x03(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifierB\r\n\x0bTriggerData\x1a\xd3\x05\n\rAPI_Transport\x12\x46\n\x05layer\x18\x01 \x01(\x0e\x32\x37.rv.data.NetworkAPI.Action.API_Transport.TransportLayer\x12=\n\x04play\x18\x02 \x01(\x0b\x32-.rv.data.NetworkAPI.Action.API_Transport.PlayH\x00\x12?\n\x05pause\x18\x03 \x01(\x0b\x32..rv.data.NetworkAPI.Action.API_Transport.PauseH\x00\x12N\n\rskip_backward\x18\x04 \x01(\x0b\x32\x35.rv.data.NetworkAPI.Action.API_Transport.SkipBackwardH\x00\x12L\n\x0cskip_forward\x18\x05 \x01(\x0b\x32\x34.rv.data.NetworkAPI.Action.API_Transport.SkipForwardH\x00\x12\x45\n\tgo_to_end\x18\x06 \x01(\x0b\x32\x30.rv.data.NetworkAPI.Action.API_Transport.GoToEndH\x00\x1a\x06\n\x04Play\x1a\x07\n\x05Pause\x1a\x1f\n\x0cSkipBackward\x12\x0f\n\x07seconds\x18\x01 \x01(\x05\x1a\x1e\n\x0bSkipForward\x12\x0f\n\x07seconds\x18\x01 \x01(\x05\x1a!\n\x07GoToEnd\x12\x16\n\x0eseconds_to_end\x18\x01 \x01(\x05\"\x8c\x01\n\x0eTransportLayer\x12\x1b\n\x17TRANSPORT_LAYER_UNKNOWN\x10\x00\x12 \n\x1cTRANSPORT_LAYER_PRESENTATION\x10\x01\x12 \n\x1cTRANSPORT_LAYER_ANNOUNCEMENT\x10\x02\x12\x19\n\x15TRANSPORT_LAYER_AUDIO\x10\x03\x42\x11\n\x0fTransportAction\x1a\xb6\x02\n\x08\x41PI_Prop\x12\x42\n\x07trigger\x18\x01 \x01(\x0b\x32/.rv.data.NetworkAPI.Action.API_Prop.TriggerPropH\x00\x12>\n\x05\x63lear\x18\x02 \x01(\x0b\x32-.rv.data.NetworkAPI.Action.API_Prop.ClearPropH\x00\x1aL\n\x0bTriggerProp\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x1aJ\n\tClearProp\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifierB\x0c\n\nPropAction\x1a\x95\x05\n\tAPI_Timer\x12@\n\x05start\x18\x01 \x01(\x0b\x32/.rv.data.NetworkAPI.Action.API_Timer.StartTimerH\x00\x12>\n\x04stop\x18\x02 \x01(\x0b\x32..rv.data.NetworkAPI.Action.API_Timer.StopTimerH\x00\x12@\n\x05reset\x18\x03 \x01(\x0b\x32/.rv.data.NetworkAPI.Action.API_Timer.ResetTimerH\x00\x12H\n\tconfigure\x18\x04 \x01(\x0b\x32\x33.rv.data.NetworkAPI.Action.API_Timer.ConfigureTimerH\x00\x1aK\n\nStartTimer\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x1aJ\n\tStopTimer\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x1aK\n\nResetTimer\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x1a\x84\x01\n\x0e\x43onfigureTimer\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x12\x33\n\rconfiguration\x18\x02 \x01(\x0b\x32\x1c.rv.data.Timer.ConfigurationB\r\n\x0bTimerAction\x1a\x82\x03\n\x0b\x41PI_Message\x12H\n\x07trigger\x18\x01 \x01(\x0b\x32\x35.rv.data.NetworkAPI.Action.API_Message.TriggerMessageH\x00\x12\x44\n\x05\x63lear\x18\x02 \x01(\x0b\x32\x33.rv.data.NetworkAPI.Action.API_Message.ClearMessageH\x00\x1a\x82\x01\n\x0eTriggerMessage\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x12\x31\n\x0ctoken_values\x18\x02 \x03(\x0b\x32\x1b.rv.data.Message.TokenValue\x1aM\n\x0c\x43learMessage\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifierB\x0f\n\rMessageAction\x1aJ\n\tAPI_Macro\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x1aI\n\x08\x41PI_Look\x12=\n\nidentifier\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x1a\xd7\x04\n\tAPI_Stage\x12\x44\n\x07layouts\x18\x01 \x01(\x0b\x32\x31.rv.data.NetworkAPI.Action.API_Stage.StageLayoutsH\x00\x12\x44\n\x07message\x18\x02 \x01(\x0b\x32\x31.rv.data.NetworkAPI.Action.API_Stage.StageMessageH\x00\x1aN\n\x0cStageLayouts\x12>\n\x07layouts\x18\x01 \x03(\x0b\x32-.rv.data.NetworkAPI.IndexOrNameIdentifierPair\x1a\xde\x02\n\x0cStageMessage\x12U\n\x0cshow_message\x18\x01 \x01(\x0b\x32=.rv.data.NetworkAPI.Action.API_Stage.StageMessage.ShowMessageH\x00\x12W\n\rclear_message\x18\x02 \x01(\x0b\x32>.rv.data.NetworkAPI.Action.API_Stage.StageMessage.ClearMessageH\x00\x12U\n\x0chide_message\x18\x03 \x01(\x0b\x32=.rv.data.NetworkAPI.Action.API_Stage.StageMessage.HideMessageH\x00\x1a\x1e\n\x0bShowMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x1a\x0e\n\x0c\x43learMessage\x1a\r\n\x0bHideMessageB\x08\n\x06\x41\x63tionB\r\n\x0bStageAction\x1a\x0f\n\rStatusRequest\x1a\x0c\n\nAPI_Status\x1a\x7f\n\x12\x41PI_StatusResponse\x12:\n\x10group_definition\x18\x01 \x01(\x0b\x32 .rv.data.ProLink.GroupDefinition\x12-\n\x06status\x18\x02 \x01(\x0b\x32\x1d.rv.data.ProLink.MemberStatusB\t\n\x07\x43ommand\x1a\x45\n\x15IndexOrNameIdentifier\x12\x0f\n\x05index\x18\x01 \x01(\x05H\x00\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x42\x0b\n\tComponent\x1a\x8d\x01\n\x19IndexOrNameIdentifierPair\x12\x36\n\x03key\x18\x01 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifier\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).rv.data.NetworkAPI.IndexOrNameIdentifierB\t\n\x07\x43ommandb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PROAPIIN']._serialized_start=109
  _globals['_PROAPIIN']._serialized_end=278
  _globals['_PROAPIOUT']._serialized_start=281
  _globals['_PROAPIOUT']._serialized_end=509
  _globals['_PROAPINETWORKCONFIGURATION']._serialized_start=512
  _globals['_PROAPINETWORKCONFIGURATION']._serialized_end=845
  _globals['_PROLINK']._serialized_start=848
  _globals['_PROLINK']._serialized_end=6808
  _globals['_PROLINK_GROUPDEFINITION']._serialized_start=860
  _globals['_PROLINK_GROUPDEFINITION']._serialized_end=1081
  _globals['_PROLINK_GROUPDEFINITION_MEMBER']._serialized_start=1047
  _globals['_PROLINK_GROUPDEFINITION_MEMBER']._serialized_end=1081
  _globals['_PROLINK_ZEROCONFIG']._serialized_start=1084
  _globals['_PROLINK_ZEROCONFIG']._serialized_end=1352
  _globals['_PROLINK_ZEROCONFIG_NETWORKENVIRONMENT']._serialized_start=1099
  _globals['_PROLINK_ZEROCONFIG_NETWORKENVIRONMENT']._serialized_end=1237
  _globals['_PROLINK_ZEROCONFIG_MULTICASTPACKET']._serialized_start=1239
  _globals['_PROLINK_ZEROCONFIG_MULTICASTPACKET']._serialized_end=1352
  _globals['_PROLINK_TOWERMESSAGE']._serialized_start=1355
  _globals['_PROLINK_TOWERMESSAGE']._serialized_end=2222
  _globals['_PROLINK_TOWERMESSAGE_TOWERSTATUSREQUEST']._serialized_start=1371
  _globals['_PROLINK_TOWERMESSAGE_TOWERSTATUSREQUEST']._serialized_end=1391
  _globals['_PROLINK_TOWERMESSAGE_TOWERSTATUSRESPONSE']._serialized_start=1393
  _globals['_PROLINK_TOWERMESSAGE_TOWERSTATUSRESPONSE']._serialized_end=1509
  _globals['_PROLINK_TOWERMESSAGE_TOWERADDMEMBERREQUEST']._serialized_start=1512
  _globals['_PROLINK_TOWERMESSAGE_TOWERADDMEMBERREQUEST']._serialized_end=1675
  _globals['_PROLINK_TOWERMESSAGE_TOWERREMOVEMEMBERREQUEST']._serialized_start=1677
  _globals['_PROLINK_TOWERMESSAGE_TOWERREMOVEMEMBERREQUEST']._serialized_end=1769
  _globals['_PROLINK_TOWERMESSAGE_TOWERADDMEMBERRESPONSE']._serialized_start=1772
  _globals['_PROLINK_TOWERMESSAGE_TOWERADDMEMBERRESPONSE']._serialized_end=2111
  _globals['_PROLINK_TOWERMESSAGE_TOWERADDMEMBERRESPONSE_ACCEPT']._serialized_start=2033
  _globals['_PROLINK_TOWERMESSAGE_TOWERADDMEMBERRESPONSE_ACCEPT']._serialized_end=2041
  _globals['_PROLINK_TOWERMESSAGE_TOWERADDMEMBERRESPONSE_DECLINEREASON']._serialized_start=2043
  _globals['_PROLINK_TOWERMESSAGE_TOWERADDMEMBERRESPONSE_DECLINEREASON']._serialized_end=2099
  _globals['_PROLINK_TOWERMESSAGE_TOWERHEARTBEATREQUEST']._serialized_start=2113
  _globals['_PROLINK_TOWERMESSAGE_TOWERHEARTBEATREQUEST']._serialized_end=2136
  _globals['_PROLINK_TOWERMESSAGE_TOWERHEARTBEATRESPONSE']._serialized_start=2138
  _globals['_PROLINK_TOWERMESSAGE_TOWERHEARTBEATRESPONSE']._serialized_end=2222
  _globals['_PROLINK_MEMBERSTATUS']._serialized_start=2225
  _globals['_PROLINK_MEMBERSTATUS']._serialized_end=2677
  _globals['_PROLINK_MEMBERSTATUS_PLATFORM']._serialized_start=2481
  _globals['_PROLINK_MEMBERSTATUS_PLATFORM']._serialized_end=2557
  _globals['_PROLINK_MEMBERSTATUS_CONNECTIONSTATUS']._serialized_start=2559
  _globals['_PROLINK_MEMBERSTATUS_CONNECTIONSTATUS']._serialized_end=2677
  _globals['_PROLINK_CLIENTACTION']._serialized_start=2680
  _globals['_PROLINK_CLIENTACTION']._serialized_end=3167
  _globals['_PROLINK_CLIENTACTION_ADDCONNECTION']._serialized_start=2978
  _globals['_PROLINK_CLIENTACTION_ADDCONNECTION']._serialized_end=3039
  _globals['_PROLINK_CLIENTACTION_REMOVECONNECTION']._serialized_start=3041
  _globals['_PROLINK_CLIENTACTION_REMOVECONNECTION']._serialized_end=3085
  _globals['_PROLINK_CLIENTACTION_CANCELACTION']._serialized_start=3087
  _globals['_PROLINK_CLIENTACTION_CANCELACTION']._serialized_end=3101
  _globals['_PROLINK_CLIENTACTION_RENDERTIME']._serialized_start=3103
  _globals['_PROLINK_CLIENTACTION_RENDERTIME']._serialized_end=3153
  _globals['_PROLINK_HANDLERIN']._serialized_start=3170
  _globals['_PROLINK_HANDLERIN']._serialized_end=6032
  _globals['_PROLINK_HANDLERIN_GROUPNAME']._serialized_start=4089
  _globals['_PROLINK_HANDLERIN_GROUPNAME']._serialized_end=4100
  _globals['_PROLINK_HANDLERIN_GROUPDEFINITIONREQUEST']._serialized_start=4102
  _globals['_PROLINK_HANDLERIN_GROUPDEFINITIONREQUEST']._serialized_end=4126
  _globals['_PROLINK_HANDLERIN_GROUPJOINCONFIRMATION']._serialized_start=4128
  _globals['_PROLINK_HANDLERIN_GROUPJOINCONFIRMATION']._serialized_end=4165
  _globals['_PROLINK_HANDLERIN_GROUPJOINPASSWORD']._serialized_start=4167
  _globals['_PROLINK_HANDLERIN_GROUPJOINPASSWORD']._serialized_end=4200
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT']._serialized_start=4203
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT']._serialized_end=5578
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_SUCCESS']._serialized_start=4376
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_SUCCESS']._serialized_end=4449
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE']._serialized_start=4452
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE']._serialized_end=5568
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_UNEXPECTED']._serialized_start=5299
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_UNEXPECTED']._serialized_end=5311
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_DECLINED']._serialized_start=5313
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_DECLINED']._serialized_end=5323
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_TIMEOUT']._serialized_start=5325
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_TIMEOUT']._serialized_end=5334
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_LINKDISABLED']._serialized_start=5336
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_LINKDISABLED']._serialized_end=5350
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_INOTHERGROUP']._serialized_start=5352
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_INOTHERGROUP']._serialized_end=5407
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_INVALIDIPADDRESS']._serialized_start=5409
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_INVALIDIPADDRESS']._serialized_end=5427
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_ALREADYINGROUP']._serialized_start=5429
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_ALREADYINGROUP']._serialized_end=5486
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_COULDNOTADD']._serialized_start=5488
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_COULDNOTADD']._serialized_end=5522
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_COULDNOTJOIN']._serialized_start=5524
  _globals['_PROLINK_HANDLERIN_ADDCONNECTIONRESULT_FAILURE_COULDNOTJOIN']._serialized_end=5558
  _globals['_PROLINK_HANDLERIN_MEMBERSTATUSCHANGE']._serialized_start=5580
  _globals['_PROLINK_HANDLERIN_MEMBERSTATUSCHANGE']._serialized_end=5648
  _globals['_PROLINK_HANDLERIN_PROPRESENTERINFO']._serialized_start=5650
  _globals['_PROLINK_HANDLERIN_PROPRESENTERINFO']._serialized_end=5668
  _globals['_PROLINK_HANDLERIN_SERVERSTATE']._serialized_start=5670
  _globals['_PROLINK_HANDLERIN_SERVERSTATE']._serialized_end=5751
  _globals['_PROLINK_HANDLERIN_CONFIGURATIONREQUEST']._serialized_start=5753
  _globals['_PROLINK_HANDLERIN_CONFIGURATIONREQUEST']._serialized_end=5775
  _globals['_PROLINK_HANDLERIN_LOGREQUEST']._serialized_start=5778
  _globals['_PROLINK_HANDLERIN_LOGREQUEST']._serialized_end=6021
  _globals['_PROLINK_HANDLERIN_LOGREQUEST_SEVERITY']._serialized_start=5876
  _globals['_PROLINK_HANDLERIN_LOGREQUEST_SEVERITY']._serialized_end=6021
  _globals['_PROLINK_HANDLEROUT']._serialized_start=6035
  _globals['_PROLINK_HANDLEROUT']._serialized_end=6808
  _globals['_PROLINK_HANDLEROUT_GROUPNAME']._serialized_start=6473
  _globals['_PROLINK_HANDLEROUT_GROUPNAME']._serialized_end=6498
  _globals['_PROLINK_HANDLEROUT_GROUPJOINCONFIRMATION']._serialized_start=6500
  _globals['_PROLINK_HANDLEROUT_GROUPJOINCONFIRMATION']._serialized_end=6539
  _globals['_PROLINK_HANDLEROUT_GROUPJOINPASSWORD']._serialized_start=6541
  _globals['_PROLINK_HANDLEROUT_GROUPJOINPASSWORD']._serialized_end=6578
  _globals['_PROLINK_HANDLEROUT_PROPRESENTERINFO']._serialized_start=6581
  _globals['_PROLINK_HANDLEROUT_PROPRESENTERINFO']._serialized_end=6796
  _globals['_PROLINK_HANDLEROUT_PROPRESENTERINFO_PLATFORM']._serialized_start=2481
  _globals['_PROLINK_HANDLEROUT_PROPRESENTERINFO_PLATFORM']._serialized_end=2557
  _globals['_NETWORKAPI']._serialized_start=6811
  _globals['_NETWORKAPI']._serialized_end=14497
  _globals['_NETWORKAPI_LINKSTATUS']._serialized_start=7047
  _globals['_NETWORKAPI_LINKSTATUS']._serialized_end=7301
  _globals['_NETWORKAPI_LINKSTATUS_PLATFORM']._serialized_start=2481
  _globals['_NETWORKAPI_LINKSTATUS_PLATFORM']._serialized_end=2557
  _globals['_NETWORKAPI_GROUP']._serialized_start=7303
  _globals['_NETWORKAPI_GROUP']._serialized_end=7419
  _globals['_NETWORKAPI_GROUP_MEMBER']._serialized_start=7377
  _globals['_NETWORKAPI_GROUP_MEMBER']._serialized_end=7419
  _globals['_NETWORKAPI_GROUPCHANGE']._serialized_start=7422
  _globals['_NETWORKAPI_GROUPCHANGE']._serialized_end=7641
  _globals['_NETWORKAPI_GROUPRESPONSE']._serialized_start=7644
  _globals['_NETWORKAPI_GROUPRESPONSE']._serialized_end=7855
  _globals['_NETWORKAPI_GROUPRESPONSE_SUCCESS']._serialized_start=4376
  _globals['_NETWORKAPI_GROUPRESPONSE_SUCCESS']._serialized_end=4385
  _globals['_NETWORKAPI_GROUPRESPONSE_STATUS']._serialized_start=7794
  _globals['_NETWORKAPI_GROUPRESPONSE_STATUS']._serialized_end=7843
  _globals['_NETWORKAPI_GROUPSTATUS']._serialized_start=7857
  _globals['_NETWORKAPI_GROUPSTATUS']._serialized_end=7920
  _globals['_NETWORKAPI_GROUPINVITE']._serialized_start=7923
  _globals['_NETWORKAPI_GROUPINVITE']._serialized_end=8051
  _globals['_NETWORKAPI_GROUPJOIN']._serialized_start=8053
  _globals['_NETWORKAPI_GROUPJOIN']._serialized_end=8167
  _globals['_NETWORKAPI_GROUPKICK']._serialized_start=8169
  _globals['_NETWORKAPI_GROUPKICK']._serialized_end=8230
  _globals['_NETWORKAPI_SERVERSTATE']._serialized_start=8232
  _globals['_NETWORKAPI_SERVERSTATE']._serialized_end=8296
  _globals['_NETWORKAPI_ACTION']._serialized_start=8299
  _globals['_NETWORKAPI_ACTION']._serialized_end=14271
  _globals['_NETWORKAPI_ACTION_API_CLEAR']._serialized_start=9100
  _globals['_NETWORKAPI_ACTION_API_CLEAR']._serialized_end=9425
  _globals['_NETWORKAPI_ACTION_API_CLEAR_LAYER']._serialized_start=9246
  _globals['_NETWORKAPI_ACTION_API_CLEAR_LAYER']._serialized_end=9412
  _globals['_NETWORKAPI_ACTION_API_TWOSTEPTRIGGER']._serialized_start=9428
  _globals['_NETWORKAPI_ACTION_API_TWOSTEPTRIGGER']._serialized_end=10048
  _globals['_NETWORKAPI_ACTION_API_TWOSTEPTRIGGER_OPERATION']._serialized_start=9975
  _globals['_NETWORKAPI_ACTION_API_TWOSTEPTRIGGER_OPERATION']._serialized_end=10033
  _globals['_NETWORKAPI_ACTION_API_PREROLLCOMPLETE']._serialized_start=10050
  _globals['_NETWORKAPI_ACTION_API_PREROLLCOMPLETE']._serialized_end=10099
  _globals['_NETWORKAPI_ACTION_API_TRIGGER']._serialized_start=10102
  _globals['_NETWORKAPI_ACTION_API_TRIGGER']._serialized_end=11255
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_PRESENTATION']._serialized_start=10395
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_PRESENTATION']._serialized_end=10993
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_PRESENTATION_PLAYLISTPRESENTATION']._serialized_start=10640
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_PRESENTATION_PLAYLISTPRESENTATION']._serialized_end=10736
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_PRESENTATION_LIBRARYPRESENTATION']._serialized_start=10739
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_PRESENTATION_LIBRARYPRESENTATION']._serialized_end=10971
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_MEDIA']._serialized_start=10995
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_MEDIA']._serialized_end=11076
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_VIDEOINPUT']._serialized_start=11078
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_VIDEOINPUT']._serialized_end=11157
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_AUDIO']._serialized_start=11159
  _globals['_NETWORKAPI_ACTION_API_TRIGGER_AUDIO']._serialized_end=11240
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT']._serialized_start=11258
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT']._serialized_end=11981
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_PLAY']._serialized_start=11704
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_PLAY']._serialized_end=11710
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_PAUSE']._serialized_start=11712
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_PAUSE']._serialized_end=11719
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_SKIPBACKWARD']._serialized_start=11721
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_SKIPBACKWARD']._serialized_end=11752
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_SKIPFORWARD']._serialized_start=11754
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_SKIPFORWARD']._serialized_end=11784
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_GOTOEND']._serialized_start=11786
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_GOTOEND']._serialized_end=11819
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_TRANSPORTLAYER']._serialized_start=11822
  _globals['_NETWORKAPI_ACTION_API_TRANSPORT_TRANSPORTLAYER']._serialized_end=11962
  _globals['_NETWORKAPI_ACTION_API_PROP']._serialized_start=11984
  _globals['_NETWORKAPI_ACTION_API_PROP']._serialized_end=12294
  _globals['_NETWORKAPI_ACTION_API_PROP_TRIGGERPROP']._serialized_start=12128
  _globals['_NETWORKAPI_ACTION_API_PROP_TRIGGERPROP']._serialized_end=12204
  _globals['_NETWORKAPI_ACTION_API_PROP_CLEARPROP']._serialized_start=12206
  _globals['_NETWORKAPI_ACTION_API_PROP_CLEARPROP']._serialized_end=12280
  _globals['_NETWORKAPI_ACTION_API_TIMER']._serialized_start=12297
  _globals['_NETWORKAPI_ACTION_API_TIMER']._serialized_end=12958
  _globals['_NETWORKAPI_ACTION_API_TIMER_STARTTIMER']._serialized_start=12580
  _globals['_NETWORKAPI_ACTION_API_TIMER_STARTTIMER']._serialized_end=12655
  _globals['_NETWORKAPI_ACTION_API_TIMER_STOPTIMER']._serialized_start=12657
  _globals['_NETWORKAPI_ACTION_API_TIMER_STOPTIMER']._serialized_end=12731
  _globals['_NETWORKAPI_ACTION_API_TIMER_RESETTIMER']._serialized_start=12733
  _globals['_NETWORKAPI_ACTION_API_TIMER_RESETTIMER']._serialized_end=12808
  _globals['_NETWORKAPI_ACTION_API_TIMER_CONFIGURETIMER']._serialized_start=12811
  _globals['_NETWORKAPI_ACTION_API_TIMER_CONFIGURETIMER']._serialized_end=12943
  _globals['_NETWORKAPI_ACTION_API_MESSAGE']._serialized_start=12961
  _globals['_NETWORKAPI_ACTION_API_MESSAGE']._serialized_end=13347
  _globals['_NETWORKAPI_ACTION_API_MESSAGE_TRIGGERMESSAGE']._serialized_start=13121
  _globals['_NETWORKAPI_ACTION_API_MESSAGE_TRIGGERMESSAGE']._serialized_end=13251
  _globals['_NETWORKAPI_ACTION_API_MESSAGE_CLEARMESSAGE']._serialized_start=13253
  _globals['_NETWORKAPI_ACTION_API_MESSAGE_CLEARMESSAGE']._serialized_end=13330
  _globals['_NETWORKAPI_ACTION_API_MACRO']._serialized_start=13349
  _globals['_NETWORKAPI_ACTION_API_MACRO']._serialized_end=13423
  _globals['_NETWORKAPI_ACTION_API_LOOK']._serialized_start=13425
  _globals['_NETWORKAPI_ACTION_API_LOOK']._serialized_end=13498
  _globals['_NETWORKAPI_ACTION_API_STAGE']._serialized_start=13501
  _globals['_NETWORKAPI_ACTION_API_STAGE']._serialized_end=14100
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGELAYOUTS']._serialized_start=13654
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGELAYOUTS']._serialized_end=13732
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGEMESSAGE']._serialized_start=13735
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGEMESSAGE']._serialized_end=14085
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGEMESSAGE_SHOWMESSAGE']._serialized_start=14014
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGEMESSAGE_SHOWMESSAGE']._serialized_end=14044
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGEMESSAGE_CLEARMESSAGE']._serialized_start=13253
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGEMESSAGE_CLEARMESSAGE']._serialized_end=13267
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGEMESSAGE_HIDEMESSAGE']._serialized_start=14062
  _globals['_NETWORKAPI_ACTION_API_STAGE_STAGEMESSAGE_HIDEMESSAGE']._serialized_end=14075
  _globals['_NETWORKAPI_ACTION_STATUSREQUEST']._serialized_start=14102
  _globals['_NETWORKAPI_ACTION_STATUSREQUEST']._serialized_end=14117
  _globals['_NETWORKAPI_ACTION_API_STATUS']._serialized_start=14119
  _globals['_NETWORKAPI_ACTION_API_STATUS']._serialized_end=14131
  _globals['_NETWORKAPI_ACTION_API_STATUSRESPONSE']._serialized_start=14133
  _globals['_NETWORKAPI_ACTION_API_STATUSRESPONSE']._serialized_end=14260
  _globals['_NETWORKAPI_INDEXORNAMEIDENTIFIER']._serialized_start=14273
  _globals['_NETWORKAPI_INDEXORNAMEIDENTIFIER']._serialized_end=14342
  _globals['_NETWORKAPI_INDEXORNAMEIDENTIFIERPAIR']._serialized_start=14345
  _globals['_NETWORKAPI_INDEXORNAMEIDENTIFIERPAIR']._serialized_end=14486
# @@protoc_insertion_point(module_scope)
