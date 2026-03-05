from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict


class NewsletterEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    action: Optional[str] = None
    name: Optional[str] = None
    role: Optional[str] = None
    mute: Optional[str] = None
