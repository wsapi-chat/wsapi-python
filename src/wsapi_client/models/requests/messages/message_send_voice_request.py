"""Legacy constructor names accepted; serialization uses the current REST fields."""

from typing import Optional

from pydantic import AliasChoices, Field

from . import SendMediaRequest


class MessageSendVoiceRequest(SendMediaRequest):
    data: Optional[str] = Field(None, validation_alias=AliasChoices("data", "voiceBase64", "voice_base64"))
    url: Optional[str] = Field(None, validation_alias=AliasChoices("url", "voiceURL", "voiceUrl", "voice_url"))
