from __future__ import annotations

import builtins
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class StatusPrivacyResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    list: Optional[builtins.list[str]] = None
    is_default: Optional[bool] = Field(None, alias="isDefault")
