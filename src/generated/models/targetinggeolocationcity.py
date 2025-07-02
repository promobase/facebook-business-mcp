"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingGeoLocationCityField = Literal[
    "country", "distance_unit", "key", "name", "radius", "region", "region_id"
]


class TargetingGeoLocationCityFields(BaseModel):
    """Pydantic model for TargetingGeoLocationCity fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    country: str = Field(None, alias="country")
    distance_unit: str = Field(None, alias="distance_unit")
    key: str = Field(None, alias="key")
    name: str = Field(None, alias="name")
    radius: int = Field(None, alias="radius")
    region: str = Field(None, alias="region")
    region_id: str = Field(None, alias="region_id")
