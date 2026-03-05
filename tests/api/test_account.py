"""
Tests for AccountClient API methods.
"""

from wsapi_client.api.account import AccountClient
from wsapi_client.models.requests.account.update_instance_name_request import UpdateInstanceNameRequest


class TestAccountClient:
    """Test suite for AccountClient."""

    def test_list_instances(self, wsapi_http):
        """Test listing instances."""
        wsapi_http._mock_client.set_response(
            200,
            {
                "items": [
                    {
                        "id": "ins_123",
                        "created": "2025-01-01T00:00:00Z",
                        "name": "Test Instance",
                        "status": "active",
                    }
                ],
                "totalCount": 1,
                "pageNumber": 1,
                "pageSize": 20,
            },
        )
        client = AccountClient(wsapi_http)

        client.list_instances()

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/account/instances"

    def test_get_instance(self, wsapi_http):
        """Test getting a single instance."""
        wsapi_http._mock_client.set_response(
            200,
            {
                "name": "Test Instance",
                "hasApiKey": True,
                "status": "active",
                "deviceId": "dev_123",
                "created": "2025-01-01T00:00:00Z",
            },
        )
        client = AccountClient(wsapi_http)

        result = client.get_instance("ins_123")

        assert result.name == "Test Instance"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/account/instances/ins_123"

    def test_update_instance_name(self, wsapi_http):
        """Test updating instance name."""
        wsapi_http._mock_client.set_response(204)
        client = AccountClient(wsapi_http)

        request = UpdateInstanceNameRequest(name="New Name")
        client.update_instance_name("ins_123", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/account/instances/ins_123/name"
        assert call["json"]["name"] == "New Name"

    def test_restart_instance(self, wsapi_http):
        """Test restarting an instance."""
        wsapi_http._mock_client.set_response(204)
        client = AccountClient(wsapi_http)

        client.restart_instance("ins_123")

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/account/instances/ins_123/restart"

    def test_list_subscriptions(self, wsapi_http):
        """Test listing subscriptions."""
        wsapi_http._mock_client.set_response(
            200,
            {
                "items": [],
                "totalCount": 0,
                "pageNumber": 1,
                "pageSize": 20,
            },
        )
        client = AccountClient(wsapi_http)

        client.list_subscriptions()

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/account/subscriptions"


class TestAccountClientTryMethods:
    """Test suite for AccountClient try_ methods."""

    def test_try_get_instance_success(self, wsapi_http):
        """Test try_get_instance on success."""
        wsapi_http._mock_client.set_response(
            200,
            {
                "name": "Test Instance",
                "hasApiKey": True,
                "status": "active",
                "deviceId": "dev_123",
                "created": "2025-01-01T00:00:00Z",
            },
        )
        client = AccountClient(wsapi_http)

        response = client.try_get_instance("ins_123")

        assert response.is_success
        assert response.result.name == "Test Instance"

    def test_try_update_instance_name_success(self, wsapi_http):
        """Test try_update_instance_name on success."""
        wsapi_http._mock_client.set_response(204)
        client = AccountClient(wsapi_http)

        request = UpdateInstanceNameRequest(name="New Name")
        response = client.try_update_instance_name("ins_123", request)

        assert response.is_success

    def test_try_restart_instance_success(self, wsapi_http):
        """Test try_restart_instance on success."""
        wsapi_http._mock_client.set_response(204)
        client = AccountClient(wsapi_http)

        response = client.try_restart_instance("ins_123")

        assert response.is_success
