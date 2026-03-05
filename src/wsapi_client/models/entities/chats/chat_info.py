from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ChatListItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    lid: Optional[str] = None
    is_group: Optional[bool] = Field(None, alias="isGroup")
    is_archived: Optional[bool] = Field(None, alias="isArchived")
    is_pinned: Optional[bool] = Field(None, alias="isPinned")
    is_muted: Optional[bool] = Field(None, alias="isMuted")
    mute_end_time: Optional[str] = Field(None, alias="muteEndTime")
    push_name: Optional[str] = Field(None, alias="pushName")
    business_name: Optional[str] = Field(None, alias="businessName")
    full_name: Optional[str] = Field(None, alias="fullName")
    last_activity: Optional[str] = Field(None, alias="lastActivity")
