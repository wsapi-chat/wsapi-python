from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from ...entities.groups.group_info import Identity


class ChatStatusEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user: Optional[Identity] = None
    status: Optional[str] = None
