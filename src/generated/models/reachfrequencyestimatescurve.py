"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ReachFrequencyEstimatesCurveField = Literal[
    "budget",
    "conversion",
    "impression",
    "interpolated_reach",
    "num_points",
    "raw_impression",
    "raw_reach",
    "reach",
]


class ReachFrequencyEstimatesCurveFields(BaseModel):
    """Pydantic model for ReachFrequencyEstimatesCurve fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    budget: list[int] = Field(None, alias="budget")
    conversion: list[int] = Field(None, alias="conversion")
    impression: list[int] = Field(None, alias="impression")
    interpolated_reach: float = Field(None, alias="interpolated_reach")
    num_points: int = Field(None, alias="num_points")
    raw_impression: list[int] = Field(None, alias="raw_impression")
    raw_reach: list[int] = Field(None, alias="raw_reach")
    reach: list[int] = Field(None, alias="reach")
