from __future__ import annotations

from ..http import ApiResponse, WSApiHttp
from ..models.entities.communities.community_info import CommunityInfoResponse
from ..models.entities.communities.community_sub_group import CommunitySubGroupResponse
from ..models.entities.groups.group_info import Identity
from ..models.entities.messages.message_created import MessageCreated


class CommunitiesClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def list(self) -> list[CommunityInfoResponse]:
        return self._http.send_json("GET", "/communities", model=list[CommunityInfoResponse])

    def create(self, request) -> MessageCreated:
        return self._http.send_json(
            "POST", "/communities", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def get(self, community_id: str) -> CommunityInfoResponse:
        return self._http.send_json("GET", f"/communities/{community_id}", model=CommunityInfoResponse)

    def leave(self, community_id: str) -> None:
        self._http.send_json("POST", f"/communities/{community_id}/leave", model=None)

    def set_name(self, community_id: str, request) -> None:
        self._http.send_json(
            "PUT", f"/communities/{community_id}/name", model=None, json=request.model_dump(by_alias=True)
        )

    def set_description(self, community_id: str, request) -> None:
        self._http.send_json(
            "PUT", f"/communities/{community_id}/description", model=None, json=request.model_dump(by_alias=True)
        )

    def set_picture(self, community_id: str, request) -> dict:
        return self._http.send_json(
            "POST", f"/communities/{community_id}/picture", model=dict, json=request.model_dump(by_alias=True)
        )

    def set_locked(self, community_id: str, request) -> None:
        self._http.send_json(
            "PUT", f"/communities/{community_id}/settings/locked", model=None, json=request.model_dump(by_alias=True)
        )

    def get_participants(self, community_id: str) -> list[Identity]:
        return self._http.send_json("GET", f"/communities/{community_id}/participants", model=list[Identity])

    def update_participants(self, community_id: str, request) -> None:
        self._http.send_json(
            "PUT", f"/communities/{community_id}/participants", model=None, json=request.model_dump(by_alias=True)
        )

    def get_invite_link(self, community_id: str) -> dict:
        return self._http.send_json("GET", f"/communities/{community_id}/invite-link", model=dict)

    def reset_invite_link(self, community_id: str) -> dict:
        return self._http.send_json("POST", f"/communities/{community_id}/invite-link/reset", model=dict)

    def get_sub_groups(self, community_id: str) -> list[CommunitySubGroupResponse]:
        return self._http.send_json("GET", f"/communities/{community_id}/groups", model=list[CommunitySubGroupResponse])

    def create_group(self, community_id: str, request) -> MessageCreated:
        return self._http.send_json(
            "POST", f"/communities/{community_id}/groups", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def link_group(self, community_id: str, request) -> None:
        self._http.send_json(
            "PUT", f"/communities/{community_id}/groups/link", model=None, json=request.model_dump(by_alias=True)
        )

    def unlink_group(self, community_id: str, request) -> None:
        self._http.send_json(
            "PUT", f"/communities/{community_id}/groups/unlink", model=None, json=request.model_dump(by_alias=True)
        )

    # Try variants
    def try_list(self) -> ApiResponse[list[CommunityInfoResponse]]:
        return self._http.try_send_json("GET", "/communities", model=list[CommunityInfoResponse])

    def try_create(self, request) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "/communities", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def try_get(self, community_id: str) -> ApiResponse[CommunityInfoResponse]:
        return self._http.try_send_json("GET", f"/communities/{community_id}", model=CommunityInfoResponse)

    def try_leave(self, community_id: str) -> ApiResponse[None]:
        return self._http.try_send_json("POST", f"/communities/{community_id}/leave", model=None)

    def try_set_name(self, community_id: str, request) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/communities/{community_id}/name", model=None, json=request.model_dump(by_alias=True)
        )

    def try_set_description(self, community_id: str, request) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/communities/{community_id}/description", model=None, json=request.model_dump(by_alias=True)
        )

    def try_set_picture(self, community_id: str, request) -> ApiResponse[dict]:
        return self._http.try_send_json(
            "POST", f"/communities/{community_id}/picture", model=dict, json=request.model_dump(by_alias=True)
        )

    def try_set_locked(self, community_id: str, request) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/communities/{community_id}/settings/locked", model=None, json=request.model_dump(by_alias=True)
        )

    def try_get_participants(self, community_id: str) -> ApiResponse[list[Identity]]:
        return self._http.try_send_json("GET", f"/communities/{community_id}/participants", model=list[Identity])

    def try_update_participants(self, community_id: str, request) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/communities/{community_id}/participants", model=None, json=request.model_dump(by_alias=True)
        )

    def try_get_invite_link(self, community_id: str) -> ApiResponse[dict]:
        return self._http.try_send_json("GET", f"/communities/{community_id}/invite-link", model=dict)

    def try_reset_invite_link(self, community_id: str) -> ApiResponse[dict]:
        return self._http.try_send_json("POST", f"/communities/{community_id}/invite-link/reset", model=dict)

    def try_get_sub_groups(self, community_id: str) -> ApiResponse[list[CommunitySubGroupResponse]]:
        return self._http.try_send_json(
            "GET", f"/communities/{community_id}/groups", model=list[CommunitySubGroupResponse]
        )

    def try_create_group(self, community_id: str, request) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", f"/communities/{community_id}/groups", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def try_link_group(self, community_id: str, request) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/communities/{community_id}/groups/link", model=None, json=request.model_dump(by_alias=True)
        )

    def try_unlink_group(self, community_id: str, request) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/communities/{community_id}/groups/unlink", model=None, json=request.model_dump(by_alias=True)
        )
