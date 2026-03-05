from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ...entities.groups.group_info import Identity


class CallOfferEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    caller: Optional[Identity] = None
    chat_id: str = Field(alias="chatId")
    time: datetime
    is_group: Optional[bool] = Field(default=None, alias="isGroup")
    is_video: Optional[bool] = Field(default=None, alias="isVideo")
