from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupUpdatePictureRequest(BaseModel):
    data: str = Field(alias="data")

    model_config = ConfigDict(populate_by_name=True)
