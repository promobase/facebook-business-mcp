"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .targetinggeolocation import TargetingGeoLocationFields


# Field literal type
AdAssetCustomizationRuleCustomizationSpecField = Literal[
    "age_max",
    "age_min",
    "audience_network_positions",
    "device_platforms",
    "facebook_positions",
    "geo_locations",
    "instagram_positions",
    "locales",
    "messenger_positions",
    "publisher_platforms",
]


class AdAssetCustomizationRuleCustomizationSpecFields(BaseModel):
    """Pydantic model for AdAssetCustomizationRuleCustomizationSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    age_max: int = Field(None, alias="age_max")
    age_min: int = Field(None, alias="age_min")
    audience_network_positions: list[str] = Field(None, alias="audience_network_positions")
    device_platforms: list[dict[str, Any]] = Field(None, alias="device_platforms")
    facebook_positions: list[str] = Field(None, alias="facebook_positions")
    geo_locations: TargetingGeoLocationFields = Field(None, alias="geo_locations")
    instagram_positions: list[str] = Field(None, alias="instagram_positions")
    locales: list[int] = Field(None, alias="locales")
    messenger_positions: list[str] = Field(None, alias="messenger_positions")
    publisher_platforms: list[str] = Field(None, alias="publisher_platforms")
