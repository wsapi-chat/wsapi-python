"""Legacy constructor names accepted; serialization uses the current REST fields."""

from typing import Optional

from pydantic import AliasChoices, Field

from . import SendMediaRequest


class MessageSendAudioRequest(SendMediaRequest):
    data: Optional[str] = Field(None, validation_alias=AliasChoices("data", "audioBase64", "audio_base64"))
    url: Optional[str] = Field(None, validation_alias=AliasChoices("url", "audioURL", "audioUrl", "audio_url"))
