"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignMultiAdsField = Literal["enroll_status", "source_type"]


class AdCampaignMultiAdsFields(BaseModel):
    """Pydantic model for AdCampaignMultiAds fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    enroll_status: str = Field(None, alias="enroll_status")
    source_type: str = Field(None, alias="source_type")
