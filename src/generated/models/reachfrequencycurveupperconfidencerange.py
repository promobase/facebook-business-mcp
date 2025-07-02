"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ReachFrequencyCurveUpperConfidenceRangeField = Literal[
    "impression_upper",
    "num_points",
    "reach",
    "reach_upper",
    "uniq_video_views_2s_upper",
    "video_views_2s_upper",
]


class ReachFrequencyCurveUpperConfidenceRangeFields(BaseModel):
    """Pydantic model for ReachFrequencyCurveUpperConfidenceRange fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    impression_upper: list[int] = Field(None, alias="impression_upper")
    num_points: int = Field(None, alias="num_points")
    reach: list[int] = Field(None, alias="reach")
    reach_upper: list[int] = Field(None, alias="reach_upper")
    uniq_video_views_2s_upper: list[int] = Field(None, alias="uniq_video_views_2s_upper")
    video_views_2s_upper: list[int] = Field(None, alias="video_views_2s_upper")
