from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class MessageExtendedText(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    matched_text: Optional[str] = Field(alias="matchedText", default=None)
    description: Optional[str] = None
    title: Optional[str] = None
    jpeg_thumbnail: Optional[str] = Field(alias="jpegThumbnail", default=None)
