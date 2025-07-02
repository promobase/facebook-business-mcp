"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adspixelstats import AdsPixelStatsFields


# Field literal type
AdsPixelStatsResultField = Literal["aggregation", "data", "start_time"]


class AdsPixelStatsResultFields(BaseModel):
    """Pydantic model for AdsPixelStatsResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    aggregation: str = Field(None, alias="aggregation")
    data: list[AdsPixelStatsFields] = Field(None, alias="data")
    start_time: datetime = Field(None, alias="start_time")
