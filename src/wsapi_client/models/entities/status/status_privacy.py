from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class StatusPrivacyResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    list: Optional[List[str]] = None
    is_default: Optional[bool] = Field(None, alias="isDefault")
