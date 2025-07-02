"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgenthankyoupagegatedfile import LeadGenThankYouPageGatedFileFields


# Field literal type
LeadGenThankYouPageField = Literal[
    "body",
    "business_phone_number",
    "button_text",
    "button_type",
    "country_code",
    "enable_messenger",
    "gated_file",
    "id",
    "lead_gen_use_case",
    "status",
    "title",
    "website_url",
]


class LeadGenThankYouPageFields(BaseModel):
    """Pydantic model for LeadGenThankYouPage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    body: str = Field(None, alias="body")
    business_phone_number: str = Field(None, alias="business_phone_number")
    button_text: str = Field(None, alias="button_text")
    button_type: str = Field(None, alias="button_type")
    country_code: str = Field(None, alias="country_code")
    enable_messenger: bool = Field(None, alias="enable_messenger")
    gated_file: LeadGenThankYouPageGatedFileFields = Field(None, alias="gated_file")
    id: str = Field(None, alias="id")
    lead_gen_use_case: str = Field(None, alias="lead_gen_use_case")
    status: str = Field(None, alias="status")
    title: str = Field(None, alias="title")
    website_url: str = Field(None, alias="website_url")
