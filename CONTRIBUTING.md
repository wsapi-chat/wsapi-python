# Contributing to wsapi-python

Thank you for your interest in contributing! This guide will help you get started.

## Prerequisites

- Python 3.9 or later
- pip
- git

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/wsapi-python.git
   cd wsapi-python
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```
4. **Install in development mode**:
   ```bash
   pip install -e "./src[dev]"
   ```
5. **Create a feature branch**:
   ```bash
   git checkout -b feat/my-feature
   ```

## Development Workflow

| Task | Command |
|------|---------|
| Run tests | `pytest tests/` |
| Run a single test file | `pytest tests/api/test_messages.py` |
| Run a specific test | `pytest tests/api/test_messages.py::test_send_text_success -v` |
| Lint check | `ruff check src/ tests/` |
| Auto-fix lint issues | `ruff check --fix src/ tests/` |
| Format check | `ruff format --check src/ tests/` |
| Auto-format | `ruff format src/ tests/` |
| Build package | `python -m build src/` |

## Project Structure

| Path | Description |
|------|-------------|
| `src/wsapi_client/client.py` | Main `WSApiClient` class aggregating all resource clients |
| `src/wsapi_client/http.py` | HTTP transport layer (httpx); `ApiResponse[T]` for try_ methods |
| `src/wsapi_client/exceptions.py` | `ApiException` wrapping `ProblemDetails` |
| `src/wsapi_client/api/` | Resource clients (messages, contacts, groups, chats, etc.) |
| `src/wsapi_client/models/requests/` | Request DTOs |
| `src/wsapi_client/models/entities/` | Response/domain models |
| `src/wsapi_client/models/events/` | Webhook/SSE event models |
| `src/wsapi_client/models/constants/` | Enums (event types, message types, presence) |
| `src/wsapi_client/events/factory.py` | `parse_event()` — JSON to typed event models |
| `src/wsapi_client/sse/client.py` | `SSEClient` for real-time event streaming |
| `tests/` | Test suite (pytest + mock HTTP clients) |

## Key Patterns

### Client Composition

`WSApiClient` composes resource-specific clients (`.messages`, `.contacts`, `.groups`, etc.), each backed by a shared HTTP client.

### Dual API Pattern

Every resource method has two variants:
- **Exception-based**: `send_text(req)` — raises `ApiException` on error
- **Try-based**: `try_send_text(req)` — returns `ApiResponse[T]` with `.result`, `.error`, `.is_success`

### Event Factory

`parse_event()` in `events/factory.py` maps `eventType` strings to typed Pydantic models for both webhook and SSE event handling.

### Pydantic v2

All models use Pydantic v2 with `model_config = ConfigDict(populate_by_name=True)` and `Field(alias=...)` for JSON serialization.

## Where to Add Features

| Feature | Where |
|---------|-------|
| New API endpoint | Add method to existing client in `src/wsapi_client/api/` |
| New resource client | Create file in `api/`, add to `WSApiClient` in `client.py` |
| New request/response model | Add to `models/requests/` or `models/entities/` |
| New event type | Add model in `models/events/`, register in `events/factory.py` |
| New enum/constant | Add to `models/constants/` |

## Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add support for polls API
fix: handle empty response body in media download
docs: update CHANGELOG for v1.0.10
test: add coverage for group admin operations
chore: update ruff to 0.9.0
```

## Pull Request Checklist

- [ ] Code follows existing patterns and conventions
- [ ] All tests pass (`pytest tests/`)
- [ ] Linter passes (`ruff check src/ tests/`)
- [ ] Formatter passes (`ruff format --check src/ tests/`)
- [ ] New features include tests
- [ ] CHANGELOG.md is updated (if applicable)
- [ ] Commit messages follow Conventional Commits format
