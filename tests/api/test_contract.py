"""Regression tests against the current wire contract, including non-throwing calls."""

import importlib
import json
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlsplit

import pytest

from wsapi_client.api.account import AccountClient
from wsapi_client.api.chats import ChatsClient
from wsapi_client.api.communities import CommunitiesClient
from wsapi_client.api.contacts import ContactsClient
from wsapi_client.api.groups import GroupsClient
from wsapi_client.api.media import MediaClient
from wsapi_client.api.messages import MessagesClient
from wsapi_client.api.newsletters import NewslettersClient
from wsapi_client.api.users import UsersClient
from wsapi_client.events.factory import parse_event
from wsapi_client.models.requests.communities.community_requests import LinkGroupRequest
from wsapi_client.models.requests.groups.group_join_with_invite_request import GroupJoinWithInviteRequest
from wsapi_client.models.requests.groups.group_join_with_link_request import GroupJoinWithLinkRequest
from wsapi_client.models.requests.newsletters.newsletter_requests import SetSubscriptionRequest
from wsapi_client.models.requests.users.set_presence_request import SetMyPresenceRequest
from wsapi_client.models.requests.users.set_privacy_request import SetPrivacyRequest
from wsapi_client.models.requests.users.update_profile_request import UpdateProfileRequest


@pytest.mark.parametrize("prefix", ["", "try_"])
@pytest.mark.parametrize(
    "client_type,method,args,verb,path,response",
    [
        (ContactsClient, "block", ("u",), "PUT", "/contacts/u/block", None),
        (ContactsClient, "unblock", ("u",), "PUT", "/contacts/u/unblock", None),
        (ChatsClient, "clear", ("c",), "POST", "/chats/c/clear", None),
        (
            NewslettersClient,
            "set_subscription",
            ("n", SetSubscriptionRequest(subscribed=False)),
            "PUT",
            "/newsletters/n/subscription",
            None,
        ),
        (
            CommunitiesClient,
            "link_group",
            ("c", LinkGroupRequest(group_id="g")),
            "POST",
            "/communities/c/groups/link",
            None,
        ),
        (
            CommunitiesClient,
            "unlink_group",
            ("c", LinkGroupRequest(group_id="g/1")),
            "DELETE",
            "/communities/c/groups/g%2F1",
            None,
        ),
        (UsersClient, "get_profile", (), "GET", "/users/me/profile", {"id": "u"}),
        (UsersClient, "update_profile", (UpdateProfileRequest(name="Name"),), "PUT", "/users/me/profile", None),
        (UsersClient, "set_presence", (SetMyPresenceRequest(presence="available"),), "PUT", "/users/me/presence", None),
        (UsersClient, "get_privacy_settings", (), "GET", "/users/me/privacy", {"lastSeen": "contacts"}),
        (
            UsersClient,
            "set_privacy_setting",
            (SetPrivacyRequest(setting="lastSeen", value="contacts"),),
            "PUT",
            "/users/me/privacy",
            {"lastSeen": "contacts"},
        ),
    ],
)
def test_current_routes(wsapi_http, prefix, client_type, method, args, verb, path, response):
    wsapi_http._mock_client.set_response(200 if response is not None else 204, response)
    result = getattr(client_type(wsapi_http), prefix + method)(*args)
    if prefix:
        assert result.is_success, result.error
        result = result.result
    call = wsapi_http._mock_client.get_last_call()
    assert (call["method"], call["url"]) == (verb, path)
    if method == "set_privacy_setting":
        assert result.last_seen == "contacts"
    if method == "unlink_group":
        assert call["json"] is None
    if method == "set_subscription":
        assert call["json"]["subscribed"] is False


@pytest.mark.parametrize("prefix", ["", "try_"])
def test_group_join_response_contract(wsapi_http, prefix):
    client = GroupsClient(wsapi_http)
    wsapi_http._mock_client.set_response(200, {"id": "g"})
    joined = getattr(client, prefix + "join_with_link")(GroupJoinWithLinkRequest(code="invite"))
    assert (joined.result if prefix else joined).id == "g"
    wsapi_http._mock_client.set_response(204)
    joined = getattr(client, prefix + "join_with_invite")(
        GroupJoinWithInviteRequest(group_id="g", inviter_id="u", code="invite")
    )
    assert (joined.result if prefix else joined) is None
    if prefix:
        assert joined.is_success


