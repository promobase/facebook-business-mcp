"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountCustomAudienceLimitsField = Literal[
    "audience_update_quota_in_total",
    "audience_update_quota_left",
    "has_hit_audience_update_limit",
    "next_audience_update_available_time",
    "rate_limit_reset_time",
]


class AdAccountCustomAudienceLimitsFields(BaseModel):
    """Pydantic model for AdAccountCustomAudienceLimits fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience_update_quota_in_total: int = Field(None, alias="audience_update_quota_in_total")
    audience_update_quota_left: float = Field(None, alias="audience_update_quota_left")
    has_hit_audience_update_limit: bool = Field(None, alias="has_hit_audience_update_limit")
    next_audience_update_available_time: str = Field(
        None, alias="next_audience_update_available_time"
    )
    rate_limit_reset_time: str = Field(None, alias="rate_limit_reset_time")
