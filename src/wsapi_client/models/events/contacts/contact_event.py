from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ...entities.groups.group_info import Identity


class ContactEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contact: Optional[Identity] = None
    full_name: Optional[str] = Field(None, alias="fullName")
    in_phone_address_book: Optional[bool] = Field(None, alias="inPhoneAddressBook")
