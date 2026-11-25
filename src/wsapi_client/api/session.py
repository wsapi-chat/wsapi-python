from __future__ import annotations

from typing import Any, Dict, Union

from pydantic import ValidationError

from ..http import ApiResponse, WSApiHttp
from ..models.entities.session.passkey_state import PasskeyState
from ..models.entities.session.session_pair_code import SessionPairCode
from ..models.entities.session.session_qr_code import SessionQRCode
from ..models.entities.session.session_status import SessionStatus
from ..models.problem_details import ProblemDetails
from ..models.requests.session.passkey_assertion import PasskeyAssertion

PasskeyAssertionInput = Union[PasskeyAssertion, Dict[str, Any]]


def _assertion_body(assertion: PasskeyAssertionInput) -> Dict[str, Any]:
    # Accept the raw ``PublicKeyCredential.toJSON()`` dict as well as the model.
    model = assertion if isinstance(assertion, PasskeyAssertion) else PasskeyAssertion.model_validate(assertion)
    return model.model_dump(by_alias=True, exclude_none=True)


class SessionClient:
    """Pairing and session management.

    ``get_qr_image``, ``get_qr_code`` and ``get_pair_code`` fail with HTTP 409 while a passkey
    verification step is pending (``SessionStatus.is_passkey_pending``). Stop polling them and
    complete the step with ``get_passkey_state`` / ``submit_passkey`` instead.
    """

    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def get_qr_image(self) -> bytes:
        """PNG of the pairing QR code. Raises ``ApiException`` (409) while a passkey step is pending."""
        return self._http.send_bytes("GET", "/session/qr")

    def get_qr_code(self) -> SessionQRCode:
        """Raw pairing QR string. Raises ``ApiException`` (409) while a passkey step is pending."""
        return self._http.send_json("GET", "/session/qr/text", model=SessionQRCode)

    def get_pair_code(self, phone_number: str) -> SessionPairCode:
        """Pair code for a phone number. Raises ``ApiException`` (409) while a passkey step is pending."""
        return self._http.send_json("GET", f"/session/pair-code/{phone_number}", model=SessionPairCode)

    def logout(self) -> None:
        self._http.send_json("POST", "/session/logout", model=None)

    def get_session_status(self) -> SessionStatus:
        return self._http.send_json("GET", "/session/status", model=SessionStatus)

    def flush_history(self) -> dict[str, str]:
        return self._http.send_json("POST", "/session/flush-history", model=dict[str, str])

    def get_passkey_state(self) -> PasskeyState:
        """State of the passkey verification step; includes the WebAuthn challenge while ``required``."""
        return self._http.send_json("GET", "/session/passkey", model=PasskeyState)

    def submit_passkey(self, assertion: PasskeyAssertionInput) -> PasskeyState:
        """Forward the browser's ``PublicKeyCredential.toJSON()`` assertion to WhatsApp.

        Accepts a ``PasskeyAssertion`` or the raw dict. Errors: 400 (malformed or mismatched
        assertion; the step stays ``required``), 409 (no step pending), 413 (body too large),
        502 (WhatsApp rejected it).
        """
        return self._http.send_json("POST", "/session/passkey", model=PasskeyState, json=_assertion_body(assertion))

    def request_passkey(self) -> PasskeyState:
        """Ask WhatsApp for a passkey challenge (idempotent while one is pending).

        Errors: 400 (already paired), 409 (could not connect), 502 (no challenge returned).
        """
        return self._http.send_json("POST", "/session/passkey/request", model=PasskeyState)

    def confirm_passkey(self) -> None:
        """Compatibility only: the server now sends the confirmation automatically.

        Not needed in normal use. A no-op if the confirmation was already sent; 409 if no step
        is in ``confirmation_required``.
        """
        self._http.send_json("POST", "/session/passkey/confirm", model=None)

    # Try methods
    def try_get_qr_image(self) -> ApiResponse[bytes]:
        return self._http.try_send_bytes("GET", "/session/qr")

    def try_get_qr_code(self) -> ApiResponse[SessionQRCode]:
        return self._http.try_send_json("GET", "/session/qr/text", model=SessionQRCode)

    def try_get_pair_code(self, phone_number: str) -> ApiResponse[SessionPairCode]:
        return self._http.try_send_json("GET", f"/session/pair-code/{phone_number}", model=SessionPairCode)

    def try_logout(self) -> ApiResponse[None]:
        return self._http.try_send_json("POST", "/session/logout", model=None)

    def try_get_session_status(self) -> ApiResponse[SessionStatus]:
        return self._http.try_send_json("GET", "/session/status", model=SessionStatus)

    def try_flush_history(self) -> ApiResponse[dict[str, str]]:
        return self._http.try_send_json("POST", "/session/flush-history", model=dict[str, str])

    def try_get_passkey_state(self) -> ApiResponse[PasskeyState]:
        return self._http.try_send_json("GET", "/session/passkey", model=PasskeyState)

    def try_submit_passkey(self, assertion: PasskeyAssertionInput) -> ApiResponse[PasskeyState]:
        try:
            body = _assertion_body(assertion)
        except ValidationError as exc:
            return ApiResponse(error=ProblemDetails(status=400, title="Invalid Request", detail=str(exc)))
        return self._http.try_send_json("POST", "/session/passkey", model=PasskeyState, json=body)

    def try_request_passkey(self) -> ApiResponse[PasskeyState]:
        return self._http.try_send_json("POST", "/session/passkey/request", model=PasskeyState)

    def try_confirm_passkey(self) -> ApiResponse[None]:
        """Compatibility only; see ``confirm_passkey``."""
        return self._http.try_send_json("POST", "/session/passkey/confirm", model=None)
