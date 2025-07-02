"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingDynamicRuleField = Literal[
    "action.type",
    "ad_group_id",
    "campaign_group_id",
    "campaign_id",
    "impression_count",
    "page_id",
    "post",
    "retention_seconds",
]


class TargetingDynamicRuleFields(BaseModel):
    """Pydantic model for TargetingDynamicRule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action_type: str = Field(None, alias="action.type")
    ad_group_id: str = Field(None, alias="ad_group_id")
    campaign_group_id: str = Field(None, alias="campaign_group_id")
    campaign_id: str = Field(None, alias="campaign_id")
    impression_count: str = Field(None, alias="impression_count")
    page_id: str = Field(None, alias="page_id")
    post: str = Field(None, alias="post")
    retention_seconds: str = Field(None, alias="retention_seconds")
