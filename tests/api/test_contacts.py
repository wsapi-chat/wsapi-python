"""
Tests for ContactsClient API methods.
"""
import pytest
from wsapi_client.api.contacts import ContactsClient
from wsapi_client.models.requests.contacts.contact_create_request import ContactCreateRequest
from wsapi_client.models.requests.contacts.contact_update_request import ContactUpdateRequest


class TestContactsClient:
    """Test suite for ContactsClient."""

    def test_list_contacts(self, wsapi_http, sample_contact_info):
        """Test listing all contacts."""
        wsapi_http._mock_client.set_response(200, [sample_contact_info])
        client = ContactsClient(wsapi_http)

        result = client.list()

        assert len(result) == 1
        assert result[0].id == "1234567890@s.whatsapp.net"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/contacts"

    def test_get_contact(self, wsapi_http, sample_contact_info):
        """Test getting a single contact."""
        wsapi_http._mock_client.set_response(200, sample_contact_info)
        client = ContactsClient(wsapi_http)

        result = client.get("1234567890@s.whatsapp.net")

        assert result.id == "1234567890@s.whatsapp.net"
        assert result.full_name == "John Doe"
        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "GET"
        assert call["url"] == "/contacts/1234567890@s.whatsapp.net"

    def test_create_contact(self, wsapi_http):
        """Test creating a new contact."""
        wsapi_http._mock_client.set_response(201)
        client = ContactsClient(wsapi_http)

        request = ContactCreateRequest(
            id="1234567890@s.whatsapp.net",
            full_name="New Contact",
            first_name="New"
        )
        client.create(request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "POST"
        assert call["url"] == "/contacts"
        assert call["json"]["fullName"] == "New Contact"
        assert call["json"]["firstName"] == "New"

    def test_update_contact(self, wsapi_http):
        """Test updating a contact."""
        wsapi_http._mock_client.set_response(204)
        client = ContactsClient(wsapi_http)

        request = ContactUpdateRequest(full_name="Updated Name", first_name="Updated")
        client.update("1234567890@s.whatsapp.net", request)

        call = wsapi_http._mock_client.get_last_call()
        assert call["method"] == "PUT"
        assert call["url"] == "/contacts/1234567890@s.whatsapp.net"
        assert call["json"]["fullName"] == "Updated Name"
        assert call["json"]["firstName"] == "Updated"


class TestContactsClientTryMethods:
    """Test suite for ContactsClient try_ methods."""

    def test_try_list_success(self, wsapi_http, sample_contact_info):
        """Test try_list on success."""
        wsapi_http._mock_client.set_response(200, [sample_contact_info])
        client = ContactsClient(wsapi_http)

        response = client.try_list()

        assert response.is_success
        assert len(response.result) == 1

    def test_try_get_success(self, wsapi_http, sample_contact_info):
        """Test try_get on success."""
        wsapi_http._mock_client.set_response(200, sample_contact_info)
        client = ContactsClient(wsapi_http)

        response = client.try_get("1234567890@s.whatsapp.net")

        assert response.is_success
        assert response.result.id == "1234567890@s.whatsapp.net"

    def test_try_create_success(self, wsapi_http):
        """Test try_create on success."""
        wsapi_http._mock_client.set_response(201)
        client = ContactsClient(wsapi_http)

        request = ContactCreateRequest(
            id="1234567890@s.whatsapp.net",
            full_name="New Contact",
            first_name="New"
        )
        response = client.try_create(request)

        assert response.is_success

    def test_try_update_success(self, wsapi_http):
        """Test try_update on success."""
        wsapi_http._mock_client.set_response(204)
        client = ContactsClient(wsapi_http)

        request = ContactUpdateRequest(full_name="Updated Name", first_name="Updated")
        response = client.try_update("1234567890@s.whatsapp.net", request)

        assert response.is_success
