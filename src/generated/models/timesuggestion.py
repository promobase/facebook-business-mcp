"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TimeSuggestionField = Literal["high_demand_periods", "is_enabled"]


class TimeSuggestionFields(BaseModel):
    """Pydantic model for TimeSuggestion fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    high_demand_periods: list[dict[str, Any]] = Field(None, alias="high_demand_periods")
    is_enabled: bool = Field(None, alias="is_enabled")
