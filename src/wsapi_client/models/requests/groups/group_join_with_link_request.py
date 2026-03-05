from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupJoinWithLinkRequest(BaseModel):
    code: str = Field(alias="code")

    model_config = ConfigDict(populate_by_name=True)
