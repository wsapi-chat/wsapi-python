from __future__ import annotations

import hashlib
import hmac


def verify_signature(raw_body: bytes, secret: str, signature_header: str) -> bool:
    """Verify the HMAC-SHA256 signature of a webhook payload.

    Args:
        raw_body: The raw request body bytes.
        secret: The signing secret configured for the instance.
        signature_header: The value of the X-Webhook-Signature header.

    Returns:
        True if the signature is valid, False otherwise.
    """
    if not signature_header:
        return False

    expected = "sha256=" + hmac.new(
        secret.encode("utf-8"),
        raw_body,
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(expected, signature_header)
