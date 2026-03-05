"""
Tests for SessionClient API methods.
"""

from wsapi_client.api.session import SessionClient


class TestSessionClient:
    """Test suite for SessionClient."""

    def test_get_session_status(self, wsapi_http, sample_session_status):
        """Test getting session status."""
        wsapi_http._mock_client.set_response(200, sample_session_status)
        client = SessionClient(wsapi_http)

        result = client.get_session_status()

        assert result.is_connected is True
        assert result.is_logged_in is True
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/session/status"

    def test_get_qr_code(self, wsapi_http):
        """Test getting login QR code."""
        wsapi_http._mock_client.set_response(200, {"code": "base64encodedqrcode"})
        client = SessionClient(wsapi_http)

        result = client.get_qr_code()

        assert result.code == "base64encodedqrcode"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/session/qr/text"

    def test_get_pair_code(self, wsapi_http):
        """Test getting login pair code."""
        wsapi_http._mock_client.set_response(200, {"code": "ABC123"})
        client = SessionClient(wsapi_http)

        result = client.get_pair_code("1234567890")

        assert result.code == "ABC123"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/session/pair-code/1234567890"

    def test_logout(self, wsapi_http):
        """Test logging out."""
        wsapi_http._mock_client.set_response(200, {})
        client = SessionClient(wsapi_http)

        client.logout()

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "/session/logout"

    def test_flush_history(self, wsapi_http):
        """Test flushing history."""
        wsapi_http._mock_client.set_response(202)
        client = SessionClient(wsapi_http)

        client.flush_history()

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "/session/flush-history"


class TestSessionClientTryMethods:
    """Test suite for SessionClient try_ methods."""

    def test_try_get_session_status_success(self, wsapi_http, sample_session_status):
        """Test try_get_session_status on success."""
        wsapi_http._mock_client.set_response(200, sample_session_status)
        client = SessionClient(wsapi_http)

        response = client.try_get_session_status()

        assert response.is_success
        assert response.result.is_connected is True

    def test_try_get_qr_code_success(self, wsapi_http):
        """Test try_get_qr_code on success."""
        wsapi_http._mock_client.set_response(200, {"code": "base64qr"})
        client = SessionClient(wsapi_http)

        response = client.try_get_qr_code()

        assert response.is_success
        assert response.result.code == "base64qr"

    def test_try_logout_success(self, wsapi_http):
        """Test try_logout on success."""
        wsapi_http._mock_client.set_response(200, {})
        client = SessionClient(wsapi_http)

        response = client.try_logout()

        assert response.is_success

    def test_try_flush_history_success(self, wsapi_http):
        """Test try_flush_history on success."""
        wsapi_http._mock_client.set_response(202)
        client = SessionClient(wsapi_http)

        response = client.try_flush_history()

        assert response.is_success
