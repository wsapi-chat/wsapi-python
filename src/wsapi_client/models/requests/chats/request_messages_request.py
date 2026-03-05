from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class RequestMessagesRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    last_message_id: str = Field(alias="lastMessageId")
    last_message_sender_id: str = Field(alias="lastMessageSenderId")
    count: Optional[int] = None
