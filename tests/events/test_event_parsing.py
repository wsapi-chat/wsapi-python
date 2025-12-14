"""
Tests for event parsing functionality.

These tests verify that the parse_event function correctly parses
webhook events into their corresponding event models.
"""
import json
import pytest
from wsapi_client.events.factory import parse_event
from wsapi_client.models.events.messages.message_event import MessageEvent
from wsapi_client.models.events.messages.message_read_event import MessageReadEvent
from wsapi_client.models.events.messages.message_delete_event import MessageDeleteEvent
from wsapi_client.models.events.messages.message_star_event import MessageStarEvent
from wsapi_client.models.events.session.session_logged_in_event import SessionLoggedInEvent
from wsapi_client.models.events.session.session_logged_out_event import SessionLoggedOutEvent
from wsapi_client.models.events.session.session_logged_error_event import SessionLoggedErrorEvent
from wsapi_client.models.events.calls.call_offer_event import CallOfferEvent
from wsapi_client.models.events.calls.call_accept_event import CallAcceptEvent
from wsapi_client.models.events.calls.call_terminate_event import CallTerminateEvent
from wsapi_client.models.events.chats.chat_presence_event import ChatPresenceEvent
from wsapi_client.models.events.chats.chat_setting_event import ChatSettingEvent
from wsapi_client.models.events.chats.chat_push_name_event import ChatPushNameEvent
from wsapi_client.models.events.chats.chat_status_event import ChatStatusEvent
from wsapi_client.models.events.chats.chat_picture_event import ChatPictureEvent
from wsapi_client.models.events.contacts.contact_event import ContactEvent
from wsapi_client.models.events.groups.group_event import GroupEvent
from wsapi_client.models.events.users.user_presence_event import UserPresenceEvent


def make_event(event_type: str, event_data: dict) -> str:
    """Helper to create a properly formatted event JSON."""
    return json.dumps({
        "instanceId": "test-instance",
        "receivedAt": "2025-01-01T12:00:00Z",
        "eventType": event_type,
        "eventData": event_data
    })


class TestMessageEvents:
    """Tests for message-related events."""

    def test_parse_message_event(self):
        """Test parsing a text message event."""
        event_json = make_event("message", {
            "id": "msg_123",
            "chatId": "1234567890@s.whatsapp.net",
            "sender": {"id": "1234567890@s.whatsapp.net", "isMe": False},
            "senderName": "John Doe",
            "time": "2025-01-01T12:00:00Z",
            "isGroup": False,
            "isStatus": False,
            "expiration": "0",
            "type": "text",
            "text": "Hello, World!"
        })

        event = parse_event(event_json)

        assert isinstance(event, MessageEvent)
        assert event.id == "msg_123"
        assert event.chat_id == "1234567890@s.whatsapp.net"
        assert event.sender.id == "1234567890@s.whatsapp.net"
        assert event.text == "Hello, World!"
        assert event.type == "text"

    def test_parse_message_with_mentions(self):
        """Test parsing a message with mentions."""
        event_json = make_event("message", {
            "id": "msg_456",
            "chatId": "group@g.us",
            "sender": {"id": "1234567890@s.whatsapp.net"},
            "senderName": "John",
            "time": "2025-01-01T12:00:00Z",
            "isGroup": True,
            "isStatus": False,
            "expiration": "0",
            "type": "text",
            "text": "Hey @everyone!",
            "mentions": ["9876543210@s.whatsapp.net"]
        })

        event = parse_event(event_json)

        assert isinstance(event, MessageEvent)
        assert event.is_group is True
        assert event.mentions == ["9876543210@s.whatsapp.net"]

    def test_parse_message_read_event(self):
        """Test parsing a message read event."""
        event_json = make_event("message_read", {
            "chatId": "1234567890@s.whatsapp.net",
            "sender": {"id": "1234567890@s.whatsapp.net"},
            "time": "2025-01-01T12:05:00Z",
            "isGroup": False,
            "isFromMe": False,
            "messageSender": {"id": "9876543210@s.whatsapp.net"},
            "receiptType": "read",
            "messageIds": ["msg_789"]
        })

        event = parse_event(event_json)

        assert isinstance(event, MessageReadEvent)
        assert event.chat_id == "1234567890@s.whatsapp.net"

    def test_parse_message_delete_event(self):
        """Test parsing a message delete event."""
        event_json = make_event("message_delete", {
            "id": "msg_del_123",
            "chatId": "1234567890@s.whatsapp.net",
            "sender": {"id": "1234567890@s.whatsapp.net"},
            "senderName": "John Doe",
            "time": "2025-01-01T12:00:00Z",
            "isFromMe": False,
            "isDeletedForMe": True,
            "isDeletedForAll": False,
            "isStatus": False
        })

        event = parse_event(event_json)

        assert isinstance(event, MessageDeleteEvent)
        assert event.id == "msg_del_123"

    def test_parse_message_star_event(self):
        """Test parsing a message star event."""
        event_json = make_event("message_star", {
            "id": "msg_star_123",
            "chatId": "1234567890@s.whatsapp.net",
            "sender": {"id": "1234567890@s.whatsapp.net"},
            "time": "2025-01-01T12:00:00Z",
            "isStarred": True
        })

        event = parse_event(event_json)

        assert isinstance(event, MessageStarEvent)
        assert event.id == "msg_star_123"


