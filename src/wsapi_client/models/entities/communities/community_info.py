from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..groups.group_info import GroupParticipant, Identity


class CommunityInfoResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    community_id: Optional[str] = Field(None, alias="communityId")
    owner: Optional[Identity] = None
    name: Optional[str] = None
    created: Optional[str] = None
    description: Optional[str] = None
    is_locked: Optional[bool] = Field(None, alias="isLocked")
    community_approval_mode: Optional[str] = Field(None, alias="communityApprovalMode")
    participants: Optional[List[GroupParticipant]] = None
