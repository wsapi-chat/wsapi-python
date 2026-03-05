from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class UpdateInstanceNameRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str
