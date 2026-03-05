from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ChatUpdatePinRequest(BaseModel):
    pinned: bool = Field(alias="pinned")

    model_config = ConfigDict(populate_by_name=True)
