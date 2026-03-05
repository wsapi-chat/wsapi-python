from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupSetLockedRequest(BaseModel):
    enabled: bool = Field(alias="enabled")

    model_config = ConfigDict(populate_by_name=True)
