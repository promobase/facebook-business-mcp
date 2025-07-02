"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MinimumBudgetField = Literal[
    "currency",
    "min_daily_budget_high_freq",
    "min_daily_budget_imp",
    "min_daily_budget_low_freq",
    "min_daily_budget_video_views",
]


class MinimumBudgetFields(BaseModel):
    """Pydantic model for MinimumBudget fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    currency: str = Field(None, alias="currency")
    min_daily_budget_high_freq: int = Field(None, alias="min_daily_budget_high_freq")
    min_daily_budget_imp: int = Field(None, alias="min_daily_budget_imp")
    min_daily_budget_low_freq: int = Field(None, alias="min_daily_budget_low_freq")
    min_daily_budget_video_views: int = Field(None, alias="min_daily_budget_video_views")
