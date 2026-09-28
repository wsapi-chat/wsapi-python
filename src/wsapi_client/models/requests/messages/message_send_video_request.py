"""Legacy constructor names accepted; serialization uses the current REST fields."""

from typing import Optional

from pydantic import AliasChoices, Field

from . import SendMediaRequest


class MessageSendVideoRequest(SendMediaRequest):
    data: Optional[str] = Field(None, validation_alias=AliasChoices("data", "videoBase64", "video_base64"))
    url: Optional[str] = Field(None, validation_alias=AliasChoices("url", "videoURL", "videoUrl", "video_url"))
