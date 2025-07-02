"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsSegmentsField = Literal[
    "daily_audience_size",
    "daily_impressions",
    "description",
    "id",
    "name",
    "path",
    "popularity",
    "projected_cpm",
    "projected_daily_revenue",
]


class AdsSegmentsFields(BaseModel):
    """Pydantic model for AdsSegments fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    daily_audience_size: int = Field(None, alias="daily_audience_size")
    daily_impressions: int = Field(None, alias="daily_impressions")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    path: list[str] = Field(None, alias="path")
    popularity: float = Field(None, alias="popularity")
    projected_cpm: int = Field(None, alias="projected_cpm")
    projected_daily_revenue: int = Field(None, alias="projected_daily_revenue")
