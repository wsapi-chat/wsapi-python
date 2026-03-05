from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PostTextStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    text: str


class PostMediaStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    data: Optional[str] = None
    url: Optional[str] = None
    mime_type: Optional[str] = Field(None, alias="mimeType")
    caption: Optional[str] = None
