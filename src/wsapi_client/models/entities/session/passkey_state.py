from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from ...constants.passkey_statuses import PasskeyStatuses


class PasskeyAllowCredential(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: Optional[str] = Field(default=None, alias="id")
    type: Optional[str] = Field(default=None, alias="type")
    transports: Optional[List[str]] = Field(default=None, alias="transports")


class PasskeyChallenge(BaseModel):
    """WebAuthn ``PublicKeyCredentialRequestOptionsJSON`` (binary fields base64url-encoded).

    Pass ``model_dump(by_alias=True, exclude_none=True)`` to
    ``PublicKeyCredential.parseRequestOptionsFromJSON()`` in a browser on ``PasskeyState.origin``.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    challenge: Optional[str] = Field(default=None, alias="challenge")
    timeout: Optional[int] = Field(default=None, alias="timeout")
    rp_id: Optional[str] = Field(default=None, alias="rpId")
    allow_credentials: Optional[List[PasskeyAllowCredential]] = Field(default=None, alias="allowCredentials")
    user_verification: Optional[str] = Field(default=None, alias="userVerification")
    extensions: Optional[Dict[str, Any]] = Field(default=None, alias="extensions")


class PasskeyState(BaseModel):
    """State of the passkey (WebAuthn) verification step of device pairing.

    ``status`` is one of the values in ``PasskeyStatuses``.
    """

    model_config = ConfigDict(populate_by_name=True)

    status: str = Field(alias="status")
    source: Optional[str] = Field(default=None, alias="source")
    challenge: Optional[PasskeyChallenge] = Field(default=None, alias="challenge")
    origin: Optional[str] = Field(default=None, alias="origin")
    confirmation_code: Optional[str] = Field(default=None, alias="confirmationCode")
    confirmation_sent: Optional[bool] = Field(default=None, alias="confirmationSent")
    error: Optional[str] = Field(default=None, alias="error")
    requested_at: Optional[datetime] = Field(default=None, alias="requestedAt")
    expires_at: Optional[datetime] = Field(default=None, alias="expiresAt")

    @property
    def is_pending(self) -> bool:
        """True while a step is in progress; QR and pair-code endpoints return 409 meanwhile."""
        return self.status in PasskeyStatuses.PENDING
