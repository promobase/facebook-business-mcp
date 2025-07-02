"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BidScheduleField = Literal[
    "ad_object_id",
    "bid_recurrence_type",
    "bid_timezone",
    "bid_value",
    "id",
    "status",
    "time_end",
    "time_start",
]


class BidScheduleFields(BaseModel):
    """Pydantic model for BidSchedule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_object_id: str = Field(None, alias="ad_object_id")
    bid_recurrence_type: str = Field(None, alias="bid_recurrence_type")
    bid_timezone: str = Field(None, alias="bid_timezone")
    bid_value: int = Field(None, alias="bid_value")
    id: str = Field(None, alias="id")
    status: str = Field(None, alias="status")
    time_end: datetime = Field(None, alias="time_end")
    time_start: datetime = Field(None, alias="time_start")
