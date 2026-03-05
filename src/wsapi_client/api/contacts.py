from __future__ import annotations

from ..http import ApiResponse, WSApiHttp
from ..models.entities.contacts.contact_info import ContactInfo
from ..models.requests.contacts.contact_create_request import ContactCreateRequest


class ContactsClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def list(self) -> list[ContactInfo]:
        return self._http.send_json("GET", "/contacts", model=list[ContactInfo])

    def get(self, contact_id: str) -> ContactInfo:
        return self._http.send_json("GET", f"/contacts/{contact_id}", model=ContactInfo)

    def create(self, request: ContactCreateRequest) -> None:
        self._http.send_json("POST", "/contacts", model=None, json=request.model_dump(by_alias=True))

    def sync(self) -> None:
        self._http.send_json("POST", "/contacts/sync", model=None)

    def get_blocklist(self) -> list[str]:
        return self._http.send_json("GET", "/contacts/blocklist", model=list[str])

    def block(self, contact_id: str) -> None:
        self._http.send_json("POST", f"/contacts/{contact_id}/block", model=None)

    def unblock(self, contact_id: str) -> None:
        self._http.send_json("POST", f"/contacts/{contact_id}/unblock", model=None)

    # Try methods
    def try_list(self) -> ApiResponse[list[ContactInfo]]:
        return self._http.try_send_json("GET", "/contacts", model=list[ContactInfo])

    def try_get(self, contact_id: str) -> ApiResponse[ContactInfo]:
        return self._http.try_send_json("GET", f"/contacts/{contact_id}", model=ContactInfo)

    def try_create(self, request: ContactCreateRequest) -> ApiResponse[None]:
        return self._http.try_send_json("POST", "/contacts", model=None, json=request.model_dump(by_alias=True))

    def try_sync(self) -> ApiResponse[None]:
        return self._http.try_send_json("POST", "/contacts/sync", model=None)

    def try_get_blocklist(self) -> ApiResponse[list[str]]:
        return self._http.try_send_json("GET", "/contacts/blocklist", model=list[str])

    def try_block(self, contact_id: str) -> ApiResponse[None]:
        return self._http.try_send_json("POST", f"/contacts/{contact_id}/block", model=None)

    def try_unblock(self, contact_id: str) -> ApiResponse[None]:
        return self._http.try_send_json("POST", f"/contacts/{contact_id}/unblock", model=None)
