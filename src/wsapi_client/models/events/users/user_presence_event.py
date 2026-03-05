from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ...entities.groups.group_info import Identity


class UserPresenceEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user: Optional[Identity] = None
    status: Optional[str] = None
    last_seen: Optional[str] = Field(None, alias="lastSeen")
