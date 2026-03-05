from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict


class UpdateProfileRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = None
    status: Optional[str] = None
    picture: Optional[str] = None
