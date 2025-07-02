"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ALMEventField = Literal[
    "ad_account_ids",
    "campaign_ids",
    "channel",
    "event",
    "event_time",
    "guidance",
    "guidance_detail",
    "id",
    "parent_advertiser_ids",
    "reseller_business_id",
    "sub_channel",
    "user_id",
]


class ALMEventFields(BaseModel):
    """Pydantic model for ALMEvent fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_ids: list[str] = Field(None, alias="ad_account_ids")
    campaign_ids: list[str] = Field(None, alias="campaign_ids")
    channel: str = Field(None, alias="channel")
    event: str = Field(None, alias="event")
    event_time: datetime = Field(None, alias="event_time")
    guidance: str = Field(None, alias="guidance")
    guidance_detail: str = Field(None, alias="guidance_detail")
    id: str = Field(None, alias="id")
    parent_advertiser_ids: list[str] = Field(None, alias="parent_advertiser_ids")
    reseller_business_id: str = Field(None, alias="reseller_business_id")
    sub_channel: str = Field(None, alias="sub_channel")
    user_id: str = Field(None, alias="user_id")
