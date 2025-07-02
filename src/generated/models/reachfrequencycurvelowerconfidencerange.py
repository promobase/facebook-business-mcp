"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ReachFrequencyCurveLowerConfidenceRangeField = Literal[
    "impression_lower",
    "num_points",
    "reach",
    "reach_lower",
    "uniq_video_views_2s_lower",
    "video_views_2s_lower",
]


class ReachFrequencyCurveLowerConfidenceRangeFields(BaseModel):
    """Pydantic model for ReachFrequencyCurveLowerConfidenceRange fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    impression_lower: list[int] = Field(None, alias="impression_lower")
    num_points: int = Field(None, alias="num_points")
    reach: list[int] = Field(None, alias="reach")
    reach_lower: list[int] = Field(None, alias="reach_lower")
    uniq_video_views_2s_lower: list[int] = Field(None, alias="uniq_video_views_2s_lower")
    video_views_2s_lower: list[int] = Field(None, alias="video_views_2s_lower")
