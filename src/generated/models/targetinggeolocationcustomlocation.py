"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingGeoLocationCustomLocationField = Literal[
    "address_string",
    "country",
    "country_group",
    "custom_type",
    "distance_unit",
    "key",
    "latitude",
    "longitude",
    "max_population",
    "min_population",
    "name",
    "primary_city_id",
    "radius",
    "region_id",
]


class TargetingGeoLocationCustomLocationFields(BaseModel):
    """Pydantic model for TargetingGeoLocationCustomLocation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    address_string: str = Field(None, alias="address_string")
    country: str = Field(None, alias="country")
    country_group: str = Field(None, alias="country_group")
    custom_type: str = Field(None, alias="custom_type")
    distance_unit: str = Field(None, alias="distance_unit")
    key: str = Field(None, alias="key")
    latitude: float = Field(None, alias="latitude")
    longitude: float = Field(None, alias="longitude")
    max_population: int = Field(None, alias="max_population")
    min_population: int = Field(None, alias="min_population")
    name: str = Field(None, alias="name")
    primary_city_id: int = Field(None, alias="primary_city_id")
    radius: float = Field(None, alias="radius")
    region_id: int = Field(None, alias="region_id")
