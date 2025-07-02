"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ReachFrequencySpecField = Literal[
    "countries",
    "default_creation_data",
    "global_io_max_campaign_duration",
    "max_campaign_duration",
    "max_days_to_finish",
    "max_pause_without_prediction_rerun",
    "min_campaign_duration",
    "min_reach_limits",
]


class ReachFrequencySpecFields(BaseModel):
    """Pydantic model for ReachFrequencySpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    countries: list[str] = Field(None, alias="countries")
    default_creation_data: dict[str, Any] = Field(None, alias="default_creation_data")
    global_io_max_campaign_duration: int = Field(None, alias="global_io_max_campaign_duration")
    max_campaign_duration: dict[str, Any] = Field(None, alias="max_campaign_duration")
    max_days_to_finish: dict[str, Any] = Field(None, alias="max_days_to_finish")
    max_pause_without_prediction_rerun: dict[str, Any] = Field(
        None, alias="max_pause_without_prediction_rerun"
    )
    min_campaign_duration: dict[str, Any] = Field(None, alias="min_campaign_duration")
    min_reach_limits: dict[str, Any] = Field(None, alias="min_reach_limits")
