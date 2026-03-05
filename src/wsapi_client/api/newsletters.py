from __future__ import annotations

from ..http import ApiResponse, WSApiHttp
from ..models.entities.messages.message_created import MessageCreated
from ..models.entities.newsletters.newsletter_info import NewsletterInfoResponse


class NewslettersClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def list(self) -> list[NewsletterInfoResponse]:
        return self._http.send_json("GET", "/newsletters", model=list[NewsletterInfoResponse])

    def create(self, request) -> MessageCreated:
        return self._http.send_json(
            "POST", "/newsletters", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def get_by_invite_code(self, code: str) -> NewsletterInfoResponse:
        return self._http.send_json("GET", f"/newsletters/invite/{code}", model=NewsletterInfoResponse)

    def get(self, newsletter_id: str) -> NewsletterInfoResponse:
        return self._http.send_json("GET", f"/newsletters/{newsletter_id}", model=NewsletterInfoResponse)

    def set_subscription(self, newsletter_id: str, request) -> None:
        self._http.send_json(
            "POST", f"/newsletters/{newsletter_id}/subscription", model=None, json=request.model_dump(by_alias=True)
        )

    def toggle_mute(self, newsletter_id: str, request) -> None:
        self._http.send_json(
            "PUT", f"/newsletters/{newsletter_id}/mute", model=None, json=request.model_dump(by_alias=True)
        )

    # Try variants
    def try_list(self) -> ApiResponse[list[NewsletterInfoResponse]]:
        return self._http.try_send_json("GET", "/newsletters", model=list[NewsletterInfoResponse])

    def try_create(self, request) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "/newsletters", model=MessageCreated, json=request.model_dump(by_alias=True)
        )

    def try_get_by_invite_code(self, code: str) -> ApiResponse[NewsletterInfoResponse]:
        return self._http.try_send_json("GET", f"/newsletters/invite/{code}", model=NewsletterInfoResponse)

    def try_get(self, newsletter_id: str) -> ApiResponse[NewsletterInfoResponse]:
        return self._http.try_send_json("GET", f"/newsletters/{newsletter_id}", model=NewsletterInfoResponse)

    def try_set_subscription(self, newsletter_id: str, request) -> ApiResponse[None]:
        return self._http.try_send_json(
            "POST", f"/newsletters/{newsletter_id}/subscription", model=None, json=request.model_dump(by_alias=True)
        )

    def try_toggle_mute(self, newsletter_id: str, request) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/newsletters/{newsletter_id}/mute", model=None, json=request.model_dump(by_alias=True)
        )
