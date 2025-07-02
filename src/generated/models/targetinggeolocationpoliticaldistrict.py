"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingGeoLocationPoliticalDistrictField = Literal["country", "key", "name", "political_district"]


class TargetingGeoLocationPoliticalDistrictFields(BaseModel):
    """Pydantic model for TargetingGeoLocationPoliticalDistrict fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    country: str = Field(None, alias="country")
    key: str = Field(None, alias="key")
    name: str = Field(None, alias="name")
    political_district: str = Field(None, alias="political_district")
