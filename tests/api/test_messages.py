"""
Tests for MessagesClient API methods.
"""

from wsapi_client.api.messages import MessagesClient
from wsapi_client.models.requests.messages import (
    DeleteMessageForMeRequest,
    DeleteMessageRequest,
    EditMessageRequest,
    MarkAsReadRequest,
    MessageSendTextRequest,
    PinMessageRequest,
    SendContactRequest,
    SendDocumentRequest,
    SendLinkRequest,
    SendLocationRequest,
    SendMediaRequest,
    SendReactionRequest,
    SendStickerRequest,
    StarMessageRequest,
)


class TestMessagesClient:
    """Test suite for MessagesClient."""

    def test_send_text(self, wsapi_http, sample_message_created):
        """Test sending a text message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = MessageSendTextRequest(to="1234567890@s.whatsapp.net", text="Hello, World!")
        result = client.send_text(request)

        assert result.id == "msg_123456789"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/text"
        assert call["json"]["to"] == "1234567890@s.whatsapp.net"
        assert call["json"]["text"] == "Hello, World!"

    def test_send_text_with_mentions(self, wsapi_http, sample_message_created):
        """Test sending a text message with mentions."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = MessageSendTextRequest(
            to="123456789@g.us", text="Hello @1234567890!", mentions=["1234567890@s.whatsapp.net"]
        )
        client.send_text(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["json"]["mentions"] == ["1234567890@s.whatsapp.net"]

    def test_send_text_with_reply(self, wsapi_http, sample_message_created):
        """Test sending a reply to a message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = MessageSendTextRequest(
            to="1234567890@s.whatsapp.net", text="This is a reply", reply_to="original_msg_id"
        )
        client.send_text(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["json"]["replyTo"] == "original_msg_id"

    def test_send_image_by_url(self, wsapi_http, sample_message_created):
        """Test sending an image by URL."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendMediaRequest(
            to="1234567890@s.whatsapp.net",
            url="https://example.com/image.jpg",
            mime_type="image/jpeg",
            caption="Check this out!",
        )
        client.send_image(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/image"
        assert call["json"]["url"] == "https://example.com/image.jpg"
        assert call["json"]["mimeType"] == "image/jpeg"

    def test_send_image_view_once(self, wsapi_http, sample_message_created):
        """Test sending a view-once image."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendMediaRequest(
            to="1234567890@s.whatsapp.net", data="base64encodeddata", mime_type="image/png", view_once=True
        )
        client.send_image(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["json"]["viewOnce"] is True

    def test_send_video(self, wsapi_http, sample_message_created):
        """Test sending a video message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendMediaRequest(
            to="1234567890@s.whatsapp.net",
            url="https://example.com/video.mp4",
            mime_type="video/mp4",
            caption="Watch this!",
        )
        client.send_video(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/video"

    def test_send_audio(self, wsapi_http, sample_message_created):
        """Test sending an audio message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendMediaRequest(
            to="1234567890@s.whatsapp.net", url="https://example.com/audio.mp3", mime_type="audio/mpeg"
        )
        client.send_audio(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/audio"

    def test_send_voice(self, wsapi_http, sample_message_created):
        """Test sending a voice message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendMediaRequest(
            to="1234567890@s.whatsapp.net", url="https://example.com/voice.ogg", mime_type="audio/ogg"
        )
        client.send_voice(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/voice"

    def test_send_sticker(self, wsapi_http, sample_message_created):
        """Test sending a sticker message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendStickerRequest(
            to="1234567890@s.whatsapp.net", url="https://example.com/sticker.webp", is_animated=False
        )
        client.send_sticker(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/sticker"
        assert call["json"]["url"] == "https://example.com/sticker.webp"

    def test_send_document(self, wsapi_http, sample_message_created):
        """Test sending a document message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendDocumentRequest(
            to="1234567890@s.whatsapp.net",
            url="https://example.com/report.pdf",
            filename="report.pdf",
            caption="Monthly report",
        )
        client.send_document(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/document"
        assert call["json"]["filename"] == "report.pdf"

    def test_send_contact(self, wsapi_http, sample_message_created):
        """Test sending a contact message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendContactRequest(
            to="1234567890@s.whatsapp.net",
            vcard="BEGIN:VCARD\nVERSION:3.0\nFN:Jane Doe\nEND:VCARD",
            display_name="Jane Doe",
        )
        client.send_contact(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/contact"

    def test_send_location(self, wsapi_http, sample_message_created):
        """Test sending a location message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendLocationRequest(
            to="1234567890@s.whatsapp.net",
            latitude=37.7749,
            longitude=-122.4194,
            name="San Francisco",
            address="California, USA",
        )
        client.send_location(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/location"
        assert call["json"]["latitude"] == 37.7749
        assert call["json"]["longitude"] == -122.4194

    def test_send_link(self, wsapi_http, sample_message_created):
        """Test sending a link message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendLinkRequest(
            to="1234567890@s.whatsapp.net",
            text="Check this out",
            url="https://example.com/article",
            title="Interesting Article",
            description="A great read",
        )
        client.send_link(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/link"
        assert call["json"]["url"] == "https://example.com/article"

    def test_send_reaction(self, wsapi_http, sample_message_created):
        """Test sending a reaction to a message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = SendReactionRequest(
            to="1234567890@s.whatsapp.net", sender_id="1234567890@s.whatsapp.net", reaction="\U0001f44d"
        )
        client.send_reaction("msg_original", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/msg_original/reaction"
        assert call["json"]["reaction"] == "\U0001f44d"

    def test_edit_text(self, wsapi_http, sample_message_created):
        """Test editing a text message."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = EditMessageRequest(to="1234567890@s.whatsapp.net", text="Updated message")
        client.edit_text("msg_to_edit", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/msg_to_edit/edit"

    def test_mark_as_read(self, wsapi_http):
        """Test marking a message as read."""
        wsapi_http._mock_client.set_response(204)
        client = MessagesClient(wsapi_http)

        request = MarkAsReadRequest(
            chat_id="1234567890@s.whatsapp.net", sender_id="1234567890@s.whatsapp.net", receipt_type="read"
        )
        client.mark_as_read("msg_id", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/msg_id/read"

    def test_star_message(self, wsapi_http):
        """Test starring a message."""
        wsapi_http._mock_client.set_response(204)
        client = MessagesClient(wsapi_http)

        request = StarMessageRequest(
            chat_id="1234567890@s.whatsapp.net", sender_id="1234567890@s.whatsapp.net", starred=True
        )
        client.star("msg_id", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/msg_id/star"

    def test_delete_message(self, wsapi_http):
        """Test deleting a message for everyone."""
        wsapi_http._mock_client.set_response(204)
        client = MessagesClient(wsapi_http)

        request = DeleteMessageRequest(chat_id="1234567890@s.whatsapp.net", sender_id="1234567890@s.whatsapp.net")
        client.delete("msg_id", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/msg_id/delete"

    def test_delete_message_for_me(self, wsapi_http):
        """Test deleting a message for me only."""
        wsapi_http._mock_client.set_response(204)
        client = MessagesClient(wsapi_http)

        request = DeleteMessageForMeRequest(
            chat_id="1234567890@s.whatsapp.net",
            sender_id="1234567890@s.whatsapp.net",
            is_from_me=True,
            timestamp="2025-05-19T00:51:44.816Z",
        )
        client.delete_for_me("msg_id", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/msg_id/delete-for-me"

    def test_pin_message(self, wsapi_http):
        """Test pinning a message."""
        wsapi_http._mock_client.set_response(204)
        client = MessagesClient(wsapi_http)

        request = PinMessageRequest(
            chat_id="1234567890@s.whatsapp.net", sender_id="1234567890@s.whatsapp.net", pinned=True, pin_expiration="7d"
        )
        client.pin("msg_id", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "messages/msg_id/pin"


class TestMessagesClientTryMethods:
    """Test suite for MessagesClient try_ methods."""

    def test_try_send_text_success(self, wsapi_http, sample_message_created):
        """Test try_send_text on success."""
        wsapi_http._mock_client.set_response(201, sample_message_created)
        client = MessagesClient(wsapi_http)

        request = MessageSendTextRequest(to="1234567890@s.whatsapp.net", text="Hello!")
        response = client.try_send_text(request)

        assert response.is_success
        assert response.result.id == "msg_123456789"
        assert response.error is None

    def test_try_send_text_failure(self, wsapi_http):
        """Test try_send_text on failure."""
        wsapi_http._mock_client.set_response(
            400,
            {
                "type": "https://wsapi.chat/errors/bad-request",
                "title": "Bad Request",
                "status": 400,
                "detail": "Invalid phone number format",
            },
        )
        client = MessagesClient(wsapi_http)

        request = MessageSendTextRequest(to="invalid", text="Hello!")
        response = client.try_send_text(request)

        assert not response.is_success
        assert response.result is None
        assert response.error is not None
        assert response.error.status == 400
