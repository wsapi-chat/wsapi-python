from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GroupInviteLink(BaseModel):
    invite_link: str = Field(alias="link")

    model_config = ConfigDict(populate_by_name=True)

    @property
    def link(self) -> str:
        return self.invite_link
