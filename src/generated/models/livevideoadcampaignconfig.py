"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LiveVideoAdCampaignConfigField = Literal["id", "live_video_ad_type"]


class LiveVideoAdCampaignConfigFields(BaseModel):
    """Pydantic model for LiveVideoAdCampaignConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    live_video_ad_type: str = Field(None, alias="live_video_ad_type")
