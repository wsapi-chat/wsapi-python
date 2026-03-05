from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupUpdateNameRequest(BaseModel):
    name: str = Field(alias="name")

    model_config = ConfigDict(populate_by_name=True)
