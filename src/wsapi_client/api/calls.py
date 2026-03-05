from __future__ import annotations

from ..http import ApiResponse, WSApiHttp
from ..models.requests.calls.reject_call_request import RejectCallRequest


class CallsClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    def reject(self, call_id: str, request: RejectCallRequest) -> None:
        self._http.send_json("POST", f"/calls/{call_id}/reject", model=None, json=request.model_dump(by_alias=True))
        return None

    def try_reject(self, call_id: str, request: RejectCallRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "POST", f"/calls/{call_id}/reject", model=None, json=request.model_dump(by_alias=True)
        )