@pytest.mark.parametrize("prefix", ["", "try_"])
def test_media_id_is_encoded(wsapi_http, prefix):
    wsapi_http._mock_client.set_response(200, content=b"\x00\xff")
    result = getattr(MediaClient(wsapi_http), prefix + "download")("a+/=&")
    assert (result.result if prefix else result) == b"\x00\xff"
    assert wsapi_http._mock_client.get_last_call()["url"] == "/media/download?id=a%2B%2F%3D%26"


@pytest.mark.parametrize("kind", ["image", "video", "audio", "voice", "document", "sticker"])
def test_legacy_media_imports_serialize_canonical_fields(kind):
    module = importlib.import_module(f"wsapi_client.models.requests.messages.message_send_{kind}_request")
    cls = getattr(module, f"MessageSend{kind.title()}Request")
    request = cls(**{"to": "u", f"{kind}_url": "https://example.com/media", "filename": "sample.bin"})
    body = request.model_dump(by_alias=True, exclude_none=True)
    assert body["url"] == "https://example.com/media"
    assert not any(key.endswith(("Url", "URL", "Base64")) for key in body)


@pytest.mark.parametrize("history", [False, True])
def test_ad_referral_is_retained(history):
    message = {
        "id": "m",
        "chatId": "c",
        "sender": {"id": "u"},
        "time": "2026-09-21T00:00:00Z",
        "type": "text",
        "text": "Hi",
        "adReferral": {"ctwaClid": "click", "showAdAttribution": False},
    }
    event = parse_event(
        json.dumps(
            {
                "eventId": "e",
                "instanceId": "i",
                "receivedAt": "2026-09-21T00:00:00Z",
                "eventType": "message_history_sync" if history else "message",
                "eventData": {"chatId": "c", "messages": [message]} if history else message,
            }
        )
    )
    message_model = event.messages[0] if history else event
    assert message_model.ad_referral.ctwa_clid == "click"
    assert message_model.ad_referral.show_ad_attribution is False


@pytest.mark.parametrize("prefix", ["", "try_"])
def test_named_cloud_instance(wsapi_http, prefix):
    wsapi_http._mock_client.set_response(200, "instance-id")
    result = getattr(AccountClient(wsapi_http), prefix + "create_subscription_instance")("sub", name="A + B& C")
    assert (result.result if prefix else result) == "instance-id"
    call = wsapi_http._mock_client.get_last_call()
    assert call["method"] == "POST"
    assert parse_qs(urlsplit(call["url"]).query) == {"name": ["A + B& C"]}


def test_account_filter_encoding():
    url = AccountClient._build_url(
        "/account/instances", createdFrom="2026-09-21T00:00:00+03:00", status="a&b", pageNumber=0
    )
    assert parse_qs(urlsplit(url).query) == {
        "createdFrom": ["2026-09-21T00:00:00+03:00"],
        "status": ["a&b"],
        "pageNumber": ["0"],
    }


@pytest.mark.parametrize("prefix", ["", "try_"])
def test_legacy_delete_datetime_uses_json_timestamp(wsapi_http, prefix):
    from wsapi_client.models.requests.messages.message_delete_for_me_request import MessageDeleteForMeRequest

    wsapi_http._mock_client.set_response(204)
    request = MessageDeleteForMeRequest(
        chat_id="c", sender_id="u", is_from_me=False, timestamp=datetime(2026, 9, 21, tzinfo=timezone.utc)
    )
    getattr(MessagesClient(wsapi_http), prefix + "delete_for_me")("m", request)
    body = wsapi_http._mock_client.get_last_call()["json"]
    assert body["timestamp"] == "2026-09-21T00:00:00Z"
    assert body["isFromMe"] is False
