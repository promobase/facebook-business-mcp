"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
StoreLocationField = Literal[
    "full_address",
    "hours",
    "id",
    "phone_number",
    "pickup_options",
    "price_range",
    "store_code",
    "zip_code",
]


class StoreLocationFields(BaseModel):
    """Pydantic model for StoreLocation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    full_address: str = Field(None, alias="full_address")
    hours: dict[str, Any] = Field(None, alias="hours")
    id: str = Field(None, alias="id")
    phone_number: str = Field(None, alias="phone_number")
    pickup_options: list[str] = Field(None, alias="pickup_options")
    price_range: str = Field(None, alias="price_range")
    store_code: str = Field(None, alias="store_code")
    zip_code: str = Field(None, alias="zip_code")
