from __future__ import annotations

from typing import List

from pydantic import BaseModel, ConfigDict, Field


class GroupCreateRequest(BaseModel):
    name: str = Field(alias="name")
    participants: List[str] = Field(alias="participants", default_factory=list)
    """Initial participant JIDs. Optional: leave empty to create a group with only the paired account."""

    model_config = ConfigDict(populate_by_name=True)
