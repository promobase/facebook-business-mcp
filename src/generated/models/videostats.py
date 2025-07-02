"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
VideoStatsField = Literal[
    "aggregate", "error", "metadata", "time_series", "totals", "x_axis_breakdown"
]


class VideoStatsFields(BaseModel):
    """Pydantic model for VideoStats fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    aggregate: list[dict[str, dict[str, Any]]] = Field(None, alias="aggregate")
    error: str = Field(None, alias="error")
    metadata: list[dict[str, dict[str, Any]]] = Field(None, alias="metadata")
    time_series: list[dict[str, list[dict[str, Any]]]] = Field(None, alias="time_series")
    totals: list[dict[str, dict[str, Any]]] = Field(None, alias="totals")
    x_axis_breakdown: list[list[dict[str, dict[str, Any]]]] = Field(None, alias="x_axis_breakdown")
