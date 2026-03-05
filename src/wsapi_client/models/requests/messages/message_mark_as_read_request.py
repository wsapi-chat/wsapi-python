from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class MessageMarkAsReadRequest(BaseModel):
    chat_id: str = Field(alias="chatId")
    sender_id: str = Field(alias="senderId")
    receipt_type: Literal["delivered", "sender", "read", "played"] = Field(alias="receiptType")

    model_config = ConfigDict(populate_by_name=True)
