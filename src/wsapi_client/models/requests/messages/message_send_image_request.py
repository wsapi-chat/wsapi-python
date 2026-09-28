"""Legacy constructor names accepted; serialization uses the current REST fields."""

from typing import Optional

from pydantic import AliasChoices, Field

from . import SendMediaRequest


class MessageSendImageRequest(SendMediaRequest):
    data: Optional[str] = Field(None, validation_alias=AliasChoices("data", "imageBase64", "image_base64"))
    url: Optional[str] = Field(None, validation_alias=AliasChoices("url", "imageURL", "imageUrl", "image_url"))
