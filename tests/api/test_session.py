"""
Tests for SessionClient API methods.
"""

from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from wsapi_client.api.session import SessionClient
from wsapi_client.exceptions import ApiException
from wsapi_client.models import PasskeyAssertion
from wsapi_client.models.constants.passkey_statuses import PasskeySources, PasskeyStatuses
from wsapi_client.models.entities.session.passkey_state import PasskeyState


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


ASSERTION = {
    "id": "cred",
    "rawId": "cred",
    "type": "public-key",
    "response": {
        "clientDataJSON": "Y2xpZW50",
        "authenticatorData": "YXV0aA",
        "signature": "c2ln",
        "userHandle": None,
    },
    "clientExtensionResults": {},
}

REQUIRED_STATE = {
    "status": "required",
    "source": "notification",
    "challenge": {
        "challenge": "Y2hhbGxlbmdl",
        "timeout": 600000,
        "rpId": "whatsapp.com",
        "allowCredentials": [{"id": "cred", "type": "public-key", "transports": ["internal", "hybrid"]}],
        "userVerification": "required",
        "extensions": {},
    },
    "origin": "https://web.whatsapp.com",
    "requestedAt": "2026-11-25T10:00:00Z",
    "expiresAt": "2026-11-25T10:05:00Z",
}


class TestSessionPasskey:
    """Passkey (WebAuthn) pairing step."""

    @pytest.mark.parametrize("prefix", ["", "try_"])
    def test_get_passkey_state(self, wsapi_http, prefix):
        wsapi_http._mock_client.set_response(200, REQUIRED_STATE)

        result = getattr(SessionClient(wsapi_http), prefix + "get_passkey_state")()
        if prefix:
            assert result.is_success
            result = result.result

        assert isinstance(result, PasskeyState)
        assert result.status == PasskeyStatuses.REQUIRED
        assert result.is_pending
        assert result.source == "notification"
        assert result.origin == "https://web.whatsapp.com"
        assert result.challenge.rp_id == "whatsapp.com"
        assert result.challenge.allow_credentials[0].transports == ["internal", "hybrid"]
        assert result.expires_at == datetime(2026, 11, 25, 10, 5, tzinfo=timezone.utc)
        # The challenge round-trips to the browser's JSON shape.
        assert result.challenge.model_dump(by_alias=True, exclude_none=True) == REQUIRED_STATE["challenge"]
        call = wsapi_http._mock_client.get_last_call()
        assert (call["method"], call["url"]) == ("GET", "/session/passkey")

    @pytest.mark.parametrize("prefix", ["", "try_"])
    @pytest.mark.parametrize("as_model", [False, True])
    def test_submit_passkey(self, wsapi_http, prefix, as_model):
        wsapi_http._mock_client.set_response(
            200, {"status": "confirmation_required", "confirmationCode": "123456", "confirmationSent": True}
        )
        assertion = PasskeyAssertion.model_validate(ASSERTION) if as_model else ASSERTION

        result = getattr(SessionClient(wsapi_http), prefix + "submit_passkey")(assertion)
        if prefix:
            assert result.is_success
            result = result.result

        assert result.status == PasskeyStatuses.CONFIRMATION_REQUIRED
        assert result.confirmation_code == "123456"
        assert result.confirmation_sent is True
        call = wsapi_http._mock_client.get_last_call()
        assert (call["method"], call["url"]) == ("POST", "/session/passkey")
        assert call["json"] == {
            "id": "cred",
            "rawId": "cred",
            "type": "public-key",
            "response": {"clientDataJSON": "Y2xpZW50", "authenticatorData": "YXV0aA", "signature": "c2ln"},
            "clientExtensionResults": {},
        }

    def test_submit_passkey_rejects_incomplete_assertion(self, wsapi_http):
        client = SessionClient(wsapi_http)
        with pytest.raises(ValidationError):
            client.submit_passkey({"rawId": "cred"})
        response = client.try_submit_passkey({"rawId": "cred"})
        assert not response.is_success
        assert response.error.status == 400
        assert wsapi_http._mock_client.calls == []

    @pytest.mark.parametrize("prefix", ["", "try_"])
    def test_request_passkey(self, wsapi_http, prefix):
        wsapi_http._mock_client.set_response(200, {**REQUIRED_STATE, "source": "requested"})

        result = getattr(SessionClient(wsapi_http), prefix + "request_passkey")()
        if prefix:
            result = result.result

        assert result.source == PasskeySources.REQUESTED
        call = wsapi_http._mock_client.get_last_call()
        assert (call["method"], call["url"], call["json"]) == ("POST", "/session/passkey/request", None)

    @pytest.mark.parametrize("prefix", ["", "try_"])
    def test_confirm_passkey(self, wsapi_http, prefix):
        wsapi_http._mock_client.set_response(204)

        result = getattr(SessionClient(wsapi_http), prefix + "confirm_passkey")()

        assert (result.result if prefix else result) is None
        call = wsapi_http._mock_client.get_last_call()
        assert (call["method"], call["url"]) == ("POST", "/session/passkey/confirm")

    def test_session_status_passkey_status(self, wsapi_http):
        wsapi_http._mock_client.set_response(
            200, {"isConnected": True, "isLoggedIn": False, "passkeyStatus": "submitted"}
        )

        status = SessionClient(wsapi_http).get_session_status()

        assert status.passkey_status == PasskeyStatuses.SUBMITTED
        assert status.is_passkey_pending

    def test_session_status_without_passkey_status(self, wsapi_http, sample_session_status):
        wsapi_http._mock_client.set_response(200, sample_session_status)

        status = SessionClient(wsapi_http).get_session_status()

        assert status.passkey_status is None
        assert not status.is_passkey_pending

    @pytest.mark.parametrize(
        "method,args",
        [("get_qr_image", ()), ("get_qr_code", ()), ("get_pair_code", ("1234567890",))],
    )
    def test_qr_and_pair_code_surface_passkey_pending(self, wsapi_http, method, args):
        pending = {"status": 409, "detail": "passkey verification pending"}
        wsapi_http._mock_client.set_response(409, pending)
        client = SessionClient(wsapi_http)

        with pytest.raises(ApiException) as exc:
            getattr(client, method)(*args)
        assert exc.value.problem.status == 409

        response = getattr(client, "try_" + method)(*args)
        assert not response.is_success
        assert response.error.status == 409
        assert response.error.detail == "passkey verification pending"
