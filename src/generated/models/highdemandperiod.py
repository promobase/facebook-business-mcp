"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .highdemandperiodtimesuggestionweeklysegment import (
        HighDemandPeriodTimeSuggestionWeeklySegmentFields,
    )


# Field literal type
HighDemandPeriodField = Literal[
    "ad_object_id",
    "budget_value",
    "budget_value_type",
    "id",
    "recurrence_type",
    "time_end",
    "time_start",
    "weekly_schedule",
]


class HighDemandPeriodFields(BaseModel):
    """Pydantic model for HighDemandPeriod fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_object_id: str = Field(None, alias="ad_object_id")
    budget_value: int = Field(None, alias="budget_value")
    budget_value_type: str = Field(None, alias="budget_value_type")
    id: str = Field(None, alias="id")
    recurrence_type: str = Field(None, alias="recurrence_type")
    time_end: datetime = Field(None, alias="time_end")
    time_start: datetime = Field(None, alias="time_start")
    weekly_schedule: list[HighDemandPeriodTimeSuggestionWeeklySegmentFields] = Field(
        None, alias="weekly_schedule"
    )
