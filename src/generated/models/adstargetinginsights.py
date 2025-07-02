"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsTargetingInsightsField = Literal[
    "audience_size",
    "clicks",
    "conversion_cost",
    "conversions",
    "description",
    "id",
    "impressions",
    "name",
    "revenue",
    "spend",
    "type",
]


class AdsTargetingInsightsFields(BaseModel):
    """Pydantic model for AdsTargetingInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience_size: int = Field(None, alias="audience_size")
    clicks: int = Field(None, alias="clicks")
    conversion_cost: float = Field(None, alias="conversion_cost")
    conversions: int = Field(None, alias="conversions")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    impressions: str = Field(None, alias="impressions")
    name: str = Field(None, alias="name")
    revenue: float = Field(None, alias="revenue")
    spend: float = Field(None, alias="spend")
    type: str = Field(None, alias="type")
