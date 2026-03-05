from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SessionLoggedInEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    device_id: str = Field(alias="deviceId")
