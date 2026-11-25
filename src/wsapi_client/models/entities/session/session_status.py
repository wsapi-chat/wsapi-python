from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ...constants.passkey_statuses import PasskeyStatuses


class SessionStatus(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_connected: bool = Field(alias="isConnected")
    is_logged_in: bool = Field(alias="isLoggedIn")
    device_id: Optional[str] = Field(default=None, alias="deviceId")
    passkey_status: Optional[str] = Field(default=None, alias="passkeyStatus")
    """Passkey verification state (one of ``PasskeyStatuses``); same as ``PasskeyState.status``."""

    @property
    def is_passkey_pending(self) -> bool:
        """True while a passkey step is pending: stop polling the QR and pair-code endpoints."""
        return self.passkey_status in PasskeyStatuses.PENDING
