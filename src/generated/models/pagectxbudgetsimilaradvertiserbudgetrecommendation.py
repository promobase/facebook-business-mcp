"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageCTXBudgetSimilarAdvertiserBudgetRecommendationField = Literal["budget", "reported_conversion"]


class PageCTXBudgetSimilarAdvertiserBudgetRecommendationFields(BaseModel):
    """Pydantic model for PageCTXBudgetSimilarAdvertiserBudgetRecommendation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    budget: str = Field(None, alias="budget")
    reported_conversion: str = Field(None, alias="reported_conversion")
