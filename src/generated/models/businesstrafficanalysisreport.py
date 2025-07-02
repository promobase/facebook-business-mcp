"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessTrafficAnalysisReportField = Literal[
    "audience_location", "event_category", "traffic_analysis_impressions"
]


class BusinessTrafficAnalysisReportFields(BaseModel):
    """Pydantic model for BusinessTrafficAnalysisReport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience_location: list[dict[str, Any]] = Field(None, alias="audience_location")
    event_category: list[dict[str, Any]] = Field(None, alias="event_category")
    traffic_analysis_impressions: list[dict[str, Any]] = Field(
        None, alias="traffic_analysis_impressions"
    )
