from __future__ import annotations

from ..http import ApiResponse, WSApiHttp
from ..models.entities.session.session_pair_code import SessionPairCode
from ..models.entities.session.session_qr_code import SessionQRCode
from ..models.entities.session.session_status import SessionStatus


class SessionClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def get_qr_image(self) -> bytes:
        return self._http.send_bytes("GET", "/session/qr")

    def get_qr_code(self) -> SessionQRCode:
        return self._http.send_json("GET", "/session/qr/text", model=SessionQRCode)

    def get_pair_code(self, phone_number: str) -> SessionPairCode:
        return self._http.send_json("GET", f"/session/pair-code/{phone_number}", model=SessionPairCode)

    def logout(self) -> None:
        self._http.send_json("POST", "/session/logout", model=None)

    def get_session_status(self) -> SessionStatus:
        return self._http.send_json("GET", "/session/status", model=SessionStatus)

    def flush_history(self) -> None:
        self._http.send_json("POST", "/session/flush-history", model=None)

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

    def try_flush_history(self) -> ApiResponse[None]:
        return self._http.try_send_json("POST", "/session/flush-history", model=None)
