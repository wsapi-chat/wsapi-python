from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AccountSubscription(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    created: Optional[str] = None
    cur_period_start: Optional[str] = Field(None, alias="curPeriodStart")
    cur_period_end: Optional[str] = Field(None, alias="curPeriodEnd")
    quantity: Optional[int] = None
    plan: Optional[str] = None
    price: Optional[str] = None
    status: Optional[str] = None
    cancel_at_period_end: Optional[bool] = Field(None, alias="cancelAtPeriodEnd")
    instance_ids: Optional[list[str]] = Field(None, alias="instanceIds")
