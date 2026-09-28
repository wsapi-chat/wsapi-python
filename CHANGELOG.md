# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [3.0.0]

Breaking changes: invite-info follows GroupInfoResponse, join-link returns the created ID, and join-invite returns None. Consumers of the previous return types and invite-info fields must be updated. Development installs and builds now run from the repository root.

Moved packaging configuration to the repository root so source distributions and wheels build correctly; development installs now use `pip install -e ".[test]"` from the root. Message requests use JSON-mode serialization, including legacy datetime timestamps.

Corrected user, contact, chat, community, newsletter and media routes for normal and Try calls. Query parameters are URL encoded; instance creation accepts an optional name. Legacy message request imports accept old constructor keywords but serialize canonical REST fields; prefer the models exported by `models.requests.messages`. Invite info follows GroupInfoResponse; join-link returns its ID and join-invite returns None (204). Privacy updates/history flush retain response objects. Added context-manager support, event exports, optional ad referral (including history), and reply text.

## [1.0.10] - 2025-05-30

### Added

- Communities API client for managing WhatsApp communities
- Newsletters API client for channel management
- Status API client for posting and managing status updates

### Fixed

- Several bug fixes across existing clients
- Group events and operations improvements

## [1.0.3] - 2025-04-15

### Added

- Initial SDK release
- Messages API client (text, image, video, document, audio, sticker, location, contact, poll, reaction, reply)
- Contacts API client
- Groups API client
- Chats API client
- Users API client
- Calls API client
- Media API client
- Instance API client
- Account API client
- Session API client
- SSE client for real-time event streaming with auto-reconnect
- Webhook support via Flask integration
- Dual API pattern: exception-based and try-based methods
- Pydantic v2 models for all requests, responses, and events
- Event factory for typed event deserialization
