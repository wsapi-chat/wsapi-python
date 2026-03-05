from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict


class CreateNewsletterRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str
    description: Optional[str] = None
    picture: Optional[str] = None


class SetSubscriptionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    subscribed: bool


class ToggleMuteNewsletterRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    mute: Optional[bool] = None
