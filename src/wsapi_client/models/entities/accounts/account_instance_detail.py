from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .account_instance_settings import AccountInstanceSettings


class AccountInstanceDetail(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = None
    has_api_key: Optional[bool] = Field(None, alias="hasApiKey")
    settings: Optional[AccountInstanceSettings] = None
    status: Optional[str] = None
    device_id: Optional[str] = Field(None, alias="deviceId")
    created: Optional[str] = None