class TestSessionEvents:
    """Tests for session-related events."""

    def test_parse_logged_in_event(self):
        """Test parsing a logged in event."""
        event_json = make_event("logged_in", {
            "deviceId": "device_123"
        })

        event = parse_event(event_json)

        assert isinstance(event, SessionLoggedInEvent)
        assert event.device_id == "device_123"

    def test_parse_logged_out_event(self):
        """Test parsing a logged out event."""
        event_json = make_event("logged_out", {
            "reason": "user_initiated"
        })

        event = parse_event(event_json)

        assert isinstance(event, SessionLoggedOutEvent)

    def test_parse_logged_error_event(self):
        """Test parsing a logged error event."""
        event_json = make_event("logged_error", {
            "deviceId": "device_123",
            "error": "connection_failed"
        })

        event = parse_event(event_json)

        assert isinstance(event, SessionLoggedErrorEvent)
        assert event.error == "connection_failed"


class TestCallEvents:
    """Tests for call-related events."""

    def test_parse_call_offer_event(self):
        """Test parsing a call offer event."""
        event_json = make_event("call_offer", {
            "id": "call_123",
            "caller": "1234567890@s.whatsapp.net",
            "chatId": "1234567890@s.whatsapp.net",
            "isGroup": False,
            "time": "2025-01-01T12:00:00Z",
            "isVideo": True
        })

        event = parse_event(event_json)

        assert isinstance(event, CallOfferEvent)
        assert event.id == "call_123"
        assert event.caller == "1234567890@s.whatsapp.net"
        assert event.is_video is True

    def test_parse_call_accept_event(self):
        """Test parsing a call accept event."""
        event_json = make_event("call_accept", {
            "id": "call_456",
            "caller": "1234567890@s.whatsapp.net",
            "chatId": "1234567890@s.whatsapp.net",
            "isGroup": False,
            "time": "2025-01-01T12:00:00Z",
            "isVideo": False
        })

        event = parse_event(event_json)

        assert isinstance(event, CallAcceptEvent)
        assert event.id == "call_456"

    def test_parse_call_terminate_event(self):
        """Test parsing a call terminate event."""
        event_json = make_event("call_terminate", {
            "id": "call_789",
            "caller": "1234567890@s.whatsapp.net",
            "chatId": "1234567890@s.whatsapp.net",
            "isGroup": False,
            "time": "2025-01-01T12:00:00Z",
            "reason": "user_hangup"
        })

        event = parse_event(event_json)

        assert isinstance(event, CallTerminateEvent)


class TestChatEvents:
    """Tests for chat-related events."""

    def test_parse_chat_presence_event(self):
        """Test parsing a chat presence event."""
        event_json = make_event("chat_presence", {
            "id": "1234567890@s.whatsapp.net",
            "sender": {"id": "1234567890@s.whatsapp.net"},
            "isFromMe": False,
            "state": "typing"
        })

        event = parse_event(event_json)

        assert isinstance(event, ChatPresenceEvent)
        assert event.id == "1234567890@s.whatsapp.net"
        assert event.state == "typing"

    def test_parse_chat_setting_event(self):
        """Test parsing a chat setting event."""
        event_json = make_event("chat_setting", {
            "id": "1234567890@s.whatsapp.net",
            "settingType": "mute"
        })

        event = parse_event(event_json)

        assert isinstance(event, ChatSettingEvent)
        assert event.setting_type == "mute"


