import hashlib
import hmac

from wsapi_client.webhooks import verify_signature

SECRET = "my-signing-secret"
BODY = b'{"eventType":"message","instanceId":"abc","receivedAt":"2024-01-01T00:00:00Z","eventData":{}}'


def _sign(body: bytes, secret: str) -> str:
    digest = hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def test_valid_signature():
    header = _sign(BODY, SECRET)
    assert verify_signature(BODY, SECRET, header) is True


def test_invalid_signature():
    assert verify_signature(BODY, SECRET, "sha256=bad") is False


def test_wrong_secret():
    header = _sign(BODY, "wrong-secret")
    assert verify_signature(BODY, SECRET, header) is False


def test_empty_signature_header():
    assert verify_signature(BODY, SECRET, "") is False


def test_tampered_body():
    header = _sign(BODY, SECRET)
    assert verify_signature(b"tampered", SECRET, header) is False


def test_missing_prefix():
    digest = hmac.new(SECRET.encode("utf-8"), BODY, hashlib.sha256).hexdigest()
    assert verify_signature(BODY, SECRET, digest) is False
