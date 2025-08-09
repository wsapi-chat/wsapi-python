# WSApi Python SDK

A Python SDK for integrating with the WSApi platform. Send WhatsApp messages, manage chats/contacts, and receive real-time events via webhooks or Server‑Sent Events (SSE).

## Features

- **HTTP Client**: Simple, typed models (Pydantic v2) for all API operations
- **Dual API Pattern**: Exception-based and `try_` methods for error handling
- **Resource Clients**: Messages, Instance, Media, Contacts, Groups, Chats, Users, Calls
- **Event Handling**: Webhooks and SSE client for real-time events with parsed models

---

## Getting Started

### Prerequisites
- Python 3.9+ (as specified in pyproject.toml)
- WSApi instance credentials (API Key and Instance Id)

### Installation

**From PyPI (recommended):**

```bash
pip install wsapi-client
```

📦 **Package page:** https://pypi.org/project/wsapi-client/

**From source (development):**

1) Clone this repository
2) Create and activate a virtual environment (recommended)
3) Install in editable mode:

```bash
pip install -e .
```

**Dependencies:** httpx, pydantic (automatically installed)

---

# 🔧 API Client Usage

## Basic Client Setup

```python
from wsapi_client import WSApiClient, ApiException
from wsapi_client.models.requests.messages import MessageSendTextRequest

client = WSApiClient(api_key="<your-api-key>", instance_id="<instance-id>")
```

## Sending Messages

```python
req = MessageSendTextRequest(to="1234567890@s.whatsapp.net", text="Hello from Python!")

# Style 1: Exception-based (raises on error)
try:
    created = client.messages.send_text(req)
    print("Message id:", created.id)
except ApiException as ex:
    # ProblemDetails available via ex.problem
    print("Send failed:", ex.problem.detail)

# Style 2: ApiResponse-based (never raises)
resp = client.messages.try_send_text(req)
if resp.is_success and resp.result:
    print("Message id:", resp.result.id)
else:
    print("Send failed:", resp.error.detail if resp.error else "unknown error")

client.close()
```

## Other API Operations

```python
# Users
user = client.users.get_by_id("5511999999999")  # Just phone number for user lookup
print(user.status)

# Instance settings
settings = client.instance.get_settings()
print(f"Instance: {settings.name}")

# Calls (reject)
from wsapi_client.models.requests.calls import RejectCallRequest
client.calls.reject("call_123", RejectCallRequest(caller="+15551234567"))
```

## Client Reference

### `WSApiClient` Resources:

- **`messages`**: send text/image/video/audio/voice/sticker/document/contact/location/link/reaction, edit_text; mark_as_read, star, delete, delete_for_me
- **`instance`**: get settings, etc.
- **`media`**: download files
- **`contacts`**: contact management operations
- **`groups`**: group management operations  
- **`chats`**: chat management operations
- **`users`**: get_by_id/try_get_by_id
- **`calls`**: reject/try_reject

### ApiResponse[T] Pattern

Each method has an exception-based and a `try_` variant:

- **`result: T | None`** — data when successful
- **`error: ProblemDetails | None`** — error when not successful  
- **`is_success: bool`** — convenience flag

### Important Notes

- **Close the client** when you're done: `client.close()`
- **No-content endpoints** (204) return `None` on success
- **Models use Pydantic v2** with aliases to match WSApi's JSON
- **Timeouts and transport errors** are surfaced as `ApiException` (exception path) or as `ProblemDetails` with status 408/500 in `ApiResponse` (try_ path)

---

# 📡 Event Handling

There are two ways to receive real-time events from the WSApi: **Webhooks** (recommended) and **Server-Sent Events (SSE)**.

## Option 1: Webhooks (Recommended)

Configure a webhook endpoint in your WSApi instance settings to receive events via HTTP POST requests. This is the most reliable and scalable approach.

### Setup Process:
1. Configure webhook URL and optional auth header in your WSApi instance settings
2. Create an endpoint in your web application to receive events
3. Use the same event parsing functionality as SSE

### Example using Flask:

