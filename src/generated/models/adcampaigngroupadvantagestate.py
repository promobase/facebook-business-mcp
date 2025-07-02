"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignGroupAdvantageStateField = Literal[
    "advantage_audience_state",
    "advantage_budget_state",
    "advantage_placement_state",
    "advantage_state",
]


class AdCampaignGroupAdvantageStateFields(BaseModel):
    """Pydantic model for AdCampaignGroupAdvantageState fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    advantage_audience_state: str = Field(None, alias="advantage_audience_state")
    advantage_budget_state: str = Field(None, alias="advantage_budget_state")
    advantage_placement_state: str = Field(None, alias="advantage_placement_state")
    advantage_state: str = Field(None, alias="advantage_state")
