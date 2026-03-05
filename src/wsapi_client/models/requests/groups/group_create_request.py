from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupCreateRequest(BaseModel):
    name: str = Field(alias="name")
    participants: list[str] = Field(alias="participants", default_factory=list)

    model_config = ConfigDict(populate_by_name=True)
