from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Sender(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    lid: Optional[str] = None
    phone: Optional[str] = None
    device: Optional[int] = None
    is_me: Optional[bool] = Field(None, alias="isMe")
