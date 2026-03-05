from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .message_event import MessageEvent


class MessageHistorySyncEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    chat_id: Optional[str] = Field(None, alias="chatId")
    messages: list[MessageEvent]
