from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..users.sender import Sender


class MessageReplyTo(BaseModel):
    text: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)

    id: str
    sender: Sender
    is_forwarded: bool = Field(alias="isForwarded")
