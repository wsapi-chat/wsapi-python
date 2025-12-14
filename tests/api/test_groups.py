"""
Tests for GroupsClient API methods.
"""
import pytest
from wsapi_client.api.groups import GroupsClient
from wsapi_client.models.requests.groups.group_create_request import GroupCreateRequest
from wsapi_client.models.requests.groups.group_update_description_request import GroupUpdateDescriptionRequest
from wsapi_client.models.requests.groups.group_update_name_request import GroupUpdateNameRequest
from wsapi_client.models.requests.groups.group_update_picture_request import GroupUpdatePictureRequest
from wsapi_client.models.requests.groups.group_update_participants_request import GroupUpdateParticipantsRequest


class TestGroupsClient:
    """Test suite for GroupsClient."""

    def test_list_groups(self, wsapi_http, sample_group_info):
        """Test listing all groups."""
        wsapi_http._mock_client.set_response(200, [sample_group_info])
        client = GroupsClient(wsapi_http)

        result = client.list()

        assert len(result) == 1
        assert result[0].id == "123456789-987654321@g.us"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/groups"

    def test_get_group(self, wsapi_http, sample_group_info):
        """Test getting a single group."""
        wsapi_http._mock_client.set_response(200, sample_group_info)
        client = GroupsClient(wsapi_http)

        result = client.get("123456789-987654321@g.us")

        assert result.id == "123456789-987654321@g.us"
        assert result.name == "Test Group"
        assert result.description == "A test group"
        assert result.picture == "https://example.com/group-pic.jpg"
        assert result.invite_link == "https://chat.whatsapp.com/ABC123"
        assert len(result.participants) == 2
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/groups/123456789-987654321@g.us"

    def test_create_group(self, wsapi_http):
        """Test creating a new group."""
        wsapi_http._mock_client.set_response(201, {"id": "new-group@g.us"})
        client = GroupsClient(wsapi_http)

        request = GroupCreateRequest(
            name="New Group",
            participants=["1234567890@s.whatsapp.net", "9876543210@s.whatsapp.net"]
        )
        result = client.create(request)

        assert result.id == "new-group@g.us"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "/groups"
        assert call["json"]["name"] == "New Group"
        assert len(call["json"]["participants"]) == 2

    def test_delete_group(self, wsapi_http):
        """Test deleting (leaving) a group."""
        wsapi_http._mock_client.set_response(204)
        client = GroupsClient(wsapi_http)

        client.delete("123456789-987654321@g.us")

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/groups/123456789-987654321@g.us/leave"

    def test_update_description(self, wsapi_http):
        """Test updating group description."""
        wsapi_http._mock_client.set_response(204)
        client = GroupsClient(wsapi_http)

        request = GroupUpdateDescriptionRequest(description="Updated description")
        client.update_description("123456789-987654321@g.us", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/groups/123456789-987654321@g.us/description"
        assert call["json"]["description"] == "Updated description"

    def test_update_name(self, wsapi_http):
        """Test updating group name."""
        wsapi_http._mock_client.set_response(204)
        client = GroupsClient(wsapi_http)

        request = GroupUpdateNameRequest(name="New Name")
        client.update_name("123456789-987654321@g.us", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/groups/123456789-987654321@g.us/name"
        assert call["json"]["name"] == "New Name"

    def test_update_picture(self, wsapi_http):
        """Test updating group picture."""
        wsapi_http._mock_client.set_response(201, {"pictureId": "pic_123"})
        client = GroupsClient(wsapi_http)

        request = GroupUpdatePictureRequest(picture_base64="base64encodedimage")
        result = client.update_picture("123456789-987654321@g.us", request)

        assert result.picture_id == "pic_123"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "/groups/123456789-987654321@g.us/picture"

    def test_get_invite_link(self, wsapi_http):
        """Test getting group invite link."""
        wsapi_http._mock_client.set_response(200, {"inviteLink": "https://chat.whatsapp.com/ABC123"})
        client = GroupsClient(wsapi_http)

        result = client.get_invite_link("123456789-987654321@g.us")

        assert result.invite_link == "https://chat.whatsapp.com/ABC123"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/groups/123456789-987654321@g.us/invite-link"

    def test_get_requests(self, wsapi_http):
        """Test getting group join requests."""
        wsapi_http._mock_client.set_response(200, [
            {"userId": "1234567890@s.whatsapp.net", "requestedAt": "2025-01-01T00:00:00Z"},
            {"userId": "9876543210@s.whatsapp.net", "requestedAt": "2025-01-02T00:00:00Z"}
        ])
        client = GroupsClient(wsapi_http)

        result = client.get_requests("123456789-987654321@g.us")

        assert len(result) == 2
        assert result[0].user_id == "1234567890@s.whatsapp.net"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/groups/123456789-987654321@g.us/requests"

    def test_update_participants(self, wsapi_http):
        """Test updating group participants."""
        wsapi_http._mock_client.set_response(204)
        client = GroupsClient(wsapi_http)

        request = GroupUpdateParticipantsRequest(
            participants=["1234567890@s.whatsapp.net", "9876543210@s.whatsapp.net"],
            action="add"
        )
        client.update_participants("123456789-987654321@g.us", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/groups/123456789-987654321@g.us/participants"
        assert len(call["json"]["participants"]) == 2
        assert call["json"]["action"] == "add"

    def test_get_invite_info(self, wsapi_http):
        """Test getting invite info by code."""
        wsapi_http._mock_client.set_response(200, {
            "id": "123456789-987654321@g.us",
            "ownerId": "1234567890@s.whatsapp.net",
            "name": "Test Group",
            "created": "2025-01-01T00:00:00Z",
            "description": "A test group",
            "isAnnounce": False,
            "isLocked": False,
            "isEphemeral": False,
            "ephemeralExpiration": 0,
            "participants": [{"id": "1234567890@s.whatsapp.net"}]
        })
        client = GroupsClient(wsapi_http)

        result = client.get_invite_info("ABC123")

        assert result.id == "123456789-987654321@g.us"
        assert result.name == "Test Group"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/groups/invite/ABC123"


class TestGroupsClientTryMethods:
    """Test suite for GroupsClient try_ methods."""

    def test_try_list_success(self, wsapi_http, sample_group_info):
        """Test try_list on success."""
        wsapi_http._mock_client.set_response(200, [sample_group_info])
        client = GroupsClient(wsapi_http)

        response = client.try_list()

        assert response.is_success
        assert len(response.result) == 1

    def test_try_create_success(self, wsapi_http):
        """Test try_create on success."""
        wsapi_http._mock_client.set_response(201, {"id": "new-group@g.us"})
        client = GroupsClient(wsapi_http)

        request = GroupCreateRequest(
            name="New Group",
            participants=["1234567890@s.whatsapp.net"]
        )
        response = client.try_create(request)

        assert response.is_success
        assert response.result.id == "new-group@g.us"

    def test_try_delete_success(self, wsapi_http):
        """Test try_delete on success."""
        wsapi_http._mock_client.set_response(204)
        client = GroupsClient(wsapi_http)

        response = client.try_delete("123456789-987654321@g.us")

        assert response.is_success
