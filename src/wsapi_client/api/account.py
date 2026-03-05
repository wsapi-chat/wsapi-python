from __future__ import annotations

from typing import Optional

from ..http import ApiResponse, WSApiHttp
from ..models.entities.accounts.account_instance import AccountInstance
from ..models.entities.accounts.account_instance_defaults import AccountInstanceDefaults
from ..models.entities.accounts.account_instance_detail import AccountInstanceDetail
from ..models.entities.accounts.account_instance_settings import AccountInstanceSettings
from ..models.entities.accounts.account_subscription import AccountSubscription
from ..models.entities.accounts.account_subscription_change import AccountSubscriptionChange
from ..models.entities.accounts.paged_response import PagedResponse
from ..models.requests.account.update_instance_name_request import UpdateInstanceNameRequest


class AccountClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    @staticmethod
    def _build_url(base: str, **params) -> str:
        filtered = {k: v for k, v in params.items() if v is not None}
        if not filtered:
            return base
        query = "&".join(f"{k}={v}" for k, v in filtered.items())
        return f"{base}?{query}"

    # ── Instances ─────────────────────────────────────────────

    def list_instances(
        self,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        created_from: Optional[str] = None,
        created_to: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PagedResponse[AccountInstance]:
        url = self._build_url(
            "/account/instances",
            pageNumber=page_number,
            pageSize=page_size,
            createdFrom=created_from,
            createdTo=created_to,
            status=status,
        )
        return self._http.send_json("GET", url, model=PagedResponse[AccountInstance])

    def try_list_instances(
        self,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        created_from: Optional[str] = None,
        created_to: Optional[str] = None,
        status: Optional[str] = None,
    ) -> ApiResponse[PagedResponse[AccountInstance]]:
        url = self._build_url(
            "/account/instances",
            pageNumber=page_number,
            pageSize=page_size,
            createdFrom=created_from,
            createdTo=created_to,
            status=status,
        )
        return self._http.try_send_json("GET", url, model=PagedResponse[AccountInstance])

    def get_instance(self, instance_id: str) -> AccountInstanceDetail:
        return self._http.send_json("GET", f"/account/instances/{instance_id}", model=AccountInstanceDetail)

    def try_get_instance(self, instance_id: str) -> ApiResponse[AccountInstanceDetail]:
        return self._http.try_send_json("GET", f"/account/instances/{instance_id}", model=AccountInstanceDetail)

    def update_instance_name(self, instance_id: str, request: UpdateInstanceNameRequest) -> None:
        self._http.send_json(
            "PUT",
            f"/account/instances/{instance_id}/name",
            model=None,
            json=request.model_dump(by_alias=True),
        )

    def try_update_instance_name(self, instance_id: str, request: UpdateInstanceNameRequest) -> ApiResponse[object]:
        return self._http.try_send_json(
            "PUT",
            f"/account/instances/{instance_id}/name",
            model=None,
            json=request.model_dump(by_alias=True),
        )

    def update_instance_settings(self, instance_id: str, request: AccountInstanceSettings) -> None:
        self._http.send_json(
            "PUT",
            f"/account/instances/{instance_id}/settings",
            model=None,
            json=request.model_dump(by_alias=True),
        )

    def try_update_instance_settings(self, instance_id: str, request: AccountInstanceSettings) -> ApiResponse[object]:
        return self._http.try_send_json(
            "PUT",
            f"/account/instances/{instance_id}/settings",
            model=None,
            json=request.model_dump(by_alias=True),
        )

    def regenerate_instance_api_key(self, instance_id: str) -> str:
        return self._http.send_json("PUT", f"/account/instances/{instance_id}/apikey", model=str)

    def try_regenerate_instance_api_key(self, instance_id: str) -> ApiResponse[str]:
        return self._http.try_send_json("PUT", f"/account/instances/{instance_id}/apikey", model=str)

    def restart_instance(self, instance_id: str) -> None:
        self._http.send_json("PUT", f"/account/instances/{instance_id}/restart", model=None)

    def try_restart_instance(self, instance_id: str) -> ApiResponse[object]:
        return self._http.try_send_json("PUT", f"/account/instances/{instance_id}/restart", model=None)

    # ── Instance Defaults ─────────────────────────────────────

    def get_instance_defaults(self) -> AccountInstanceDefaults:
        return self._http.send_json("GET", "/account/instances/defaults", model=AccountInstanceDefaults)

    def try_get_instance_defaults(self) -> ApiResponse[AccountInstanceDefaults]:
        return self._http.try_send_json("GET", "/account/instances/defaults", model=AccountInstanceDefaults)

    def update_instance_defaults(self, request: AccountInstanceDefaults) -> None:
        self._http.send_json(
            "PUT",
            "/account/instances/defaults",
            model=None,
            json=request.model_dump(by_alias=True),
        )

    def try_update_instance_defaults(self, request: AccountInstanceDefaults) -> ApiResponse[object]:
        return self._http.try_send_json(
            "PUT",
            "/account/instances/defaults",
            model=None,
            json=request.model_dump(by_alias=True),
        )

    # ── Subscriptions ─────────────────────────────────────────

    def list_subscriptions(
        self,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> PagedResponse[AccountSubscription]:
        url = self._build_url(
            "/account/subscriptions",
            pageNumber=page_number,
            pageSize=page_size,
        )
        return self._http.send_json("GET", url, model=PagedResponse[AccountSubscription])

    def try_list_subscriptions(
        self,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ApiResponse[PagedResponse[AccountSubscription]]:
        url = self._build_url(
            "/account/subscriptions",
            pageNumber=page_number,
            pageSize=page_size,
        )
        return self._http.try_send_json("GET", url, model=PagedResponse[AccountSubscription])

    def list_subscription_instances(
        self,
        subscription_id: str,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        created_from: Optional[str] = None,
        created_to: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PagedResponse[AccountInstance]:
        url = self._build_url(
            f"/account/subscriptions/{subscription_id}/instances",
            pageNumber=page_number,
            pageSize=page_size,
            createdFrom=created_from,
            createdTo=created_to,
            status=status,
        )
        return self._http.send_json("GET", url, model=PagedResponse[AccountInstance])

    def try_list_subscription_instances(
        self,
        subscription_id: str,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        created_from: Optional[str] = None,
        created_to: Optional[str] = None,
        status: Optional[str] = None,
    ) -> ApiResponse[PagedResponse[AccountInstance]]:
        url = self._build_url(
            f"/account/subscriptions/{subscription_id}/instances",
            pageNumber=page_number,
            pageSize=page_size,
            createdFrom=created_from,
            createdTo=created_to,
            status=status,
        )
        return self._http.try_send_json("GET", url, model=PagedResponse[AccountInstance])

    def create_subscription_instance(self, subscription_id: str) -> str:
        return self._http.send_json(
            "POST",
            f"/account/subscriptions/{subscription_id}/instances",
            model=str,
        )

    def try_create_subscription_instance(self, subscription_id: str) -> ApiResponse[str]:
        return self._http.try_send_json(
            "POST",
            f"/account/subscriptions/{subscription_id}/instances",
            model=str,
        )

    def delete_subscription_instance(self, subscription_id: str, instance_id: str) -> None:
        self._http.send_json(
            "DELETE",
            f"/account/subscriptions/{subscription_id}/instances/{instance_id}",
            model=None,
        )

    def try_delete_subscription_instance(self, subscription_id: str, instance_id: str) -> ApiResponse[object]:
        return self._http.try_send_json(
            "DELETE",
            f"/account/subscriptions/{subscription_id}/instances/{instance_id}",
            model=None,
        )

    # ── Subscription Changes ──────────────────────────────────

    def list_subscription_changes(
        self,
        subscription_id: str,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        timestamp_from: Optional[str] = None,
        timestamp_to: Optional[str] = None,
        change_type: Optional[str] = None,
        instance_id: Optional[str] = None,
    ) -> PagedResponse[AccountSubscriptionChange]:
        url = self._build_url(
            f"/account/subscriptions/{subscription_id}/changes",
            pageNumber=page_number,
            pageSize=page_size,
            timestampFrom=timestamp_from,
            timestampTo=timestamp_to,
            changeType=change_type,
            instanceId=instance_id,
        )
        return self._http.send_json("GET", url, model=PagedResponse[AccountSubscriptionChange])

    def try_list_subscription_changes(
        self,
        subscription_id: str,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        timestamp_from: Optional[str] = None,
        timestamp_to: Optional[str] = None,
        change_type: Optional[str] = None,
        instance_id: Optional[str] = None,
    ) -> ApiResponse[PagedResponse[AccountSubscriptionChange]]:
        url = self._build_url(
            f"/account/subscriptions/{subscription_id}/changes",
            pageNumber=page_number,
            pageSize=page_size,
            timestampFrom=timestamp_from,
            timestampTo=timestamp_to,
            changeType=change_type,
            instanceId=instance_id,
        )
        return self._http.try_send_json("GET", url, model=PagedResponse[AccountSubscriptionChange])
