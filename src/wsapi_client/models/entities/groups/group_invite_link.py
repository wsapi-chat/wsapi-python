from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupInviteLink(BaseModel):
    invite_link: str = Field(alias="inviteLink")

    model_config = ConfigDict(populate_by_name=True)
