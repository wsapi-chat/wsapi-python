from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupCreated(BaseModel):
    id: str = Field(alias="id")

    model_config = ConfigDict(populate_by_name=True)
