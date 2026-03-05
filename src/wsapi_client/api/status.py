from __future__ import annotations

from ..http import ApiResponse, WSApiHttp
from ..models.entities.messages.message_created import MessageCreated
from ..models.entities.status.status_privacy import StatusPrivacyResponse
from ..models.requests.status.status_requests import PostMediaStatusRequest, PostTextStatusRequest


class StatusClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def get_privacy(self) -> list[StatusPrivacyResponse]:
        return self._http.send_json("GET", "/status/privacy", model=list[StatusPrivacyResponse])

    def post_text(self, request: PostTextStatusRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", "/status/text", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def post_image(self, request: PostMediaStatusRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", "/status/image", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def post_video(self, request: PostMediaStatusRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", "/status/video", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def delete(self, status_id: str) -> None:
        self._http.send_json("POST", f"/status/{status_id}/delete", model=None)

    # Try variants
    def try_get_privacy(self) -> ApiResponse[list[StatusPrivacyResponse]]:
        return self._http.try_send_json("GET", "/status/privacy", model=list[StatusPrivacyResponse])

    def try_post_text(self, request: PostTextStatusRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "/status/text", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def try_post_image(self, request: PostMediaStatusRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "/status/image", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def try_post_video(self, request: PostMediaStatusRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "/status/video", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def try_delete(self, status_id: str) -> ApiResponse[None]:
        return self._http.try_send_json("POST", f"/status/{status_id}/delete", model=None)
