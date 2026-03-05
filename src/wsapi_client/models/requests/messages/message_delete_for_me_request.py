from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class MessageDeleteForMeRequest(BaseModel):
    chat_id: str = Field(alias="chatId")
    sender_id: str = Field(alias="senderId")
    is_from_me: bool = Field(alias="isFromMe")
    timestamp: datetime = Field(alias="timestamp")

    model_config = ConfigDict(populate_by_name=True)
