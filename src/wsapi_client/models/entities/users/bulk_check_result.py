from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class BulkCheckResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    query: Optional[str] = None
    is_in_whats_app: Optional[bool] = Field(None, alias="isInWhatsApp")
    jid: Optional[str] = None
