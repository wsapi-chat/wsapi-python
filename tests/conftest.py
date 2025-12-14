"""
Pytest configuration and shared fixtures for wsapi-client tests.
"""
from __future__ import annotations
from typing import Any, Optional
from unittest.mock import MagicMock, Mock
import pytest

from wsapi_client.http import WSApiHttp, ApiResponse
from wsapi_client.models.problem_details import ProblemDetails


class MockResponse:
    """Mock httpx response for testing."""

    def __init__(
        self,
        status_code: int = 200,
        json_data: Any = None,
        content: bytes = b"",
        text: str = ""
    ):
        self.status_code = status_code
        self._json_data = json_data
        # If json_data is provided, set content to non-empty to indicate body exists
        # This is needed because _has_body checks len(content) > 0
        if json_data is not None and not content:
            self.content = b'{"_mock": true}'
        else:
            self.content = content
        self.text = text

    def json(self) -> Any:
        return self._json_data


class MockHttpClient:
    """Mock HTTP client that records calls and returns configured responses."""

    def __init__(self):
        self.calls: list[dict] = []
        self.response: Optional[MockResponse] = None

    def set_response(
        self,
        status_code: int = 200,
        json_data: Any = None,
        content: bytes = b""
    ):
        self.response = MockResponse(status_code, json_data, content)

    def request(self, method: str, url: str, json: Any = None) -> MockResponse:
        self.calls.append({
            "method": method,
            "url": url,
            "json": json
        })
        return self.response or MockResponse(200, {})

    def stream(self, method: str, url: str):
        """Mock stream context manager."""
        self.calls.append({"method": method, "url": url, "stream": True})
        return MagicMock()

    def close(self):
        pass

    def get_last_call(self) -> Optional[dict]:
        return self.calls[-1] if self.calls else None

    def clear_calls(self):
        self.calls = []


@pytest.fixture
def mock_http_client():
    """Fixture that provides a mock HTTP client."""
    return MockHttpClient()


@pytest.fixture
def wsapi_http(mock_http_client):
    """Fixture that provides a WSApiHttp instance with mocked client."""
    http = WSApiHttp(
        api_key="test-api-key",
        instance_id="test-instance-id",
        client=mock_http_client
    )
    # Store reference to mock client for test assertions
    http._mock_client = mock_http_client
    return http


# Sample data fixtures
@pytest.fixture
def sample_message_created():
    return {"id": "msg_123456789"}


@pytest.fixture
def sample_chat_info():
    return {
        "id": "1234567890@s.whatsapp.net",
        "isReadOnly": False,
        "isGroup": False,
        "isArchived": False,
        "isPinned": False,
        "isEphemeral": False,
        "isMuted": False,
        "isSpam": False,
        "pushName": "John Doe",
        "businessName": None,
        "status": "Available"
    }


@pytest.fixture
def sample_contact_info():
    return {
        "id": "1234567890@s.whatsapp.net",
        "fullName": "John Doe",
        "businessName": "Doe Corp",
        "pushName": "Johnny",
        "status": "Available",
        "pictureId": "pic_123",
        "inPhoneAddressBook": True
    }


@pytest.fixture
def sample_group_info():
    """Sample group info matching the OpenAPI spec for GET /groups and GET /groups/{groupId}."""
    return {
        "id": "123456789-987654321@g.us",
        "name": "Test Group",
        "description": "A test group",
        "picture": "https://example.com/group-pic.jpg",
        "inviteLink": "https://chat.whatsapp.com/ABC123",
        "participants": ["1234567890@s.whatsapp.net", "9876543210@s.whatsapp.net"]
    }


@pytest.fixture
def sample_user_info():
    return {
        "jid": "1234567890@s.whatsapp.net",
        "name": "John Doe",
        "status": "Available"
    }


@pytest.fixture
def sample_instance_settings():
    return {
        "name": "Test Instance",
        "description": "Test description",
        "webhookUrl": "https://example.com/webhook",
        "webhookAuthHeader": "X-Auth",
        "webhookAuthValue": "secret",
        "pullMode": False,
        "eventFilters": ["message", "message_read"]
    }


@pytest.fixture
def sample_session_status():
    return {
        "connected": True,
        "isLoggedIn": True
    }


@pytest.fixture
def sample_account_info():
    return {
        "id": "1234567890@s.whatsapp.net",
        "deviceId": 1,
        "phone": "1234567890",
        "pushName": "My Account",
        "businessName": "Test Business",
        "status": "Available",
        "pictureId": "pic_123"
    }
