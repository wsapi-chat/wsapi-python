# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

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
