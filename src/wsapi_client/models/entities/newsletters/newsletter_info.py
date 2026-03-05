from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class NewsletterInfoResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    subscriber_count: Optional[int] = Field(None, alias="subscriberCount")
    verification_state: Optional[str] = Field(None, alias="verificationState")
    picture_url: Optional[str] = Field(None, alias="pictureUrl")
    invite_code: Optional[str] = Field(None, alias="inviteCode")
    role: Optional[str] = None
    mute: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = Field(None, alias="createdAt")
