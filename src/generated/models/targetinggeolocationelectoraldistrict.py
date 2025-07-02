"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingGeoLocationElectoralDistrictField = Literal[
    "country", "deprecation_code", "electoral_district", "key", "name"
]


class TargetingGeoLocationElectoralDistrictFields(BaseModel):
    """Pydantic model for TargetingGeoLocationElectoralDistrict fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    country: str = Field(None, alias="country")
    deprecation_code: str = Field(None, alias="deprecation_code")
    electoral_district: str = Field(None, alias="electoral_district")
    key: str = Field(None, alias="key")
    name: str = Field(None, alias="name")
