"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignDeliveryStatsUnsupportedReasonsField = Literal["reason_data", "reason_type"]


class AdCampaignDeliveryStatsUnsupportedReasonsFields(BaseModel):
    """Pydantic model for AdCampaignDeliveryStatsUnsupportedReasons fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    reason_data: list[dict[str, str]] = Field(None, alias="reason_data")
    reason_type: str = Field(None, alias="reason_type")
