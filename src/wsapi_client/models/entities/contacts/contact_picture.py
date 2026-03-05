from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ContactPicture(BaseModel):
    id: str = Field(alias="id")
    url: str = Field(alias="url")

    model_config = ConfigDict(populate_by_name=True)
