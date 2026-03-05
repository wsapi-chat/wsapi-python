from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CommunitySubGroupResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_id: Optional[str] = Field(None, alias="groupId")
    name: Optional[str] = None
    name_set_at: Optional[str] = Field(None, alias="nameSetAt")
    is_announcement_group: Optional[bool] = Field(None, alias="isAnnouncementGroup")
