"""
Tests for CallsClient API methods.
"""

from wsapi_client.api.calls import CallsClient
from wsapi_client.models.requests.calls.reject_call_request import RejectCallRequest


class TestCallsClient:
    """Test suite for CallsClient."""

    def test_reject_call(self, wsapi_http):
        """Test rejecting a call."""
        wsapi_http._mock_client.set_response(204)
        client = CallsClient(wsapi_http)

        request = RejectCallRequest(caller_id="1234567890@s.whatsapp.net")
        client.reject("call_123", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "/calls/call_123/reject"


class TestCallsClientTryMethods:
    """Test suite for CallsClient try_ methods."""

    def test_try_reject_success(self, wsapi_http):
        """Test try_reject on success."""
        wsapi_http._mock_client.set_response(204)
        client = CallsClient(wsapi_http)

        request = RejectCallRequest(caller_id="1234567890@s.whatsapp.net")
        response = client.try_reject("call_123", request)

        assert response.is_success
