from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class AccountInstanceSettings(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    use_custom_defaults: Optional[bool] = Field(None, alias="useCustomDefaults")
    pull_mode: Optional[bool] = Field(None, alias="pullMode")
    webhook_url: Optional[str] = Field(None, alias="webhookUrl")
    event_signing_secret: Optional[str] = Field(None, alias="eventSigningSecret")
    history_sync: Optional[bool] = Field(None, alias="historySync")
    event_filters: Optional[List[str]] = Field(None, alias="eventFilters")
