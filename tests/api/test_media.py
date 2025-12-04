"""
Tests for MediaClient API methods.
"""
import pytest
from wsapi_client.api.media import MediaClient


class TestMediaClient:
    """Test suite for MediaClient."""

    def test_download(self, wsapi_http):
        """Test downloading media."""
        wsapi_http._mock_client.set_response(200, content=b"binary_media_data")
        client = MediaClient(wsapi_http)

        result = client.download("media_123")

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/media/download?id=media_123"


class TestMediaClientTryMethods:
    """Test suite for MediaClient try_ methods."""

    def test_try_download_success(self, wsapi_http):
        """Test try_download on success."""
        wsapi_http._mock_client.set_response(200, content=b"binary_data")
        client = MediaClient(wsapi_http)

        response = client.try_download("media_456")

        assert response.is_success
        call = wsapi_http._mock_client.get_last_call()
        assert call["url"] == "/media/download?id=media_456"
