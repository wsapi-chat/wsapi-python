from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ChatArchive(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_archived: bool = Field(alias="isArchived")
