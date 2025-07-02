"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingGeoLocationGeoEntitiesField = Literal["country", "key", "name", "region", "region_id"]


class TargetingGeoLocationGeoEntitiesFields(BaseModel):
    """Pydantic model for TargetingGeoLocationGeoEntities fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    country: str = Field(None, alias="country")
    key: str = Field(None, alias="key")
    name: str = Field(None, alias="name")
    region: str = Field(None, alias="region")
    region_id: str = Field(None, alias="region_id")