class TestContactEvents:
    """Tests for contact-related events."""

    def test_parse_contact_event(self):
        """Test parsing a contact event."""
        event_json = make_event("contact", {
            "id": "1234567890@s.whatsapp.net",
            "fullName": "John Doe",
            "inPhoneAddressBook": True
        })

        event = parse_event(event_json)

        assert isinstance(event, ContactEvent)
        assert event.id == "1234567890@s.whatsapp.net"
        assert event.full_name == "John Doe"
        assert event.in_phone_address_book is True


class TestGroupEvents:
    """Tests for group-related events."""

    def test_parse_group_event(self):
        """Test parsing a group event."""
        event_json = make_event("group", {
            "id": "group123@g.us",
            "sender": {"id": "1234567890@s.whatsapp.net"}
        })

        event = parse_event(event_json)

        assert isinstance(event, GroupEvent)
        assert event.id == "group123@g.us"

    def test_parse_group_event_with_description(self):
        """Test parsing a group event with description change."""
        event_json = make_event("group", {
            "id": "group456@g.us",
            "sender": {"id": "1234567890@s.whatsapp.net"},
            "description": {
                "topic": "New group topic",
                "timestamp": "2025-01-01T12:00:00Z"
            }
        })

        event = parse_event(event_json)

        assert isinstance(event, GroupEvent)
        assert event.description is not None
        assert event.description.topic == "New group topic"


class TestUserEvents:
    """Tests for user-related events (as defined in OpenAPI spec)."""

    def test_parse_user_presence_event(self):
        """Test parsing a user presence event."""
        event_json = make_event("user_presence", {
            "id": "1234567890@s.whatsapp.net",
            "status": "available",
            "lastSeen": "2025-01-01T12:00:00Z"
        })

        event = parse_event(event_json)

        assert isinstance(event, UserPresenceEvent)
        assert event.status == "available"

    def test_parse_chat_push_name_event(self):
        """Test parsing chat_push_name which maps to ChatPushNameEvent."""
        event_json = make_event("chat_push_name", {
            "id": "1234567890@s.whatsapp.net",
            "pushName": "Johnny"
        })

        event = parse_event(event_json)

        assert isinstance(event, ChatPushNameEvent)
        assert event.push_name == "Johnny"

    def test_parse_chat_status_event(self):
        """Test parsing chat_status which maps to ChatStatusEvent."""
        event_json = make_event("chat_status", {
            "id": "1234567890@s.whatsapp.net",
            "status": "Busy"
        })

        event = parse_event(event_json)

        assert isinstance(event, ChatStatusEvent)
        assert event.status == "Busy"

    def test_parse_chat_picture_event(self):
        """Test parsing chat_picture which maps to ChatPictureEvent."""
        event_json = make_event("chat_picture", {
            "id": "1234567890@s.whatsapp.net",
            "sender": {"id": "1234567890@s.whatsapp.net"},
            "pictureId": "pic_456"
        })

        event = parse_event(event_json)

        assert isinstance(event, ChatPictureEvent)
        assert event.picture_id == "pic_456"


class TestEventParsingErrors:
    """Tests for event parsing error handling."""

    def test_empty_json_raises_error(self):
        """Test that empty JSON raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            parse_event("")

    def test_missing_instance_id_raises_error(self):
        """Test that missing instanceId raises ValueError."""
        event_json = json.dumps({
            "receivedAt": "2025-01-01T12:00:00Z",
            "eventType": "message",
            "eventData": {}
        })

        with pytest.raises(ValueError, match="Missing required event fields"):
            parse_event(event_json)

    def test_missing_event_type_raises_error(self):
        """Test that missing eventType raises ValueError."""
        event_json = json.dumps({
            "instanceId": "test",
            "receivedAt": "2025-01-01T12:00:00Z",
            "eventData": {}
        })

        with pytest.raises(ValueError, match="Missing required event fields"):
            parse_event(event_json)

    def test_unknown_event_type_raises_error(self):
        """Test that unknown eventType raises ValueError."""
        event_json = json.dumps({
            "instanceId": "test",
            "receivedAt": "2025-01-01T12:00:00Z",
            "eventType": "unknown_event_type",
            "eventData": {}
        })

        with pytest.raises(ValueError, match="Unknown event type"):
            parse_event(event_json)

    def test_invalid_json_raises_error(self):
        """Test that invalid JSON raises error."""
        with pytest.raises(Exception):
            parse_event("not valid json")
