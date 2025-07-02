"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
OutcomePredictionPointField = Literal["actions", "impressions", "reach", "spend"]


class OutcomePredictionPointFields(BaseModel):
    """Pydantic model for OutcomePredictionPoint fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actions: float = Field(None, alias="actions")
    impressions: float = Field(None, alias="impressions")
    reach: float = Field(None, alias="reach")
    spend: int = Field(None, alias="spend")
