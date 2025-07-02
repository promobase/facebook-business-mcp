"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields


# Field literal type
CallAdsPhoneDataField = Literal[
    "call_ads_phone_data_use_case",
    "callback_variant",
    "destination_website_url",
    "id",
    "page",
    "phone_number",
]


class CallAdsPhoneDataFields(BaseModel):
    """Pydantic model for CallAdsPhoneData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    call_ads_phone_data_use_case: str = Field(None, alias="call_ads_phone_data_use_case")
    callback_variant: str = Field(None, alias="callback_variant")
    destination_website_url: str = Field(None, alias="destination_website_url")
    id: str = Field(None, alias="id")
    page: PageFields = Field(None, alias="page")
    phone_number: str = Field(None, alias="phone_number")
