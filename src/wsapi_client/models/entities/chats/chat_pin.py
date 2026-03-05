from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ChatPin(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    is_pinned: bool = Field(alias="isPinned")
