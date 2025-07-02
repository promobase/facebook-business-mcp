"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdPlacementField = Literal[
    "bundle_id",
    "display_format",
    "external_placement_id",
    "google_display_format",
    "id",
    "name",
    "placement_group",
    "platform",
    "status",
]


class AdPlacementFields(BaseModel):
    """Pydantic model for AdPlacement fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    bundle_id: str = Field(None, alias="bundle_id")
    display_format: str = Field(None, alias="display_format")
    external_placement_id: str = Field(None, alias="external_placement_id")
    google_display_format: str = Field(None, alias="google_display_format")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    placement_group: dict[str, Any] = Field(None, alias="placement_group")
    platform: str = Field(None, alias="platform")
    status: str = Field(None, alias="status")
