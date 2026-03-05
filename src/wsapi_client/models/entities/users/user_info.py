from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UserInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    lid: Optional[str] = None
    phone: Optional[str] = None
    device: Optional[int] = None
    is_in_whats_app: Optional[bool] = Field(None, alias="isInWhatsApp")
    status: Optional[str] = None
    picture_id: Optional[str] = Field(None, alias="pictureId")
    picture_url: Optional[str] = Field(None, alias="pictureUrl")
    is_verified: Optional[bool] = Field(None, alias="isVerified")
