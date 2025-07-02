"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativePlaceDataField = Literal[
    "address_string", "label", "latitude", "location_source_id", "longitude", "type"
]


class AdCreativePlaceDataFields(BaseModel):
    """Pydantic model for AdCreativePlaceData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    address_string: str = Field(None, alias="address_string")
    label: str = Field(None, alias="label")
    latitude: float = Field(None, alias="latitude")
    location_source_id: str = Field(None, alias="location_source_id")
    longitude: float = Field(None, alias="longitude")
    type: str = Field(None, alias="type")
