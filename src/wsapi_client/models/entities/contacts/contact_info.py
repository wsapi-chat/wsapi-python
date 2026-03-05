from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ContactInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    lid: Optional[str] = None
    phone: Optional[str] = None
    device: Optional[int] = None
    full_name: Optional[str] = Field(None, alias="fullName")
    first_name: Optional[str] = Field(None, alias="firstName")
    push_name: Optional[str] = Field(None, alias="pushName")
    business_name: Optional[str] = Field(None, alias="businessName")
    in_phone_address_book: Optional[bool] = Field(None, alias="inPhoneAddressBook")
