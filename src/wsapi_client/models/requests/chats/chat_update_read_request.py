from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ChatUpdateReadRequest(BaseModel):
    read: bool = Field(alias="read")

    model_config = ConfigDict(populate_by_name=True)
