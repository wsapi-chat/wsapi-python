from __future__ import annotations

from ..http import ApiResponse, WSApiHttp
from ..models.entities.users.bulk_check_result import BulkCheckResult
from ..models.entities.users.privacy_settings_response import PrivacySettingsResponse
from ..models.entities.users.user_info import UserInfo
from ..models.entities.users.user_me_info import UserMeInfo
from ..models.requests.users.bulk_check_request import BulkCheckRequest
from ..models.requests.users.set_presence_request import SetMyPresenceRequest
from ..models.requests.users.set_privacy_request import SetPrivacyRequest
from ..models.requests.users.update_profile_request import UpdateProfileRequest


class UsersClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def get_profile(self) -> UserMeInfo:
        return self._http.send_json("GET", "/users/profile", model=UserMeInfo)

    def update_profile(self, request: UpdateProfileRequest) -> None:
        self._http.send_json("PUT", "/users/profile", model=None, json=request.model_dump(by_alias=True))

    def set_presence(self, request: SetMyPresenceRequest) -> None:
        self._http.send_json("PUT", "/users/presence", model=None, json=request.model_dump(by_alias=True))

    def get_privacy_settings(self) -> PrivacySettingsResponse:
        return self._http.send_json("GET", "/users/privacy", model=PrivacySettingsResponse)

    def set_privacy_setting(self, request: SetPrivacyRequest) -> None:
        self._http.send_json("PUT", "/users/privacy", model=None, json=request.model_dump(by_alias=True))

    def bulk_check(self, request: BulkCheckRequest) -> list[BulkCheckResult]:
        return self._http.send_json(
            "POST", "/users/check", model=list[BulkCheckResult], json=request.model_dump(by_alias=True)
        )

    def check(self, user_id: str) -> UserInfo:
        return self._http.send_json("GET", f"/users/{user_id}/check", model=UserInfo)

    def get_user_profile(self, user_id: str) -> UserInfo:
        return self._http.send_json("GET", f"/users/{user_id}/profile", model=UserInfo)

    # Try methods
    def try_get_profile(self) -> ApiResponse[UserMeInfo]:
        return self._http.try_send_json("GET", "/users/profile", model=UserMeInfo)

    def try_update_profile(self, request: UpdateProfileRequest) -> ApiResponse[None]:
        return self._http.try_send_json("PUT", "/users/profile", model=None, json=request.model_dump(by_alias=True))

    def try_set_presence(self, request: SetMyPresenceRequest) -> ApiResponse[None]:
        return self._http.try_send_json("PUT", "/users/presence", model=None, json=request.model_dump(by_alias=True))

    def try_get_privacy_settings(self) -> ApiResponse[PrivacySettingsResponse]:
        return self._http.try_send_json("GET", "/users/privacy", model=PrivacySettingsResponse)

    def try_set_privacy_setting(self, request: SetPrivacyRequest) -> ApiResponse[None]:
        return self._http.try_send_json("PUT", "/users/privacy", model=None, json=request.model_dump(by_alias=True))

    def try_bulk_check(self, request: BulkCheckRequest) -> ApiResponse[list[BulkCheckResult]]:
        return self._http.try_send_json(
            "POST", "/users/check", model=list[BulkCheckResult], json=request.model_dump(by_alias=True)
        )

    def try_check(self, user_id: str) -> ApiResponse[UserInfo]:
        return self._http.try_send_json("GET", f"/users/{user_id}/check", model=UserInfo)

    def try_get_user_profile(self, user_id: str) -> ApiResponse[UserInfo]:
        return self._http.try_send_json("GET", f"/users/{user_id}/profile", model=UserInfo)
