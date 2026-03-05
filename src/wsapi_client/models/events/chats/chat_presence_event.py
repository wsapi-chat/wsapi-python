from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from ...entities.users.sender import Sender


class ChatPresenceEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    sender: Sender
    state: str
