"""
Flask webhook test server for testing event parsing.

This server receives webhook events and uses the wsapi_client library
to parse and validate them.

Usage:
    cd wsapi-python
    pip install -e ".[webhook]"
    python webhook/app.py

The server will listen on http://localhost:5000/webhook
"""
from flask import Flask, request, jsonify
import json
import sys
import os

# Add the src directory to the path so we can import wsapi_client
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from wsapi_client.events.factory import parse_event

app = Flask(__name__)

# Store received events for inspection
received_events = []


@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint that receives and parses events.

    The endpoint expects a JSON body with the structure:
    {
        "instanceId": "...",
        "receivedAt": "...",
        "eventType": "...",
        "eventData": {...}
    }
    """
    try:
        raw_json = request.get_data(as_text=True)

        # Parse the event using the library
        event = parse_event(raw_json)

        # Store for inspection
        received_events.append({
            "raw": json.loads(raw_json),
            "parsed": event,
            "event_type": type(event).__name__
        })

        print(f"Received event: {type(event).__name__}")

        return jsonify({
            "status": "ok",
            "event_type": type(event).__name__,
            "message": "Event parsed successfully"
        }), 200

    except ValueError as e:
        print(f"Parse error: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route('/events', methods=['GET'])
def list_events():
    """List all received events."""
    return jsonify({
        "count": len(received_events),
        "events": [
            {
                "event_type": e["event_type"],
                "raw_event_type": e["raw"].get("eventType")
            }
            for e in received_events
        ]
    })


@app.route('/events/clear', methods=['POST'])
def clear_events():
    """Clear all received events."""
    received_events.clear()
    return jsonify({"status": "ok", "message": "Events cleared"})


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})


if __name__ == '__main__':
    print("Starting webhook test server...")
    print("Webhook endpoint: http://localhost:5000/webhook")
    print("List events: http://localhost:5000/events")
    print("Clear events: POST http://localhost:5000/events/clear")
    print("Health check: http://localhost:5000/health")
    app.run(debug=True, port=5000)
