from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AccountInstance(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    created: Optional[str] = None
    name: Optional[str] = None
    use_custom_defaults: Optional[bool] = Field(None, alias="useCustomDefaults")
    status: Optional[str] = None
    device_id: Optional[str] = Field(None, alias="deviceId")
    expired_at: Optional[str] = Field(None, alias="expiredAt")
    trial_ends_at: Optional[str] = Field(None, alias="trialEndsAt")
    is_in_trial: Optional[bool] = Field(None, alias="isInTrial")
    has_api_key: Optional[bool] = Field(None, alias="hasApiKey")
