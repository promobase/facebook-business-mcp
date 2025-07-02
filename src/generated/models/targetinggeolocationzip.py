"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingGeoLocationZipField = Literal["country", "key", "name", "primary_city_id", "region_id"]


class TargetingGeoLocationZipFields(BaseModel):
    """Pydantic model for TargetingGeoLocationZip fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    country: str = Field(None, alias="country")
    key: str = Field(None, alias="key")
    name: str = Field(None, alias="name")
    primary_city_id: int = Field(None, alias="primary_city_id")
    region_id: int = Field(None, alias="region_id")
