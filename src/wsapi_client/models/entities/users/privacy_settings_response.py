from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PrivacySettingsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_add: Optional[str] = Field(None, alias="groupAdd")
    last_seen: Optional[str] = Field(None, alias="lastSeen")
    status: Optional[str] = None
    profile: Optional[str] = None
    read_receipts: Optional[str] = Field(None, alias="readReceipts")
    online: Optional[str] = None
    call_add: Optional[str] = Field(None, alias="callAdd")
