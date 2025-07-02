"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomAudienceSharedAccountCampaignInfoField = Literal[
    "account_id",
    "account_name",
    "adset_excluding_count",
    "adset_including_count",
    "campaign_delivery_status",
    "campaign_objective",
    "campaign_pages",
    "campaign_schedule",
]


class CustomAudienceSharedAccountCampaignInfoFields(BaseModel):
    """Pydantic model for CustomAudienceSharedAccountCampaignInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    account_name: str = Field(None, alias="account_name")
    adset_excluding_count: int = Field(None, alias="adset_excluding_count")
    adset_including_count: int = Field(None, alias="adset_including_count")
    campaign_delivery_status: str = Field(None, alias="campaign_delivery_status")
    campaign_objective: str = Field(None, alias="campaign_objective")
    campaign_pages: list[dict[str, Any]] = Field(None, alias="campaign_pages")
    campaign_schedule: str = Field(None, alias="campaign_schedule")
