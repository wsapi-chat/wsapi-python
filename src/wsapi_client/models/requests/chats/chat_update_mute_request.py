from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class ChatUpdateMuteRequest(BaseModel):
    """Request to mute/unmute a chat. Set duration to 'off' to unmute."""

    model_config = ConfigDict(populate_by_name=True)

    duration: Optional[Literal["8h", "1w", "always", "off"]] = Field(default=None, alias="duration")
