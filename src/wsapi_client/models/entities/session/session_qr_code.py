from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SessionQRCode(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    code: str = Field(alias="code")
