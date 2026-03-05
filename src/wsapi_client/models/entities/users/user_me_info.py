from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UserMeInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    lid: Optional[str] = None
    phone: Optional[str] = None
    device_id: Optional[int] = Field(None, alias="deviceId")
    push_name: Optional[str] = Field(None, alias="pushName")
    business_name: Optional[str] = Field(None, alias="businessName")
    status: Optional[str] = None
    picture_id: Optional[str] = Field(None, alias="pictureId")
    is_verified: Optional[bool] = Field(None, alias="isVerified")
