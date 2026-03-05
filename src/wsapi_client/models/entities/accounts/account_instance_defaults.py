from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class AccountInstanceDefaults(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    default_webhook_url: Optional[str] = Field(None, alias="defaultWebhookUrl")
    default_signing_secret: Optional[str] = Field(None, alias="defaultSigningSecret")
    default_event_filters: Optional[List[str]] = Field(None, alias="defaultEventFilters")
    default_history_sync: Optional[bool] = Field(None, alias="defaultHistorySync")
    default_pull_mode: Optional[bool] = Field(None, alias="defaultPullMode")
