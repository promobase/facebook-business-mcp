"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignOptimizationEventField = Literal["custom_conversion_id", "event_sequence", "event_type"]


class AdCampaignOptimizationEventFields(BaseModel):
    """Pydantic model for AdCampaignOptimizationEvent fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    custom_conversion_id: str = Field(None, alias="custom_conversion_id")
    event_sequence: int = Field(None, alias="event_sequence")
    event_type: str = Field(None, alias="event_type")
