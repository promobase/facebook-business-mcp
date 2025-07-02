"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AgencyClientDeclarationField = Literal[
    "agency_representing_client",
    "client_based_in_france",
    "client_city",
    "client_country_code",
    "client_email_address",
    "client_name",
    "client_postal_code",
    "client_province",
    "client_street",
    "client_street2",
    "has_written_mandate_from_advertiser",
    "is_client_paying_invoices",
]


class AgencyClientDeclarationFields(BaseModel):
    """Pydantic model for AgencyClientDeclaration fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    agency_representing_client: int = Field(None, alias="agency_representing_client")
    client_based_in_france: int = Field(None, alias="client_based_in_france")
    client_city: str = Field(None, alias="client_city")
    client_country_code: str = Field(None, alias="client_country_code")
    client_email_address: str = Field(None, alias="client_email_address")
    client_name: str = Field(None, alias="client_name")
    client_postal_code: str = Field(None, alias="client_postal_code")
    client_province: str = Field(None, alias="client_province")
    client_street: str = Field(None, alias="client_street")
    client_street2: str = Field(None, alias="client_street2")
    has_written_mandate_from_advertiser: int = Field(
        None, alias="has_written_mandate_from_advertiser"
    )
    is_client_paying_invoices: int = Field(None, alias="is_client_paying_invoices")
