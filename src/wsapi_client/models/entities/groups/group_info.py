from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Identity(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    lid: Optional[str] = None
    phone: Optional[str] = None
    device: Optional[int] = None


class GroupParticipant(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    lid: Optional[str] = None
    phone: Optional[str] = None
    device: Optional[int] = None
    is_admin: Optional[bool] = Field(None, alias="isAdmin")
    is_super_admin: Optional[bool] = Field(None, alias="isSuperAdmin")
    display_name: Optional[str] = Field(None, alias="displayName")


class GroupInfoResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_id: Optional[str] = Field(None, alias="groupId")
    owner: Optional[Identity] = None
    name: Optional[str] = None
    created_at: Optional[str] = Field(None, alias="createdAt")
    description: Optional[str] = None
    is_announce: Optional[bool] = Field(None, alias="isAnnounce")
    is_locked: Optional[bool] = Field(None, alias="isLocked")
    is_ephemeral: Optional[bool] = Field(None, alias="isEphemeral")
    ephemeral_expiration: Optional[int] = Field(None, alias="ephemeralExpiration")
    participants: Optional[list[GroupParticipant]] = None
    community_id: Optional[str] = Field(None, alias="communityId")
    is_announcement_group: Optional[bool] = Field(None, alias="isAnnouncementGroup")
    is_join_approval_required: Optional[bool] = Field(None, alias="isJoinApprovalRequired")
    member_add_mode: Optional[str] = Field(None, alias="memberAddMode")
