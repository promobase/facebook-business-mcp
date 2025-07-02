"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BrandSafetyBlockListUsageField = Literal[
    "current_usage", "new_usage", "platform", "position", "threshold"
]


class BrandSafetyBlockListUsageFields(BaseModel):
    """Pydantic model for BrandSafetyBlockListUsage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    current_usage: int = Field(None, alias="current_usage")
    new_usage: int = Field(None, alias="new_usage")
    platform: str = Field(None, alias="platform")
    position: str = Field(None, alias="position")
    threshold: int = Field(None, alias="threshold")
