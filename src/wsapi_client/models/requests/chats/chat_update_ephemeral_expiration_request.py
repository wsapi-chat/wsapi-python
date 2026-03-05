from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ChatUpdateEphemeralExpirationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    expiration: Literal["off", "24h", "7d", "90d"] = Field(alias="expiration")
