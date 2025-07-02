"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelMicrodataStatsField = Literal[
    "allowed_domains",
    "errors_stats_for_time_ranges",
    "has_valid_events",
    "suggested_allowed_domains_count_max",
    "suggested_trusted_domains",
]


class AdsPixelMicrodataStatsFields(BaseModel):
    """Pydantic model for AdsPixelMicrodataStats fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    allowed_domains: list[str] = Field(None, alias="allowed_domains")
    errors_stats_for_time_ranges: list[dict[str, Any]] = Field(
        None, alias="errors_stats_for_time_ranges"
    )
    has_valid_events: bool = Field(None, alias="has_valid_events")
    suggested_allowed_domains_count_max: int = Field(
        None, alias="suggested_allowed_domains_count_max"
    )
    suggested_trusted_domains: list[str] = Field(None, alias="suggested_trusted_domains")
