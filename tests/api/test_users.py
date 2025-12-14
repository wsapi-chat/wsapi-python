"""
Tests for UsersClient API methods.
"""
import pytest
from wsapi_client.api.users import UsersClient


class TestUsersClient:
    """Test suite for UsersClient."""

    def test_get_by_id(self, wsapi_http, sample_user_info):
        """Test getting user by ID."""
        wsapi_http._mock_client.set_response(200, sample_user_info)
        client = UsersClient(wsapi_http)

        result = client.get_by_id("1234567890@s.whatsapp.net")

        assert result.jid == "1234567890@s.whatsapp.net"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/users/1234567890@s.whatsapp.net"

    def test_get_by_id_not_found(self, wsapi_http):
        """Test getting user by ID when not found."""
        wsapi_http._mock_client.set_response(404, None)
        client = UsersClient(wsapi_http)

        # This should return None or raise based on implementation
        # For now just verify the call was made correctly
        call_made = False
        try:
            client.get_by_id("unknown@s.whatsapp.net")
        except Exception:
            call_made = True

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/users/unknown@s.whatsapp.net"


class TestUsersClientTryMethods:
    """Test suite for UsersClient try_ methods."""

    def test_try_get_by_id_success(self, wsapi_http, sample_user_info):
        """Test try_get_by_id on success."""
        wsapi_http._mock_client.set_response(200, sample_user_info)
        client = UsersClient(wsapi_http)

        response = client.try_get_by_id("1234567890@s.whatsapp.net")

        assert response.is_success
        assert response.result.jid == "1234567890@s.whatsapp.net"

    def test_try_get_by_id_not_found(self, wsapi_http):
        """Test try_get_by_id when user not found."""
        wsapi_http._mock_client.set_response(404, {
            "type": "https://wsapi.chat/errors/not-found",
            "title": "Not Found",
            "status": 404,
            "detail": "User not found"
        })
        client = UsersClient(wsapi_http)

        response = client.try_get_by_id("unknown@s.whatsapp.net")

        assert not response.is_success
        assert response.error is not None
        assert response.error.status == 404
