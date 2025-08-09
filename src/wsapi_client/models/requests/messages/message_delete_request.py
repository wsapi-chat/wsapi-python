from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict


class MessageDeleteRequest(BaseModel):
    chat_id: str = Field(alias="chatId")
    sender_id: str = Field(alias="senderId")

    model_config = ConfigDict(populate_by_name=True)
