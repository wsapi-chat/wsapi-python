from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from ...entities.groups.group_info import Identity
from ...entities.users.sender import Sender


class GroupDescription(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    topic: Optional[str] = None


class GroupName(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    name_set_at: Optional[str] = Field(None, alias="nameSetAt")


class GroupLocked(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_locked: Optional[bool] = Field(None, alias="isLocked")


class GroupAnnounce(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_announce: Optional[bool] = Field(None, alias="isAnnounce")


class GroupLink(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    group: Optional[Identity] = None
    group_type: Optional[str] = Field(None, alias="groupType")


class GroupUnlink(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    group: Optional[Identity] = None
    group_type: Optional[str] = Field(None, alias="groupType")


class GroupMembershipApproval(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_join_approval_required: Optional[bool] = Field(None, alias="isJoinApprovalRequired")


class GroupDelete(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    deleted: Optional[bool] = None
    deleted_reason: Optional[str] = Field(None, alias="deletedReason")


class GroupEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: Optional[str] = None
    sender: Optional[Sender] = None
    timestamp: Optional[str] = None
    is_community: Optional[bool] = Field(None, alias="isCommunity")
    community_id: Optional[str] = Field(None, alias="communityId")
    is_announcement_group: Optional[bool] = Field(None, alias="isAnnouncementGroup")
    join_reason: Optional[str] = Field(None, alias="joinReason")
    group_type: Optional[str] = Field(None, alias="groupType")
    name: Optional[GroupName] = None
    description: Optional[GroupDescription] = None
    locked: Optional[GroupLocked] = None
    announce: Optional[GroupAnnounce] = None
    join: Optional[List[Identity]] = None
    leave: Optional[List[Identity]] = None
    promote: Optional[List[Identity]] = None
    demote: Optional[List[Identity]] = None
    link: Optional[GroupLink] = None
    unlink: Optional[GroupUnlink] = None
    membership_approval: Optional[GroupMembershipApproval] = Field(None, alias="membershipApproval")
    delete: Optional[GroupDelete] = None
    suspended: Optional[bool] = None
