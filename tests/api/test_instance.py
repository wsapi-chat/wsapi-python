"""
Tests for InstanceClient API methods.
"""
import pytest
from wsapi_client.api.instance import InstanceClient
from wsapi_client.models.entities.instance.instance_settings import InstanceSettings


class TestInstanceClient:
    """Test suite for InstanceClient."""

    def test_get_settings(self, wsapi_http, sample_instance_settings):
        """Test getting instance settings."""
        wsapi_http._mock_client.set_response(200, sample_instance_settings)
        client = InstanceClient(wsapi_http)

        result = client.get_settings()

        assert result.name == "Test Instance"
        assert result.webhook_url == "https://example.com/webhook"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/instance/settings"

    def test_update_settings(self, wsapi_http):
        """Test updating instance settings."""
        wsapi_http._mock_client.set_response(200, {})
        client = InstanceClient(wsapi_http)

        settings = InstanceSettings(
            name="Updated Instance",
            description="Updated description",
            webhook_url="https://new.example.com/webhook"
        )
        client.update_settings(settings)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/instance/settings"
        assert call["json"]["name"] == "Updated Instance"

    def test_restart(self, wsapi_http):
        """Test restarting instance."""
        wsapi_http._mock_client.set_response(200, {})
        client = InstanceClient(wsapi_http)

        client.restart()

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/instance/restart"

    def test_update_api_key(self, wsapi_http):
        """Test updating API key."""
        wsapi_http._mock_client.set_response(200, "new-api-key-123")
        client = InstanceClient(wsapi_http)

        result = client.update_api_key()

        assert result == "new-api-key-123"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/instance/apikey"


class TestInstanceClientTryMethods:
    """Test suite for InstanceClient try_ methods."""

    def test_try_get_settings_success(self, wsapi_http, sample_instance_settings):
        """Test try_get_settings on success."""
        wsapi_http._mock_client.set_response(200, sample_instance_settings)
        client = InstanceClient(wsapi_http)

        response = client.try_get_settings()

        assert response.is_success
        assert response.result.name == "Test Instance"

    def test_try_restart_success(self, wsapi_http):
        """Test try_restart on success."""
        wsapi_http._mock_client.set_response(200, {})
        client = InstanceClient(wsapi_http)

        response = client.try_restart()

        assert response.is_success

    def test_try_update_api_key_success(self, wsapi_http):
        """Test try_update_api_key on success."""
        wsapi_http._mock_client.set_response(200, "new-key")
        client = InstanceClient(wsapi_http)

        response = client.try_update_api_key()

        assert response.is_success
        assert response.result == "new-key"
