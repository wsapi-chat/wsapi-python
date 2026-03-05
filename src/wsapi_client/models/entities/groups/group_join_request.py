from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .group_info import Identity


class GroupParticipantRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user: Optional[Identity] = None
    requested_at: Optional[str] = Field(None, alias="requestedAt")
