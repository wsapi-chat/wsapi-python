# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python SDK for WSApi, a WhatsApp messaging API. The package is published to PyPI as `wsapi-client`.

## Common Commands

```bash
# Install in development mode (from repo root)
pip install -e ./src

# Install with test dependencies
pip install -e "./src[test]"

# Run all tests
pytest tests/

# Run a single test file
pytest tests/api/test_messages.py

# Run a specific test
pytest tests/api/test_messages.py::test_send_text_success -v

# Build package
cd src && python -m build
```

## Architecture

### Package Structure (`src/wsapi_client/`)

- **`client.py`** - Main `WSApiClient` class that aggregates all resource clients
- **`http.py`** - HTTP transport layer using httpx; defines `ApiResponse[T]` dataclass for try_ methods
- **`exceptions.py`** - `ApiException` wrapping `ProblemDetails`
- **`api/`** - Resource clients (messages, contacts, groups, chats, users, calls, media, instance, account, session)
- **`models/`** - Pydantic v2 models organized by:
  - `requests/` - Request DTOs
  - `entities/` - Response/domain models
  - `events/` - Webhook/SSE event models
  - `constants/` - Enums for event types, message types, presence statuses
- **`events/factory.py`** - `parse_event()` function that deserializes JSON to typed event models
- **`webhooks.py`** - `verify_signature()` for HMAC-SHA256 webhook signature verification
- **`sse/client.py`** - `SSEClient` for real-time event streaming

### Dual API Pattern

Each resource client method has two variants:
- **Exception-based**: `send_text(req)` - raises `ApiException` on error
- **Try-based**: `try_send_text(req)` - returns `ApiResponse[T]` with `.result`, `.error`, `.is_success`

### Key Types

- `WSApiClient` - Main entry point; exposes `.messages`, `.contacts`, `.groups`, etc.
- `SSEClient` - Real-time event streaming with auto-reconnect
- `ApiResponse[T]` - Generic response wrapper for try_ methods
- `ProblemDetails` - RFC 7807 error format from the API
- `verify_signature(raw_body, secret, signature_header)` - HMAC-SHA256 webhook signature verification

### Event Handling

Events can be received via webhooks or SSE. Both use `parse_event()` from `events/factory.py` which maps `eventType` string to the appropriate typed model class (MessageEvent, GroupEvent, etc.).

## Testing

Tests use pytest with mock HTTP clients defined in `tests/conftest.py`. The `MockHttpClient` and `MockResponse` classes simulate httpx behavior without network calls.
