"""
Tests for AccountClient API methods.
"""
import pytest
from wsapi_client.api.account import AccountClient
from wsapi_client.models.requests.account.account_update_name_request import AccountUpdateNameRequest
from wsapi_client.models.requests.account.account_update_status_request import AccountUpdateStatusRequest
from wsapi_client.models.requests.account.account_update_picture_request import AccountUpdatePictureRequest
from wsapi_client.models.requests.account.account_update_presence_request import AccountUpdatePresenceRequest


class TestAccountClient:
    """Test suite for AccountClient."""

    def test_get_info(self, wsapi_http, sample_account_info):
        """Test getting account info."""
        wsapi_http._mock_client.set_response(200, sample_account_info)
        client = AccountClient(wsapi_http)

        result = client.get_info()

        assert result.id == "1234567890@s.whatsapp.net"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/account/info"

    def test_update_name(self, wsapi_http):
        """Test updating account name."""
        wsapi_http._mock_client.set_response(204)
        client = AccountClient(wsapi_http)

        request = AccountUpdateNameRequest(name="New Name")
        client.update_name(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/account/name"
        assert call["json"]["name"] == "New Name"

    def test_update_status(self, wsapi_http):
        """Test updating account status."""
        wsapi_http._mock_client.set_response(204)
        client = AccountClient(wsapi_http)

        request = AccountUpdateStatusRequest(status="Busy")
        client.update_status(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/account/status"
        assert call["json"]["status"] == "Busy"

    def test_update_picture(self, wsapi_http):
        """Test updating account picture."""
        wsapi_http._mock_client.set_response(201, {"pictureId": "pic_123"})
        client = AccountClient(wsapi_http)

        request = AccountUpdatePictureRequest(picture_base64="base64encodedimage")
        result = client.update_picture(request)

        assert result.picture_id == "pic_123"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "/account/picture"

    def test_update_presence(self, wsapi_http):
        """Test updating account presence."""
        wsapi_http._mock_client.set_response(204)
        client = AccountClient(wsapi_http)

        request = AccountUpdatePresenceRequest(status="available")
        client.update_presence(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/account/presence"


class TestAccountClientTryMethods:
    """Test suite for AccountClient try_ methods."""

    def test_try_get_info_success(self, wsapi_http, sample_account_info):
        """Test try_get_info on success."""
        wsapi_http._mock_client.set_response(200, sample_account_info)
        client = AccountClient(wsapi_http)

        response = client.try_get_info()

        assert response.is_success
        assert response.result.id == "1234567890@s.whatsapp.net"

    def test_try_update_name_success(self, wsapi_http):
        """Test try_update_name on success."""
        wsapi_http._mock_client.set_response(204)
        client = AccountClient(wsapi_http)

        request = AccountUpdateNameRequest(name="New Name")
        response = client.try_update_name(request)

        assert response.is_success

    def test_try_update_picture_success(self, wsapi_http):
        """Test try_update_picture on success."""
        wsapi_http._mock_client.set_response(201, {"pictureId": "pic_456"})
        client = AccountClient(wsapi_http)

        request = AccountUpdatePictureRequest(picture_base64="base64data")
        response = client.try_update_picture(request)

        assert response.is_success
        assert response.result.picture_id == "pic_456"