```python
from flask import Flask, request, jsonify
from wsapi_client.events.factory import parse_event
from wsapi_client.models.events.messages import MessageEvent

app = Flask(__name__)

# Configure this in your WSApi instance settings
WEBHOOK_AUTH_TOKEN = "your-secret-token"

@app.route('/wsapi/webhook', methods=['POST'])
def handle_webhook():
    # Optional: Verify auth header if configured
    auth_header = request.headers.get('X-Webhook-Auth')  # or your configured header name
    if auth_header != WEBHOOK_AUTH_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        # Get the raw JSON event
        raw_event = request.get_json()
        
        # Parse using the same factory as SSE client
        parsed_event = parse_event(request.get_data(as_text=True))
        
        # Handle the event based on type
        if isinstance(parsed_event, MessageEvent) and parsed_event.text:
            print(f"[webhook] New message from {parsed_event.sender_name}: {parsed_event.text}")
            
            # Example: Auto-reply to messages
            # client = WSApiClient(api_key="...", instance_id="...")
            # client.messages.send_text(MessageSendTextRequest(
            #     to=parsed_event.chat_id, 
            #     text="Thanks for your message!"
            # ))
        
        return jsonify({"status": "success"}), 200
        
    except Exception as e:
        print(f"[webhook] Error processing event: {e}")
        return jsonify({"error": "Processing failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Example using FastAPI:

```python
from fastapi import FastAPI, Request, HTTPException, Header
from wsapi_client.events.factory import parse_event
from wsapi_client.models.events.messages import MessageEvent
from typing import Optional

app = FastAPI()

WEBHOOK_AUTH_TOKEN = "your-secret-token"

@app.post("/wsapi/webhook")
async def handle_webhook(
    request: Request,
    x_webhook_auth: Optional[str] = Header(None)  # Adjust header name as configured
):
    # Optional: Verify auth header if configured
    if x_webhook_auth != WEBHOOK_AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    try:
        # Get raw JSON body
        body = await request.body()
        
        # Parse the event
        parsed_event = parse_event(body.decode('utf-8'))
        
        # Handle different event types
        if isinstance(parsed_event, MessageEvent) and parsed_event.text:
            print(f"[webhook] New message: {parsed_event.text}")
            # Process message...
        
        return {"status": "success"}
        
    except Exception as e:
        print(f"[webhook] Error: {e}")
        raise HTTPException(status_code=500, detail="Processing failed")
```

## Option 2: Server-Sent Events (SSE)

For scenarios where webhooks aren't suitable, use the built-in SSE client for a persistent connection.

```python
from wsapi_client import SSEClient, SSEConnectionState
from wsapi_client.models.events.messages import MessageEvent

sse = SSEClient(api_key="<your-api-key>", instance_id="<instance-id>")

def on_event(evt):
    # evt is one of the typed event models (e.g., MessageEvent)
    if isinstance(evt, MessageEvent) and evt.text:
        print("[sse]", evt.sender_name, ":", evt.text)

def on_state(state, exc):
    print("[sse] Connection state:", state)
    if exc:
        print("[sse] Error:", exc)

sse.on_event = on_event
sse.on_connection_state_changed = on_state
sse.start()

# ... later
sse.stop()
```

## Available Event Types

Both webhook and SSE approaches support the same event types:

- **Session**: `SessionLoggedInEvent`, `SessionLoggedOutEvent`, `SessionLoggedErrorEvent`
- **Messages**: `MessageEvent`, `MessageDeleteEvent`, `MessageReadEvent`, `MessageStarEvent`, `MessageHistorySyncEvent`
- **Chats**: `ChatPresenceEvent`, `ChatSettingEvent`
- **Contacts**: `ContactEvent`
- **Users**: `UserPushNameEvent`, `UserPictureEvent`, `UserPresenceEvent`, `UserStatusEvent`
- **Calls**: `CallOfferEvent`, `CallAcceptEvent`, `CallTerminateEvent`

All events are parsed by `wsapi_client.events.factory.parse_event` which converts raw JSON into strongly-typed Python objects.

---

## Troubleshooting

- If you see JSON parsing errors, confirm the SDK version matches the WSApi server you're targeting.
- For webhook issues, check that your endpoint is accessible and returns proper HTTP status codes.
- For SSE connection issues, verify your API credentials and network connectivity.
