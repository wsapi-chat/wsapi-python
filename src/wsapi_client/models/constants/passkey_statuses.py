from __future__ import annotations


class PasskeyStatuses:
    """Values of ``PasskeyState.status`` and ``SessionStatus.passkey_status``."""

    NONE = "none"
    REQUIRED = "required"
    SUBMITTED = "submitted"
    CONFIRMATION_REQUIRED = "confirmation_required"
    ERROR = "error"

    #: While the status is one of these, stop polling the QR and pair-code endpoints (they return 409).
    PENDING = frozenset({REQUIRED, SUBMITTED, CONFIRMATION_REQUIRED})


class PasskeySources:
    """Values of ``PasskeyState.source``."""

    NOTIFICATION = "notification"
    REQUESTED = "requested"
