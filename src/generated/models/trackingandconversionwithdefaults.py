"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TrackingAndConversionWithDefaultsField = Literal[
    "custom_conversion", "custom_tracking", "default_conversion", "default_tracking"
]


class TrackingAndConversionWithDefaultsFields(BaseModel):
    """Pydantic model for TrackingAndConversionWithDefaults fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    custom_conversion: list[dict[str, Any]] = Field(None, alias="custom_conversion")
    custom_tracking: list[dict[str, Any]] = Field(None, alias="custom_tracking")
    default_conversion: list[dict[str, Any]] = Field(None, alias="default_conversion")
    default_tracking: list[dict[str, Any]] = Field(None, alias="default_tracking")
