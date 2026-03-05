from __future__ import annotations

from ..http import ApiResponse, WSApiHttp
from ..models.entities.messages.message_created import MessageCreated
from ..models.requests.messages import (
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


class MessagesClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    # Standard methods
    def send_text(self, req: MessageSendTextRequest) -> MessageCreated:
        return self._http.send_json("POST", "messages/text", model=MessageCreated, json=req.model_dump(by_alias=True))

    def send_image(self, req: SendMediaRequest) -> MessageCreated:
        return self._http.send_json("POST", "messages/image", model=MessageCreated, json=req.model_dump(by_alias=True))

    def send_video(self, req: SendMediaRequest) -> MessageCreated:
        return self._http.send_json("POST", "messages/video", model=MessageCreated, json=req.model_dump(by_alias=True))

    def send_audio(self, req: SendMediaRequest) -> MessageCreated:
        return self._http.send_json("POST", "messages/audio", model=MessageCreated, json=req.model_dump(by_alias=True))

    def send_voice(self, req: SendMediaRequest) -> MessageCreated:
        return self._http.send_json("POST", "messages/voice", model=MessageCreated, json=req.model_dump(by_alias=True))

    def send_sticker(self, req: SendStickerRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", "messages/sticker", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def send_document(self, req: SendDocumentRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", "messages/document", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def send_contact(self, req: SendContactRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", "messages/contact", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def send_location(self, req: SendLocationRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", "messages/location", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def send_link(self, req: SendLinkRequest) -> MessageCreated:
        return self._http.send_json("POST", "messages/link", model=MessageCreated, json=req.model_dump(by_alias=True))

    def send_reaction(self, message_id: str, req: SendReactionRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", f"messages/{message_id}/reaction", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def edit_text(self, message_id: str, req: EditMessageRequest) -> MessageCreated:
        return self._http.send_json(
            "POST", f"messages/{message_id}/edit", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def mark_as_read(self, message_id: str, req: MarkAsReadRequest) -> None:
        self._http.send_json("POST", f"messages/{message_id}/read", model=None, json=req.model_dump(by_alias=True))

    def star(self, message_id: str, req: StarMessageRequest) -> None:
        self._http.send_json("POST", f"messages/{message_id}/star", model=None, json=req.model_dump(by_alias=True))

    def delete(self, message_id: str, req: DeleteMessageRequest) -> None:
        self._http.send_json("POST", f"messages/{message_id}/delete", model=None, json=req.model_dump(by_alias=True))

    def delete_for_me(self, message_id: str, req: DeleteMessageForMeRequest) -> None:
        self._http.send_json(
            "POST", f"messages/{message_id}/delete-for-me", model=None, json=req.model_dump(by_alias=True)
        )

    def pin(self, message_id: str, req: PinMessageRequest) -> None:
        self._http.send_json("POST", f"messages/{message_id}/pin", model=None, json=req.model_dump(by_alias=True))

    # Try variants
    def try_send_text(self, req: MessageSendTextRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/text", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_image(self, req: SendMediaRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/image", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_video(self, req: SendMediaRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/video", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_audio(self, req: SendMediaRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/audio", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_voice(self, req: SendMediaRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/voice", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_sticker(self, req: SendStickerRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/sticker", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_document(self, req: SendDocumentRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/document", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_contact(self, req: SendContactRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/contact", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_location(self, req: SendLocationRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/location", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_link(self, req: SendLinkRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", "messages/link", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_send_reaction(self, message_id: str, req: SendReactionRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", f"messages/{message_id}/reaction", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_edit_text(self, message_id: str, req: EditMessageRequest) -> ApiResponse[MessageCreated]:
        return self._http.try_send_json(
            "POST", f"messages/{message_id}/edit", model=MessageCreated, json=req.model_dump(by_alias=True)
        )

    def try_mark_as_read(self, message_id: str, req: MarkAsReadRequest) -> ApiResponse[object]:
        return self._http.try_send_json(
            "POST", f"messages/{message_id}/read", model=None, json=req.model_dump(by_alias=True)
        )

    def try_star(self, message_id: str, req: StarMessageRequest) -> ApiResponse[object]:
        return self._http.try_send_json(
            "POST", f"messages/{message_id}/star", model=None, json=req.model_dump(by_alias=True)
        )

    def try_delete(self, message_id: str, req: DeleteMessageRequest) -> ApiResponse[object]:
        return self._http.try_send_json(
            "POST", f"messages/{message_id}/delete", model=None, json=req.model_dump(by_alias=True)
        )

    def try_delete_for_me(self, message_id: str, req: DeleteMessageForMeRequest) -> ApiResponse[object]:
        return self._http.try_send_json(
            "POST", f"messages/{message_id}/delete-for-me", model=None, json=req.model_dump(by_alias=True)
        )

    def try_pin(self, message_id: str, req: PinMessageRequest) -> ApiResponse[object]:
        return self._http.try_send_json(
            "POST", f"messages/{message_id}/pin", model=None, json=req.model_dump(by_alias=True)
        )
