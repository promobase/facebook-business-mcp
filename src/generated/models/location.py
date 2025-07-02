"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LocationField = Literal[
    "city",
    "city_id",
    "country",
    "country_code",
    "latitude",
    "located_in",
    "longitude",
    "name",
    "region",
    "region_id",
    "state",
    "street",
    "zip",
]


class LocationFields(BaseModel):
    """Pydantic model for Location fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    city: str = Field(None, alias="city")
    city_id: int = Field(None, alias="city_id")
    country: str = Field(None, alias="country")
    country_code: str = Field(None, alias="country_code")
    latitude: float = Field(None, alias="latitude")
    located_in: str = Field(None, alias="located_in")
    longitude: float = Field(None, alias="longitude")
    name: str = Field(None, alias="name")
    region: str = Field(None, alias="region")
    region_id: int = Field(None, alias="region_id")
    state: str = Field(None, alias="state")
    street: str = Field(None, alias="street")
    zip: str = Field(None, alias="zip")
