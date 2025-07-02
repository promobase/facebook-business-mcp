"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountIosFourteenCampaignLimitsField = Literal[
    "campaign_group_limit", "campaign_group_limits_details", "campaign_limit"
]


class AdAccountIosFourteenCampaignLimitsFields(BaseModel):
    """Pydantic model for AdAccountIosFourteenCampaignLimits fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    campaign_group_limit: int = Field(None, alias="campaign_group_limit")
    campaign_group_limits_details: list[dict[str, Any]] = Field(
        None, alias="campaign_group_limits_details"
    )
    campaign_limit: int = Field(None, alias="campaign_limit")
