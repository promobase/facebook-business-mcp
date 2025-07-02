"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adsactionstats import AdsActionStatsFields


# Field literal type
AdKeywordStatsField = Literal[
    "actions",
    "clicks",
    "cost_per_total_action",
    "cost_per_unique_click",
    "cpc",
    "cpm",
    "cpp",
    "ctr",
    "frequency",
    "id",
    "impressions",
    "name",
    "reach",
    "spend",
    "total_actions",
    "total_unique_actions",
    "unique_actions",
    "unique_clicks",
    "unique_ctr",
    "unique_impressions",
]


class AdKeywordStatsFields(BaseModel):
    """Pydantic model for AdKeywordStats fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actions: list[AdsActionStatsFields] = Field(None, alias="actions")
    clicks: int = Field(None, alias="clicks")
    cost_per_total_action: float = Field(None, alias="cost_per_total_action")
    cost_per_unique_click: float = Field(None, alias="cost_per_unique_click")
    cpc: float = Field(None, alias="cpc")
    cpm: float = Field(None, alias="cpm")
    cpp: float = Field(None, alias="cpp")
    ctr: float = Field(None, alias="ctr")
    frequency: float = Field(None, alias="frequency")
    id: str = Field(None, alias="id")
    impressions: int = Field(None, alias="impressions")
    name: str = Field(None, alias="name")
    reach: int = Field(None, alias="reach")
    spend: float = Field(None, alias="spend")
    total_actions: int = Field(None, alias="total_actions")
    total_unique_actions: int = Field(None, alias="total_unique_actions")
    unique_actions: list[AdsActionStatsFields] = Field(None, alias="unique_actions")
    unique_clicks: int = Field(None, alias="unique_clicks")
    unique_ctr: float = Field(None, alias="unique_ctr")
    unique_impressions: int = Field(None, alias="unique_impressions")
