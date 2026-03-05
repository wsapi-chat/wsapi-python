from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SessionStatus(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_connected: bool = Field(alias="isConnected")
    is_logged_in: bool = Field(alias="isLoggedIn")
    device_id: Optional[str] = Field(default=None, alias="deviceId")
