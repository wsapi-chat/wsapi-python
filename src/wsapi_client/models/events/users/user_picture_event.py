from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from ...entities.users.sender import Sender


class UserPictureEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    sender: Sender
    picture_id: str = Field(alias="pictureId")
