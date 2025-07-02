"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
HighDemandPeriodTimeSuggestionWeeklySegmentField = Literal[
    "days", "end_minute", "start_minute", "timezone_type"
]


class HighDemandPeriodTimeSuggestionWeeklySegmentFields(BaseModel):
    """Pydantic model for HighDemandPeriodTimeSuggestionWeeklySegment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    days: list[str] = Field(None, alias="days")
    end_minute: int = Field(None, alias="end_minute")
    start_minute: int = Field(None, alias="start_minute")
    timezone_type: str = Field(None, alias="timezone_type")
