from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupSetMemberAddModeRequest(BaseModel):
    only_admin_add: bool = Field(alias="onlyAdminAdd")

    model_config = ConfigDict(populate_by_name=True)
