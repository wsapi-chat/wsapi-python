from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class MessageRequestBase(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    to: str
    mentions: Optional[list[str]] = None
    reply_to: Optional[str] = Field(None, alias="replyTo")
    reply_to_sender_id: Optional[str] = Field(None, alias="replyToSenderId")
    is_forwarded: Optional[bool] = Field(None, alias="isForwarded")
    ephemeral_expiration: Optional[str] = Field(None, alias="ephemeralExpiration")


class MessageSendTextRequest(MessageRequestBase):
    text: str


class SendMediaRequest(MessageRequestBase):
    data: Optional[str] = None
    url: Optional[str] = None
    mime_type: Optional[str] = Field(None, alias="mimeType")
    caption: Optional[str] = None
    view_once: Optional[bool] = Field(None, alias="viewOnce")


class SendDocumentRequest(SendMediaRequest):
    filename: str


class SendStickerRequest(MessageRequestBase):
    data: Optional[str] = None
    url: Optional[str] = None
    is_animated: Optional[bool] = Field(None, alias="isAnimated")


class SendContactRequest(MessageRequestBase):
    display_name: Optional[str] = Field(None, alias="displayName")
    vcard: Optional[str] = None


class SendLocationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    to: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    name: Optional[str] = None
    address: Optional[str] = None
    url: Optional[str] = None
    ephemeral_expiration: Optional[str] = Field(None, alias="ephemeralExpiration")


class SendLinkRequest(MessageRequestBase):
    text: str
    url: str
    title: Optional[str] = None
    description: Optional[str] = None
    jpeg_thumbnail: Optional[str] = Field(None, alias="jpegThumbnail")


class SendReactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    to: str
    sender_id: Optional[str] = Field(None, alias="senderId")
    reaction: str


class EditMessageRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    to: str
    text: str
    mentions: Optional[list[str]] = None
    ephemeral_expiration: Optional[str] = Field(None, alias="ephemeralExpiration")


class MarkAsReadRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    chat_id: str = Field(alias="chatId")
    sender_id: str = Field(alias="senderId")
    receipt_type: Literal["delivered", "sender", "read", "played"] = Field(alias="receiptType")


class StarMessageRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    chat_id: str = Field(alias="chatId")
    sender_id: str = Field(alias="senderId")
    starred: Optional[bool] = None


class PinMessageRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    chat_id: str = Field(alias="chatId")
    sender_id: str = Field(alias="senderId")
    pinned: Optional[bool] = None
    pin_expiration: Optional[str] = Field(None, alias="pinExpiration")


class DeleteMessageRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    chat_id: str = Field(alias="chatId")
    sender_id: str = Field(alias="senderId")


class DeleteMessageForMeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    chat_id: str = Field(alias="chatId")
    sender_id: Optional[str] = Field(None, alias="senderId")
    is_from_me: Optional[bool] = Field(None, alias="isFromMe")
    timestamp: Optional[str] = None


__all__ = [
    "DeleteMessageForMeRequest",
    "DeleteMessageRequest",
    "EditMessageRequest",
    "MarkAsReadRequest",
    "MessageRequestBase",
    "MessageSendTextRequest",
    "PinMessageRequest",
    "SendContactRequest",
    "SendDocumentRequest",
    "SendLinkRequest",
    "SendLocationRequest",
    "SendMediaRequest",
    "SendReactionRequest",
    "SendStickerRequest",
    "StarMessageRequest",
]
