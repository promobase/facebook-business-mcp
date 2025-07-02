"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CopyrightAttributionInsightsField = Literal[
    "l7_attribution_page_view",
    "l7_attribution_page_view_delta",
    "l7_attribution_video_view",
    "l7_attribution_video_view_delta",
    "metrics_ending_date",
]


class CopyrightAttributionInsightsFields(BaseModel):
    """Pydantic model for CopyrightAttributionInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    l7_attribution_page_view: int = Field(None, alias="l7_attribution_page_view")
    l7_attribution_page_view_delta: float = Field(None, alias="l7_attribution_page_view_delta")
    l7_attribution_video_view: int = Field(None, alias="l7_attribution_video_view")
    l7_attribution_video_view_delta: float = Field(None, alias="l7_attribution_video_view_delta")
    metrics_ending_date: str = Field(None, alias="metrics_ending_date")
