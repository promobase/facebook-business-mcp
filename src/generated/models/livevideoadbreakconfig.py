"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LiveVideoAdBreakConfigField = Literal[
    "default_ad_break_duration",
    "failure_reason_polling_interval",
    "first_break_eligible_secs",
    "guide_url",
    "is_eligible_to_onboard",
    "is_enabled",
    "onboarding_url",
    "preparing_duration",
    "time_between_ad_breaks_secs",
    "viewer_count_threshold",
]


class LiveVideoAdBreakConfigFields(BaseModel):
    """Pydantic model for LiveVideoAdBreakConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    default_ad_break_duration: int = Field(None, alias="default_ad_break_duration")
    failure_reason_polling_interval: int = Field(None, alias="failure_reason_polling_interval")
    first_break_eligible_secs: int = Field(None, alias="first_break_eligible_secs")
    guide_url: str = Field(None, alias="guide_url")
    is_eligible_to_onboard: bool = Field(None, alias="is_eligible_to_onboard")
    is_enabled: bool = Field(None, alias="is_enabled")
    onboarding_url: str = Field(None, alias="onboarding_url")
    preparing_duration: int = Field(None, alias="preparing_duration")
    time_between_ad_breaks_secs: int = Field(None, alias="time_between_ad_breaks_secs")
    viewer_count_threshold: int = Field(None, alias="viewer_count_threshold")
