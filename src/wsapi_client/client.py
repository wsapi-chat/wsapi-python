from __future__ import annotations

from .api.account import AccountClient
from .api.calls import CallsClient
from .api.chats import ChatsClient
from .api.communities import CommunitiesClient
from .api.contacts import ContactsClient
from .api.groups import GroupsClient
from .api.media import MediaClient
from .api.messages import MessagesClient
from .api.newsletters import NewslettersClient
from .api.session import SessionClient
from .api.status import StatusClient
from .api.users import UsersClient
from .http import WSApiHttp


class WSApiClient:
    def __init__(
        self,
        api_key: str,
        instance_id: str,
        *,
        base_url: str = "https://wsapi.chat",
        timeout: float = 30.0,
    ) -> None:
        self._http = WSApiHttp(api_key=api_key, instance_id=instance_id, base_url=base_url, timeout=timeout)

        # Surface parity with .NET: expose sub-clients
        self.account = AccountClient(self._http)
        self.messages = MessagesClient(self._http)
        self.media = MediaClient(self._http)
        self.session = SessionClient(self._http)
        self.contacts = ContactsClient(self._http)
        self.groups = GroupsClient(self._http)
        self.chats = ChatsClient(self._http)
        self.users = UsersClient(self._http)
        self.calls = CallsClient(self._http)
        self.communities = CommunitiesClient(self._http)
        self.newsletters = NewslettersClient(self._http)
        self.status = StatusClient(self._http)

    def close(self) -> None:
        self._http.close()
