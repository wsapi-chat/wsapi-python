from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class SetPrivacyRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    setting: str
    value: str
