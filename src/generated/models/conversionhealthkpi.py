"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ConversionHealthKPIField = Literal[
    "health_indicator",
    "impacted_browsers_match_rate",
    "impacted_browsers_match_rate_mom_trend",
    "impacted_browsers_traffic_share",
    "impacted_browsers_traffic_share_mom_trend",
    "match_rate",
    "match_rate_mom_trend",
    "match_rate_vertical_benchmark",
    "match_rate_vs_benchmark_mom_trend",
]


class ConversionHealthKPIFields(BaseModel):
    """Pydantic model for ConversionHealthKPI fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    health_indicator: str = Field(None, alias="health_indicator")
    impacted_browsers_match_rate: float = Field(None, alias="impacted_browsers_match_rate")
    impacted_browsers_match_rate_mom_trend: float = Field(
        None, alias="impacted_browsers_match_rate_mom_trend"
    )
    impacted_browsers_traffic_share: float = Field(None, alias="impacted_browsers_traffic_share")
    impacted_browsers_traffic_share_mom_trend: float = Field(
        None, alias="impacted_browsers_traffic_share_mom_trend"
    )
    match_rate: float = Field(None, alias="match_rate")
    match_rate_mom_trend: float = Field(None, alias="match_rate_mom_trend")
    match_rate_vertical_benchmark: float = Field(None, alias="match_rate_vertical_benchmark")
    match_rate_vs_benchmark_mom_trend: float = Field(
        None, alias="match_rate_vs_benchmark_mom_trend"
    )
