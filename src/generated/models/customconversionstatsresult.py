"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class CustomConversionStatsResult_aggregation(str, Enum):
    """CustomConversionStatsResult_aggregation enum values."""

    count = "count"
    device_type = "device_type"
    host = "host"
    pixel_fire = "pixel_fire"
    unmatched_count = "unmatched_count"
    unmatched_usd_amount = "unmatched_usd_amount"
    url = "url"
    usd_amount = "usd_amount"


# Field literal type
CustomConversionStatsResultField = Literal["aggregation", "data", "timestamp"]


class CustomConversionStatsResultFields(BaseModel):
    """Pydantic model for CustomConversionStatsResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    aggregation: dict[str, Any] = Field(None, alias="aggregation")
    data: list[dict[str, Any]] = Field(None, alias="data")
    timestamp: datetime = Field(None, alias="timestamp")
