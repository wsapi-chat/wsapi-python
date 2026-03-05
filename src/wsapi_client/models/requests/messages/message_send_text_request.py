from __future__ import annotations

from pydantic import ConfigDict, Field

from .message_request_base import MessageRequestBase


class MessageSendTextRequest(MessageRequestBase):
    text: str = Field(alias="text")

    model_config = ConfigDict(populate_by_name=True)
