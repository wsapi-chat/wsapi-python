from __future__ import annotations

import builtins

from ..http import ApiResponse, WSApiHttp
from ..models.entities.groups.group_info import GroupInfoResponse, GroupParticipant
from ..models.entities.groups.group_invite_info import GroupInviteInfo
from ..models.entities.groups.group_invite_link import GroupInviteLink
from ..models.entities.groups.group_join_request import GroupParticipantRequest
from ..models.entities.groups.group_picture_updated import GroupPictureUpdated
from ..models.entities.messages.message_created import MessageCreated
from ..models.requests.groups.group_create_request import GroupCreateRequest
from ..models.requests.groups.group_join_with_invite_request import GroupJoinWithInviteRequest
from ..models.requests.groups.group_join_with_link_request import GroupJoinWithLinkRequest
from ..models.requests.groups.group_set_announce_request import GroupSetAnnounceRequest
from ..models.requests.groups.group_set_join_approval_request import GroupSetJoinApprovalRequest
from ..models.requests.groups.group_set_locked_request import GroupSetLockedRequest
from ..models.requests.groups.group_set_member_add_mode_request import GroupSetMemberAddModeRequest
from ..models.requests.groups.group_update_description_request import GroupUpdateDescriptionRequest
from ..models.requests.groups.group_update_name_request import GroupUpdateNameRequest
from ..models.requests.groups.group_update_participants_request import GroupUpdateParticipantsRequest
from ..models.requests.groups.group_update_picture_request import GroupUpdatePictureRequest
from ..models.requests.groups.group_update_requests_request import GroupUpdateRequestsRequest


class GroupsClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def list(self) -> list[GroupInfoResponse]:
        return self._http.send_json("GET", "/groups", model=list[GroupInfoResponse])

    def get(self, group_id: str) -> GroupInfoResponse:
        return self._http.send_json("GET", f"/groups/{group_id}", model=GroupInfoResponse)

    def create(self, request: GroupCreateRequest) -> MessageCreated:
        return self._http.send_json("POST", "/groups", model=MessageCreated, json=request.model_dump(by_alias=True))

    def update_description(self, group_id: str, request: GroupUpdateDescriptionRequest) -> None:
        self._http.send_json(
            "PUT", f"/groups/{group_id}/description", model=None, json=request.model_dump(by_alias=True)
        )

    def update_name(self, group_id: str, request: GroupUpdateNameRequest) -> None:
        self._http.send_json("PUT", f"/groups/{group_id}/name", model=None, json=request.model_dump(by_alias=True))

    def update_picture(self, group_id: str, request: GroupUpdatePictureRequest) -> GroupPictureUpdated:
        return self._http.send_json(
            "POST", f"/groups/{group_id}/picture", model=GroupPictureUpdated, json=request.model_dump(by_alias=True)
        )

    def leave(self, group_id: str) -> None:
        self._http.send_json("POST", f"/groups/{group_id}/leave", model=None)

    def delete(self, group_id: str) -> None:
        """Alias for leave() - leaves the group."""
        self.leave(group_id)

    def get_invite_link(self, group_id: str) -> GroupInviteLink:
        return self._http.send_json("GET", f"/groups/{group_id}/invite-link", model=GroupInviteLink)

    def reset_invite_link(self, group_id: str) -> GroupInviteLink:
        return self._http.send_json("POST", f"/groups/{group_id}/invite-link/reset", model=GroupInviteLink)

    def get_requests(self, group_id: str) -> builtins.list[GroupParticipantRequest]:
        return self._http.send_json("GET", f"/groups/{group_id}/requests", model=list[GroupParticipantRequest])

    def update_requests(self, group_id: str, request: GroupUpdateRequestsRequest) -> None:
        self._http.send_json("PUT", f"/groups/{group_id}/requests", model=None, json=request.model_dump(by_alias=True))

    def update_participants(self, group_id: str, request: GroupUpdateParticipantsRequest) -> None:
        self._http.send_json(
            "PUT", f"/groups/{group_id}/participants", model=None, json=request.model_dump(by_alias=True)
        )

    def get_participants(self, group_id: str) -> builtins.list[GroupParticipant]:
        return self._http.send_json("GET", f"/groups/{group_id}/participants", model=list[GroupParticipant])

    def set_announce(self, group_id: str, request: GroupSetAnnounceRequest) -> None:
        self._http.send_json(
            "PUT", f"/groups/{group_id}/settings/announce", model=None, json=request.model_dump(by_alias=True)
        )

    def set_locked(self, group_id: str, request: GroupSetLockedRequest) -> None:
        self._http.send_json(
            "PUT", f"/groups/{group_id}/settings/locked", model=None, json=request.model_dump(by_alias=True)
        )

    def set_join_approval(self, group_id: str, request: GroupSetJoinApprovalRequest) -> None:
        self._http.send_json(
            "PUT", f"/groups/{group_id}/settings/join-approval", model=None, json=request.model_dump(by_alias=True)
        )

    def set_member_add_mode(self, group_id: str, request: GroupSetMemberAddModeRequest) -> None:
        self._http.send_json(
            "PUT", f"/groups/{group_id}/settings/member-add-mode", model=None, json=request.model_dump(by_alias=True)
        )

    def join_with_link(self, request: GroupJoinWithLinkRequest) -> None:
        self._http.send_json("POST", "/groups/join/link", model=None, json=request.model_dump(by_alias=True))

    def join_with_invite(self, request: GroupJoinWithInviteRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", "/groups/join/invite", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def get_invite_info(self, invite_code: str) -> GroupInviteInfo:
        return self._http.send_json("GET", f"/groups/invite/{invite_code}", model=GroupInviteInfo)

    # Try variants
    def try_list(self) -> ApiResponse[list[GroupInfoResponse]]:
        return self._http.try_send_json("GET", "/groups", model=list[GroupInfoResponse])

    def try_get(self, group_id: str) -> ApiResponse[GroupInfoResponse]:
        return self._http.try_send_json("GET", f"/groups/{group_id}", model=GroupInfoResponse)

    def try_create(self, request: GroupCreateRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json("POST", "/groups", model=MessageCreated, json=request.model_dump(by_alias=True))

    def try_update_description(self, group_id: str, request: GroupUpdateDescriptionRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/groups/{group_id}/description", model=None, json=request.model_dump(by_alias=True)
        )

    def try_update_name(self, group_id: str, request: GroupUpdateNameRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/groups/{group_id}/name", model=None, json=request.model_dump(by_alias=True)
        )

    def try_update_picture(self, group_id: str, request: GroupUpdatePictureRequest) -> ApiResponse[GroupPictureUpdated]:
        return self._http.try_send_json(
            "POST", f"/groups/{group_id}/picture", model=GroupPictureUpdated, json=request.model_dump(by_alias=True)
        )

    def try_leave(self, group_id: str) -> ApiResponse[None]:
        return self._http.try_send_json("POST", f"/groups/{group_id}/leave", model=None)

    def try_delete(self, group_id: str) -> ApiResponse[None]:
        """Alias for try_leave() - leaves the group."""
        return self.try_leave(group_id)

    def try_get_invite_link(self, group_id: str) -> ApiResponse[GroupInviteLink]:
        return self._http.try_send_json("GET", f"/groups/{group_id}/invite-link", model=GroupInviteLink)

    def try_reset_invite_link(self, group_id: str) -> ApiResponse[GroupInviteLink]:
        return self._http.try_send_json("POST", f"/groups/{group_id}/invite-link/reset", model=GroupInviteLink)

    def try_get_requests(self, group_id: str) -> ApiResponse[builtins.list[GroupParticipantRequest]]:
        return self._http.try_send_json("GET", f"/groups/{group_id}/requests", model=list[GroupParticipantRequest])

    def try_update_requests(self, group_id: str, request: GroupUpdateRequestsRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/groups/{group_id}/requests", model=None, json=request.model_dump(by_alias=True)
        )

    def try_update_participants(self, group_id: str, request: GroupUpdateParticipantsRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/groups/{group_id}/participants", model=None, json=request.model_dump(by_alias=True)
        )

    def try_get_participants(self, group_id: str) -> ApiResponse[builtins.list[GroupParticipant]]:
        return self._http.try_send_json("GET", f"/groups/{group_id}/participants", model=list[GroupParticipant])

    def try_set_announce(self, group_id: str, request: GroupSetAnnounceRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/groups/{group_id}/settings/announce", model=None, json=request.model_dump(by_alias=True)
        )

    def try_set_locked(self, group_id: str, request: GroupSetLockedRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/groups/{group_id}/settings/locked", model=None, json=request.model_dump(by_alias=True)
        )

    def try_set_join_approval(self, group_id: str, request: GroupSetJoinApprovalRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/groups/{group_id}/settings/join-approval", model=None, json=request.model_dump(by_alias=True)
        )

    def try_set_member_add_mode(self, group_id: str, request: GroupSetMemberAddModeRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/groups/{group_id}/settings/member-add-mode", model=None, json=request.model_dump(by_alias=True)
        )

    def try_join_with_link(self, request: GroupJoinWithLinkRequest) -> ApiResponse[None]:
        return self._http.try_send_json("POST", "/groups/join/link", model=None, json=request.model_dump(by_alias=True))

    def try_join_with_invite(self, request: GroupJoinWithInviteRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "/groups/join/invite", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def try_get_invite_info(self, invite_code: str) -> ApiResponse[GroupInviteInfo]:
        return self._http.try_send_json("GET", f"/groups/invite/{invite_code}", model=GroupInviteInfo)
