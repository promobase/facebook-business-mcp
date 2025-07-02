"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ProductFeedSchedule_interval(str, Enum):
    """ProductFeedSchedule_interval enum values."""

    DAILY = "DAILY"
    HOURLY = "HOURLY"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"


# Field literal type
ProductFeedScheduleField = Literal[
    "day_of_month",
    "day_of_week",
    "hour",
    "id",
    "interval",
    "interval_count",
    "minute",
    "timezone",
    "url",
    "username",
]


class ProductFeedScheduleFields(BaseModel):
    """Pydantic model for ProductFeedSchedule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    day_of_month: int = Field(None, alias="day_of_month")
    day_of_week: str = Field(None, alias="day_of_week")
    hour: int = Field(None, alias="hour")
    id: str = Field(None, alias="id")
    interval: dict[str, Any] = Field(None, alias="interval")
    interval_count: int = Field(None, alias="interval_count")
    minute: int = Field(None, alias="minute")
    timezone: str = Field(None, alias="timezone")
    url: str = Field(None, alias="url")
    username: str = Field(None, alias="username")
