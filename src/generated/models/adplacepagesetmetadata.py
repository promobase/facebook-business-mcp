"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdPlacePageSetMetadataField = Literal["audience", "custom", "extra_data", "fixed_radius"]


class AdPlacePageSetMetadataFields(BaseModel):
    """Pydantic model for AdPlacePageSetMetadata fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience: dict[str, Any] = Field(None, alias="audience")
    custom: dict[str, Any] = Field(None, alias="custom")
    extra_data: str = Field(None, alias="extra_data")
    fixed_radius: dict[str, Any] = Field(None, alias="fixed_radius")
