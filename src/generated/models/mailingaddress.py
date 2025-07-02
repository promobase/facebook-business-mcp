"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields


# Field literal type
MailingAddressField = Literal[
    "city", "city_page", "country", "id", "postal_code", "region", "street1", "street2"
]


class MailingAddressFields(BaseModel):
    """Pydantic model for MailingAddress fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    city: str = Field(None, alias="city")
    city_page: PageFields = Field(None, alias="city_page")
    country: str = Field(None, alias="country")
    id: str = Field(None, alias="id")
    postal_code: str = Field(None, alias="postal_code")
    region: str = Field(None, alias="region")
    street1: str = Field(None, alias="street1")
    street2: str = Field(None, alias="street2")
