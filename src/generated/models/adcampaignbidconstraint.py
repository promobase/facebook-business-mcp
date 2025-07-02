"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignBidConstraintField = Literal["roas_average_floor"]


class AdCampaignBidConstraintFields(BaseModel):
    """Pydantic model for AdCampaignBidConstraint fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    roas_average_floor: int = Field(None, alias="roas_average_floor")
