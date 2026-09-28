"""Legacy constructor names accepted; serialization uses the current REST fields."""

from typing import Optional

from pydantic import AliasChoices, Field

from . import SendContactRequest


class MessageSendContactRequest(SendContactRequest):
    vcard: Optional[str] = Field(None, validation_alias=AliasChoices("vcard", "vCard", "v_card"))
