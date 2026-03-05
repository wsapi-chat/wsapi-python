from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ChatUpdateArchiveRequest(BaseModel):
    archived: bool = Field(alias="archived")

    model_config = ConfigDict(populate_by_name=True)
