"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignFrequencyControlSpecsField = Literal["event", "interval_days", "max_frequency"]


class AdCampaignFrequencyControlSpecsFields(BaseModel):
    """Pydantic model for AdCampaignFrequencyControlSpecs fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    event: str = Field(None, alias="event")
    interval_days: int = Field(None, alias="interval_days")
    max_frequency: int = Field(None, alias="max_frequency")
