"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessMediaAdPlacementValidationResultField = Literal[
    "ad_placement", "ad_placement_label", "error_messages", "is_valid"
]


class BusinessMediaAdPlacementValidationResultFields(BaseModel):
    """Pydantic model for BusinessMediaAdPlacementValidationResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_placement: str = Field(None, alias="ad_placement")
    ad_placement_label: str = Field(None, alias="ad_placement_label")
    error_messages: list[str] = Field(None, alias="error_messages")
    is_valid: bool = Field(None, alias="is_valid")
