"""Legacy constructor names accepted; serialization uses the current REST fields."""

from typing import Optional

from pydantic import AliasChoices, Field

from . import SendDocumentRequest


class MessageSendDocumentRequest(SendDocumentRequest):
    data: Optional[str] = Field(None, validation_alias=AliasChoices("data", "documentBase64", "document_base64"))
    url: Optional[str] = Field(None, validation_alias=AliasChoices("url", "documentURL", "documentUrl", "document_url"))
    filename: str = Field(..., validation_alias=AliasChoices("filename", "fileName", "file_name"))
