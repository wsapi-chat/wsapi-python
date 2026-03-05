from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ChatMute(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_muted: bool = Field(alias="isMuted")
    muted_end_time: Optional[datetime] = Field(alias="mutedEndTime", default=None)
