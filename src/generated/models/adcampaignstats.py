"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignStatsField = Literal[
    "account_id",
    "actions",
    "adgroup_id",
    "campaign_id",
    "campaign_ids",
    "clicks",
    "end_time",
    "id",
    "impressions",
    "inline_actions",
    "io_number",
    "is_completed",
    "line_number",
    "newsfeed_position",
    "social_clicks",
    "social_impressions",
    "social_spent",
    "social_unique_clicks",
    "social_unique_impressions",
    "spent",
    "start_time",
    "topline_id",
    "unique_clicks",
    "unique_impressions",
]


class AdCampaignStatsFields(BaseModel):
    """Pydantic model for AdCampaignStats fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    actions: dict[str, Any] = Field(None, alias="actions")
    adgroup_id: str = Field(None, alias="adgroup_id")
    campaign_id: str = Field(None, alias="campaign_id")
    campaign_ids: list[str] = Field(None, alias="campaign_ids")
    clicks: int = Field(None, alias="clicks")
    end_time: dict[str, Any] = Field(None, alias="end_time")
    id: str = Field(None, alias="id")
    impressions: str = Field(None, alias="impressions")
    inline_actions: dict[str, Any] = Field(None, alias="inline_actions")
    io_number: int = Field(None, alias="io_number")
    is_completed: bool = Field(None, alias="is_completed")
    line_number: int = Field(None, alias="line_number")
    newsfeed_position: dict[str, Any] = Field(None, alias="newsfeed_position")
    social_clicks: int = Field(None, alias="social_clicks")
    social_impressions: str = Field(None, alias="social_impressions")
    social_spent: int = Field(None, alias="social_spent")
    social_unique_clicks: int = Field(None, alias="social_unique_clicks")
    social_unique_impressions: str = Field(None, alias="social_unique_impressions")
    spent: int = Field(None, alias="spent")
    start_time: dict[str, Any] = Field(None, alias="start_time")
    topline_id: str = Field(None, alias="topline_id")
    unique_clicks: int = Field(None, alias="unique_clicks")
    unique_impressions: str = Field(None, alias="unique_impressions")
