from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class MessageContact(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str = Field(alias="displayName")
    v_card: str = Field(alias="vCard")
