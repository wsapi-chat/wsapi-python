from __future__ import annotations

from typing import List

from pydantic import BaseModel, ConfigDict


class BulkCheckRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    phones: List[str]
