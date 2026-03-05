from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AccountSubscriptionChange(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    timestamp: Optional[str] = None
    subscription_id: Optional[str] = Field(None, alias="subscriptionId")
    change_type: Optional[str] = Field(None, alias="changeType")
    previous_quantity: Optional[int] = Field(None, alias="previousQuantity")
    new_quantity: Optional[int] = Field(None, alias="newQuantity")
    instance_id: Optional[str] = Field(None, alias="instanceId")
    prorated_amount: Optional[float] = Field(None, alias="proratedAmount")
    notes: Optional[str] = None
