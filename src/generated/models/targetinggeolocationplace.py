"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingGeoLocationPlaceField = Literal[
    "country",
    "distance_unit",
    "key",
    "latitude",
    "longitude",
    "name",
    "primary_city_id",
    "radius",
    "region_id",
]


class TargetingGeoLocationPlaceFields(BaseModel):
    """Pydantic model for TargetingGeoLocationPlace fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    country: str = Field(None, alias="country")
    distance_unit: str = Field(None, alias="distance_unit")
    key: str = Field(None, alias="key")
    latitude: float = Field(None, alias="latitude")
    longitude: float = Field(None, alias="longitude")
    name: str = Field(None, alias="name")
    primary_city_id: int = Field(None, alias="primary_city_id")
    radius: float = Field(None, alias="radius")
    region_id: int = Field(None, alias="region_id")
