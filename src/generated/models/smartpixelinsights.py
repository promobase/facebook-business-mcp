"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
SmartPixelInsightsField = Literal["source", "stats"]


class SmartPixelInsightsFields(BaseModel):
    """Pydantic model for SmartPixelInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    source: str = Field(None, alias="source")
    stats: list[dict[str, Any]] = Field(None, alias="stats")
