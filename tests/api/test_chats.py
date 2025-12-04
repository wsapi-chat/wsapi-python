"""
Tests for ChatsClient API methods.
"""
import pytest
from wsapi_client.api.chats import ChatsClient
from wsapi_client.models.requests.chats import (
    ChatUpdatePresenceRequest,
    ChatUpdateEphemeralExpirationRequest,
    ChatUpdateMuteRequest,
    ChatUpdatePinRequest,
    ChatUpdateArchiveRequest,
    ChatUpdateReadRequest,
)


class TestChatsClient:
    """Test suite for ChatsClient."""

    def test_list_chats(self, wsapi_http, sample_chat_info):
        """Test listing all chats."""
        wsapi_http._mock_client.set_response(200, [sample_chat_info])
        client = ChatsClient(wsapi_http)

        result = client.list()

        assert len(result) == 1
        assert result[0].id == "1234567890@s.whatsapp.net"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/chats"

    def test_get_chat(self, wsapi_http, sample_chat_info):
        """Test getting a single chat."""
        wsapi_http._mock_client.set_response(200, sample_chat_info)
        client = ChatsClient(wsapi_http)

        result = client.get("1234567890@s.whatsapp.net")

        assert result.id == "1234567890@s.whatsapp.net"
        assert result.name == "John Doe"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net"

    def test_get_picture(self, wsapi_http):
        """Test getting chat picture."""
        wsapi_http._mock_client.set_response(200, {
            "pictureId": "pic_123",
            "pictureUrl": "https://example.com/pic.jpg"
        })
        client = ChatsClient(wsapi_http)

        result = client.get_picture("1234567890@s.whatsapp.net")

        assert result.picture_id == "pic_123"
        assert result.picture_url == "https://example.com/pic.jpg"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net/picture"

    def test_get_business_profile(self, wsapi_http):
        """Test getting chat business profile."""
        wsapi_http._mock_client.set_response(200, {
            "id": "1234567890@s.whatsapp.net",
            "address": "123 Main St",
            "description": "A business",
            "email": "info@example.com",
            "website": "https://example.com",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "memberSince": "2020-01-01",
            "categories": [{"id": "cat1", "name": "Retail"}],
            "businessHoursTimeZone": "America/Los_Angeles",
            "businessHours": [
                {"dayOfWeek": "Monday", "mode": "OPEN", "openTime": "09:00", "closeTime": "17:00"}
            ],
            "profileOptions": {"option1": "value1"}
        })
        client = ChatsClient(wsapi_http)

        result = client.get_business_profile("1234567890@s.whatsapp.net")

        assert result.address == "123 Main St"
        assert len(result.categories) == 1
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net/business"

    def test_subscribe_presence(self, wsapi_http):
        """Test subscribing to chat presence."""
        wsapi_http._mock_client.set_response(204)
        client = ChatsClient(wsapi_http)

        client.subscribe_presence("1234567890@s.whatsapp.net")

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net/presence/subscribe"

    def test_update_presence(self, wsapi_http):
        """Test updating chat presence (typing indicator)."""
        wsapi_http._mock_client.set_response(204)
        client = ChatsClient(wsapi_http)

        request = ChatUpdatePresenceRequest(state="typing")
        client.update_presence("1234567890@s.whatsapp.net", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net/presence/set"
        assert call["json"]["state"] == "typing"

    def test_update_ephemeral(self, wsapi_http):
        """Test updating ephemeral message settings."""
        wsapi_http._mock_client.set_response(204)
        client = ChatsClient(wsapi_http)

        request = ChatUpdateEphemeralExpirationRequest(expiration="24h")
        client.update_ephemeral("1234567890@s.whatsapp.net", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net/ephemeral"
        assert call["json"]["expiration"] == "24h"

    def test_update_mute(self, wsapi_http):
        """Test muting a chat."""
        wsapi_http._mock_client.set_response(204)
        client = ChatsClient(wsapi_http)

        request = ChatUpdateMuteRequest(duration="8h")
        client.update_mute("1234567890@s.whatsapp.net", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net/mute"

    def test_update_pin(self, wsapi_http):
        """Test pinning a chat."""
        wsapi_http._mock_client.set_response(204)
        client = ChatsClient(wsapi_http)

        request = ChatUpdatePinRequest(pinned=True)
        client.update_pin("1234567890@s.whatsapp.net", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net/pin"
        assert call["json"]["pinned"] is True

    def test_update_archive(self, wsapi_http):
        """Test archiving a chat."""
        wsapi_http._mock_client.set_response(204)
        client = ChatsClient(wsapi_http)

        request = ChatUpdateArchiveRequest(archived=True)
        client.update_archive("1234567890@s.whatsapp.net", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net/archive"
        assert call["json"]["archived"] is True

    def test_update_read(self, wsapi_http):
        """Test marking a chat as read."""
        wsapi_http._mock_client.set_response(204)
        client = ChatsClient(wsapi_http)

        request = ChatUpdateReadRequest(read=True)
        client.update_read("1234567890@s.whatsapp.net", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net/read"
        assert call["json"]["read"] is True

    def test_delete_chat(self, wsapi_http):
        """Test deleting a chat."""
        wsapi_http._mock_client.set_response(204)
        client = ChatsClient(wsapi_http)

        client.delete_chat("1234567890@s.whatsapp.net")

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "DELETE"
        assert call["url"] == "/chats/1234567890@s.whatsapp.net"


class TestChatsClientTryMethods:
    """Test suite for ChatsClient try_ methods."""

    def test_try_list_success(self, wsapi_http, sample_chat_info):
        """Test try_list on success."""
        wsapi_http._mock_client.set_response(200, [sample_chat_info])
        client = ChatsClient(wsapi_http)

        response = client.try_list()

        assert response.is_success
        assert len(response.result) == 1
        assert response.error is None

    def test_try_get_success(self, wsapi_http, sample_chat_info):
        """Test try_get on success."""
        wsapi_http._mock_client.set_response(200, sample_chat_info)
        client = ChatsClient(wsapi_http)

        response = client.try_get("1234567890@s.whatsapp.net")

        assert response.is_success
        assert response.result.id == "1234567890@s.whatsapp.net"

    def test_try_update_presence_success(self, wsapi_http):
        """Test try_update_presence on success."""
        wsapi_http._mock_client.set_response(204)
        client = ChatsClient(wsapi_http)

        request = ChatUpdatePresenceRequest(state="recording")
        response = client.try_update_presence("1234567890@s.whatsapp.net", request)

        assert response.is_success
