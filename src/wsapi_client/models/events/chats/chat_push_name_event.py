from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ...entities.groups.group_info import Identity


class ChatPushNameEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user: Optional[Identity] = None
    push_name: Optional[str] = Field(None, alias="pushName")
