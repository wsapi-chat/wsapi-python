"""
Tests for UsersClient API methods.
"""

from wsapi_client.api.users import UsersClient


class TestUsersClient:
    """Test suite for UsersClient."""

    def test_get_user_profile(self, wsapi_http):
        """Test getting user profile by ID."""
        wsapi_http._mock_client.set_response(
            200,
            {
                "id": "1234567890@s.whatsapp.net",
                "phone": "1234567890",
                "status": "Available",
                "pictureId": "pic_123",
            },
        )
        client = UsersClient(wsapi_http)

        result = client.get_user_profile("1234567890@s.whatsapp.net")

        assert result.id == "1234567890@s.whatsapp.net"
        assert result.status == "Available"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/users/1234567890@s.whatsapp.net/profile"

    def test_check(self, wsapi_http):
        """Test checking if user is on WhatsApp."""
        wsapi_http._mock_client.set_response(
            200,
            {
                "id": "1234567890@s.whatsapp.net",
                "isInWhatsApp": True,
            },
        )
        client = UsersClient(wsapi_http)

        result = client.check("1234567890@s.whatsapp.net")

        assert result.is_in_whats_app is True
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/users/1234567890@s.whatsapp.net/check"

    def test_get_user_profile_not_found(self, wsapi_http):
        """Test getting user profile when not found."""
        wsapi_http._mock_client.set_response(404, None)
        client = UsersClient(wsapi_http)

        try:
            client.get_user_profile("unknown@s.whatsapp.net")
        except Exception:
            pass

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/users/unknown@s.whatsapp.net/profile"


class TestUsersClientTryMethods:
    """Test suite for UsersClient try_ methods."""

    def test_try_get_user_profile_success(self, wsapi_http):
        """Test try_get_user_profile on success."""
        wsapi_http._mock_client.set_response(
            200,
            {
                "id": "1234567890@s.whatsapp.net",
                "status": "Available",
            },
        )
        client = UsersClient(wsapi_http)

        response = client.try_get_user_profile("1234567890@s.whatsapp.net")

        assert response.is_success
        assert response.result.id == "1234567890@s.whatsapp.net"

    def test_try_get_user_profile_not_found(self, wsapi_http):
        """Test try_get_user_profile when user not found."""
        wsapi_http._mock_client.set_response(
            404,
            {
                "type": "https://wsapi.chat/errors/not-found",
                "title": "Not Found",
                "status": 404,
                "detail": "User not found",
            },
        )
        client = UsersClient(wsapi_http)

        response = client.try_get_user_profile("unknown@s.whatsapp.net")

        assert not response.is_success
        assert response.error is not None
        assert response.error.status == 404
