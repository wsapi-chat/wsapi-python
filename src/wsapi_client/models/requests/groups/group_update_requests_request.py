from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class GroupUpdateRequestsRequest(BaseModel):
    participants: list[str] = Field(alias="participants")
    action: Literal["approve", "reject"] = Field(alias="action")

    model_config = ConfigDict(populate_by_name=True)
