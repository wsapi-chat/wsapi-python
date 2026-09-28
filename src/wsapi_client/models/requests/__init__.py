"""All request models, importable from one place.

    from wsapi_client.models import MessageSendTextRequest

The per-module paths keep working.
"""

from .account import (
    UpdateInstanceNameRequest,
)
from .calls.reject_call_request import (
    RejectCallRequest,
)
from .chats import (
    ChatUpdateArchiveRequest,
    ChatUpdateEphemeralExpirationRequest,
    ChatUpdateMuteRequest,
    ChatUpdatePinRequest,
    ChatUpdatePresenceRequest,
    ChatUpdateReadRequest,
)
from .chats.request_messages_request import (
    RequestMessagesRequest,
)
from .communities.community_requests import (
    CreateCommunityGroupRequest,
    CreateCommunityRequest,
    LinkGroupRequest,
)
from .contacts.contact_create_request import (
    ContactCreateRequest,
)
from .groups import (
    GroupCreateRequest,
    GroupJoinWithInviteRequest,
    GroupJoinWithLinkRequest,
    GroupSetAnnounceRequest,
    GroupSetJoinApprovalRequest,
    GroupSetLockedRequest,
    GroupSetMemberAddModeRequest,
    GroupUpdateDescriptionRequest,
    GroupUpdateNameRequest,
    GroupUpdateParticipantsRequest,
    GroupUpdatePictureRequest,
    GroupUpdateRequestParticipantsRequest,
    GroupUpdateRequestsRequest,
)
from .groups.group_participant_request import (
    GroupParticipantRequest,
)
from .media.media_download_request import (
    MediaDownloadRequest,
)
from .messages import (
    DeleteMessageForMeRequest,
    DeleteMessageRequest,
    EditMessageRequest,
    MarkAsReadRequest,
    MessageRequestBase,
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
from .messages.message_delete_for_me_request import (
    MessageDeleteForMeRequest,
)
from .messages.message_delete_request import (
    MessageDeleteRequest,
)
from .messages.message_mark_as_read_request import (
    MessageMarkAsReadRequest,
)
from .messages.message_send_audio_request import (
    MessageSendAudioRequest,
)
from .messages.message_send_contact_request import (
    MessageSendContactRequest,
)
from .messages.message_send_document_request import (
    MessageSendDocumentRequest,
)
from .messages.message_send_image_request import (
    MessageSendImageRequest,
)
from .messages.message_send_link_request import (
    MessageSendLinkRequest,
)
from .messages.message_send_location_request import (
    MessageSendLocationRequest,
)
from .messages.message_send_reaction_request import (
    MessageSendReactionRequest,
)
from .messages.message_send_sticker_request import (
    MessageSendStickerRequest,
)
from .messages.message_send_video_request import (
    MessageSendVideoRequest,
)
from .messages.message_send_voice_request import (
    MessageSendVoiceRequest,
)
from .messages.message_star_request import (
    MessageStarRequest,
)
from .newsletters.newsletter_requests import (
    CreateNewsletterRequest,
    SetSubscriptionRequest,
    ToggleMuteNewsletterRequest,
)
from .status.status_requests import (
    PostMediaStatusRequest,
    PostTextStatusRequest,
)
from .users.bulk_check_request import (
    BulkCheckRequest,
)
from .users.set_presence_request import (
    SetMyPresenceRequest,
)
from .users.set_privacy_request import (
    SetPrivacyRequest,
)
from .users.update_profile_request import (
    UpdateProfileRequest,
)

__all__ = [
    "BulkCheckRequest",
    "ChatUpdateArchiveRequest",
    "ChatUpdateEphemeralExpirationRequest",
    "ChatUpdateMuteRequest",
    "ChatUpdatePinRequest",
    "ChatUpdatePresenceRequest",
    "ChatUpdateReadRequest",
    "ContactCreateRequest",
    "CreateCommunityGroupRequest",
    "CreateCommunityRequest",
    "CreateNewsletterRequest",
    "DeleteMessageForMeRequest",
    "DeleteMessageRequest",
    "EditMessageRequest",
    "GroupCreateRequest",
    "GroupJoinWithInviteRequest",
    "GroupJoinWithLinkRequest",
    "GroupParticipantRequest",
    "GroupSetAnnounceRequest",
    "GroupSetJoinApprovalRequest",
    "GroupSetLockedRequest",
    "GroupSetMemberAddModeRequest",
    "GroupUpdateDescriptionRequest",
    "GroupUpdateNameRequest",
    "GroupUpdateParticipantsRequest",
    "GroupUpdatePictureRequest",
    "GroupUpdateRequestParticipantsRequest",
    "GroupUpdateRequestsRequest",
    "LinkGroupRequest",
    "MarkAsReadRequest",
    "MediaDownloadRequest",
    "MessageDeleteForMeRequest",
    "MessageDeleteRequest",
    "MessageMarkAsReadRequest",
    "MessageRequestBase",
    "MessageSendAudioRequest",
    "MessageSendContactRequest",
    "MessageSendDocumentRequest",
    "MessageSendImageRequest",
    "MessageSendLinkRequest",
    "MessageSendLocationRequest",
    "MessageSendReactionRequest",
    "MessageSendStickerRequest",
    "MessageSendTextRequest",
    "MessageSendVideoRequest",
    "MessageSendVoiceRequest",
    "MessageStarRequest",
    "PinMessageRequest",
    "PostMediaStatusRequest",
    "PostTextStatusRequest",
    "RejectCallRequest",
    "RequestMessagesRequest",
    "SendContactRequest",
    "SendDocumentRequest",
    "SendLinkRequest",
    "SendLocationRequest",
    "SendMediaRequest",
    "SendReactionRequest",
    "SendStickerRequest",
    "SetMyPresenceRequest",
    "SetPrivacyRequest",
    "SetSubscriptionRequest",
    "StarMessageRequest",
    "ToggleMuteNewsletterRequest",
    "UpdateInstanceNameRequest",
    "UpdateProfileRequest",
]
