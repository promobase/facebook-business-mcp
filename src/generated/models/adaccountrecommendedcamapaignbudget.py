"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountRecommendedCamapaignBudgetField = Literal["daily", "lifetime", "objective"]


class AdAccountRecommendedCamapaignBudgetFields(BaseModel):
    """Pydantic model for AdAccountRecommendedCamapaignBudget fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    daily: str = Field(None, alias="daily")
    lifetime: str = Field(None, alias="lifetime")
    objective: str = Field(None, alias="objective")
