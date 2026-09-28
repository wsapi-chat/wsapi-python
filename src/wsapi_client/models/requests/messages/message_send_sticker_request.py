"""Legacy constructor names accepted; serialization uses the current REST fields."""

from typing import Optional

from pydantic import AliasChoices, Field

from . import SendStickerRequest


class MessageSendStickerRequest(SendStickerRequest):
    data: Optional[str] = Field(None, validation_alias=AliasChoices("data", "stickerBase64", "sticker_base64"))
    url: Optional[str] = Field(None, validation_alias=AliasChoices("url", "stickerURL", "stickerUrl", "sticker_url"))
