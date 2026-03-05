from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class MessageRequestBase(BaseModel):
    to: str = Field(alias="to")
    mentions: Optional[List[str]] = Field(default=None, alias="mentions")
    reply_to: Optional[str] = Field(default=None, alias="replyTo")
    reply_to_sender_id: Optional[str] = Field(default=None, alias="replyToSenderId")
    is_forwarded: Optional[bool] = Field(default=False, alias="isForwarded")
    ephemeral_expiration: Optional[Literal["24h", "7d", "90d"]] = Field(default=None, alias="ephemeralExpiration")

    model_config = ConfigDict(populate_by_name=True)
