from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateCommunityRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str
    participants: Optional[List[str]] = None
    approval_mode: Optional[str] = Field(None, alias="approvalMode")


class CreateCommunityGroupRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str
    participants: Optional[List[str]] = None


class LinkGroupRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_id: str = Field(alias="groupId")
