"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adsactionstats import AdsActionStatsFields


# Field literal type
BusinessCreativeInsightsField = Literal[
    "actions",
    "age",
    "country",
    "date_end",
    "date_start",
    "device_platform",
    "gender",
    "impressions",
    "inline_link_clicks",
    "objective",
    "optimization_goal",
    "platform_position",
    "publisher_platform",
    "quality_ranking",
    "video_play_actions",
    "video_thruplay_watched_actions",
]


class BusinessCreativeInsightsFields(BaseModel):
    """Pydantic model for BusinessCreativeInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actions: list[AdsActionStatsFields] = Field(None, alias="actions")
    age: str = Field(None, alias="age")
    country: str = Field(None, alias="country")
    date_end: str = Field(None, alias="date_end")
    date_start: str = Field(None, alias="date_start")
    device_platform: str = Field(None, alias="device_platform")
    gender: str = Field(None, alias="gender")
    impressions: int = Field(None, alias="impressions")
    inline_link_clicks: int = Field(None, alias="inline_link_clicks")
    objective: str = Field(None, alias="objective")
    optimization_goal: str = Field(None, alias="optimization_goal")
    platform_position: str = Field(None, alias="platform_position")
    publisher_platform: str = Field(None, alias="publisher_platform")
    quality_ranking: str = Field(None, alias="quality_ranking")
    video_play_actions: list[AdsActionStatsFields] = Field(None, alias="video_play_actions")
    video_thruplay_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_thruplay_watched_actions"
    )
