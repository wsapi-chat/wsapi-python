from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ...entities.chats.chat_archive import ChatArchive
from ...entities.chats.chat_ephemeral import ChatEphemeral
from ...entities.chats.chat_mute import ChatMute
from ...entities.chats.chat_pin import ChatPin
from ...entities.chats.chat_read import ChatRead


class ChatSettingEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    setting_type: str = Field(alias="settingType")
    archive: Optional[ChatArchive] = None
    pin: Optional[ChatPin] = None
    read: Optional[ChatRead] = None
    mute: Optional[ChatMute] = None
    ephemeral: Optional[ChatEphemeral] = None
