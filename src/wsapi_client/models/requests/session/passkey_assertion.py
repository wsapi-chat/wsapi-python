from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PasskeyAuthenticatorResponse(BaseModel):
    """The ``response`` part of a WebAuthn assertion (binary fields base64url-encoded)."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_data_json: str = Field(alias="clientDataJSON")
    authenticator_data: Optional[str] = Field(default=None, alias="authenticatorData")
    signature: str = Field(alias="signature")
    user_handle: Optional[str] = Field(default=None, alias="userHandle")


class PasskeyAssertion(BaseModel):
    """WebAuthn assertion as produced by ``PublicKeyCredential.toJSON()`` in the browser.

    Build it from the browser JSON with ``PasskeyAssertion.model_validate(data)``.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    raw_id: str = Field(alias="rawId")
    type: Optional[str] = Field(default=None, alias="type")
    response: PasskeyAuthenticatorResponse = Field(alias="response")
