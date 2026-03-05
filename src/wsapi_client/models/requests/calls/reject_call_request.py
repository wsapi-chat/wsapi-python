from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class RejectCallRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    caller_id: str = Field(alias="callerId")
