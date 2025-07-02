"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelStatsField = Literal["count", "diagnostics_hourly_last_timestamp", "event", "value"]


class AdsPixelStatsFields(BaseModel):
    """Pydantic model for AdsPixelStats fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    count: int = Field(None, alias="count")
    diagnostics_hourly_last_timestamp: datetime = Field(
        None, alias="diagnostics_hourly_last_timestamp"
    )
    event: str = Field(None, alias="event")
    value: str = Field(None, alias="value")
