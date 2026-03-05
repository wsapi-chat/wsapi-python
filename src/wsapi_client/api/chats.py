from __future__ import annotations

from ..http import ApiResponse, WSApiHttp
from ..models.entities.chats.chat_business_profile import ChatBusinessProfile
from ..models.entities.chats.chat_info import ChatListItem
from ..models.entities.chats.chat_picture import ChatPicture
from ..models.requests.chats.chat_update_archive_request import ChatUpdateArchiveRequest
from ..models.requests.chats.chat_update_ephemeral_expiration_request import ChatUpdateEphemeralExpirationRequest
from ..models.requests.chats.chat_update_mute_request import ChatUpdateMuteRequest
from ..models.requests.chats.chat_update_pin_request import ChatUpdatePinRequest
from ..models.requests.chats.chat_update_presence_request import ChatUpdatePresenceRequest
from ..models.requests.chats.chat_update_read_request import ChatUpdateReadRequest
from ..models.requests.chats.request_messages_request import RequestMessagesRequest


class ChatsClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def list(self) -> list[ChatListItem]:
        return self._http.send_json("GET", "/chats", model=list[ChatListItem])

    def get(self, chat_id: str) -> ChatListItem:
        return self._http.send_json("GET", f"/chats/{chat_id}", model=ChatListItem)

    def get_picture(self, chat_id: str) -> ChatPicture:
        return self._http.send_json("GET", f"/chats/{chat_id}/picture", model=ChatPicture)

    def get_business_profile(self, chat_id: str) -> ChatBusinessProfile:
        return self._http.send_json("GET", f"/chats/{chat_id}/business", model=ChatBusinessProfile)

    def subscribe_presence(self, chat_id: str) -> None:
        self._http.send_json("PUT", f"/chats/{chat_id}/presence/subscribe", model=None)

    def update_presence(self, chat_id: str, request: ChatUpdatePresenceRequest) -> None:
        self._http.send_json("PUT", f"/chats/{chat_id}/presence", model=None, json=request.model_dump(by_alias=True))

    def update_ephemeral(self, chat_id: str, request: ChatUpdateEphemeralExpirationRequest) -> None:
        self._http.send_json("PUT", f"/chats/{chat_id}/ephemeral", model=None, json=request.model_dump(by_alias=True))

    def update_mute(self, chat_id: str, request: ChatUpdateMuteRequest) -> None:
        self._http.send_json("PUT", f"/chats/{chat_id}/mute", model=None, json=request.model_dump(by_alias=True))

    def update_pin(self, chat_id: str, request: ChatUpdatePinRequest) -> None:
        self._http.send_json("PUT", f"/chats/{chat_id}/pin", model=None, json=request.model_dump(by_alias=True))

    def update_archive(self, chat_id: str, request: ChatUpdateArchiveRequest) -> None:
        self._http.send_json("PUT", f"/chats/{chat_id}/archive", model=None, json=request.model_dump(by_alias=True))

    def update_read(self, chat_id: str, request: ChatUpdateReadRequest) -> None:
        self._http.send_json("PUT", f"/chats/{chat_id}/read", model=None, json=request.model_dump(by_alias=True))

    def delete_chat(self, chat_id: str) -> None:
        self._http.send_json("DELETE", f"/chats/{chat_id}", model=None)

    def clear(self, chat_id: str) -> None:
        self._http.send_json("PUT", f"/chats/{chat_id}/clear", model=None)

    def request_messages(self, chat_id: str, request: RequestMessagesRequest) -> None:
        self._http.send_json("POST", f"/chats/{chat_id}/messages", model=None, json=request.model_dump(by_alias=True))

    # Try methods
    def try_list(self) -> ApiResponse[list[ChatListItem]]:
        return self._http.try_send_json("GET", "/chats", model=list[ChatListItem])

    def try_get(self, chat_id: str) -> ApiResponse[ChatListItem]:
        return self._http.try_send_json("GET", f"/chats/{chat_id}", model=ChatListItem)

    def try_get_picture(self, chat_id: str) -> ApiResponse[ChatPicture]:
        return self._http.try_send_json("GET", f"/chats/{chat_id}/picture", model=ChatPicture)

    def try_get_business_profile(self, chat_id: str) -> ApiResponse[ChatBusinessProfile]:
        return self._http.try_send_json("GET", f"/chats/{chat_id}/business", model=ChatBusinessProfile)

    def try_subscribe_presence(self, chat_id: str) -> ApiResponse[None]:
        return self._http.try_send_json("PUT", f"/chats/{chat_id}/presence/subscribe", model=None)

    def try_update_presence(self, chat_id: str, request: ChatUpdatePresenceRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/chats/{chat_id}/presence", model=None, json=request.model_dump(by_alias=True)
        )

    def try_update_ephemeral(self, chat_id: str, request: ChatUpdateEphemeralExpirationRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/chats/{chat_id}/ephemeral", model=None, json=request.model_dump(by_alias=True)
        )

    def try_update_mute(self, chat_id: str, request: ChatUpdateMuteRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/chats/{chat_id}/mute", model=None, json=request.model_dump(by_alias=True)
        )

    def try_update_pin(self, chat_id: str, request: ChatUpdatePinRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/chats/{chat_id}/pin", model=None, json=request.model_dump(by_alias=True)
        )

    def try_update_archive(self, chat_id: str, request: ChatUpdateArchiveRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/chats/{chat_id}/archive", model=None, json=request.model_dump(by_alias=True)
        )

    def try_update_read(self, chat_id: str, request: ChatUpdateReadRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "PUT", f"/chats/{chat_id}/read", model=None, json=request.model_dump(by_alias=True)
        )

    def try_delete_chat(self, chat_id: str) -> ApiResponse[None]:
        return self._http.try_send_json("DELETE", f"/chats/{chat_id}", model=None)

    def try_clear(self, chat_id: str) -> ApiResponse[None]:
        return self._http.try_send_json("PUT", f"/chats/{chat_id}/clear", model=None)

    def try_request_messages(self, chat_id: str, request: RequestMessagesRequest) -> ApiResponse[None]:
        return self._http.try_send_json(
            "POST", f"/chats/{chat_id}/messages", model=None, json=request.model_dump(by_alias=True)
        )
