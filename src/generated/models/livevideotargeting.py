"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .targetinggeolocation import TargetingGeoLocationFields


# Field literal type
LiveVideoTargetingField = Literal["age_max", "age_min", "excluded_countries", "geo_locations"]


class LiveVideoTargetingFields(BaseModel):
    """Pydantic model for LiveVideoTargeting fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    age_max: int = Field(None, alias="age_max")
    age_min: int = Field(None, alias="age_min")
    excluded_countries: list[str] = Field(None, alias="excluded_countries")
    geo_locations: TargetingGeoLocationFields = Field(None, alias="geo_locations")
