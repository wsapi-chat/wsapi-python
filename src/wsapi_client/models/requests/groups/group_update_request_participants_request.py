from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupUpdateRequestParticipantsRequest(BaseModel):
    participants: list[str] = Field(alias="participants", default_factory=list)
    action: str = Field(alias="action")

    model_config = ConfigDict(populate_by_name=True)
