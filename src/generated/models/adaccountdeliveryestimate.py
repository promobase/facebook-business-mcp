"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .outcomepredictionpoint import OutcomePredictionPointFields


# Field literal type
AdAccountDeliveryEstimateField = Literal[
    "daily_outcomes_curve",
    "estimate_dau",
    "estimate_mau_lower_bound",
    "estimate_mau_upper_bound",
    "estimate_ready",
    "targeting_optimization_types",
]


class AdAccountDeliveryEstimateFields(BaseModel):
    """Pydantic model for AdAccountDeliveryEstimate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    daily_outcomes_curve: list[OutcomePredictionPointFields] = Field(
        None, alias="daily_outcomes_curve"
    )
    estimate_dau: int = Field(None, alias="estimate_dau")
    estimate_mau_lower_bound: int = Field(None, alias="estimate_mau_lower_bound")
    estimate_mau_upper_bound: int = Field(None, alias="estimate_mau_upper_bound")
    estimate_ready: bool = Field(None, alias="estimate_ready")
    targeting_optimization_types: list[dict[str, int]] = Field(
        None, alias="targeting_optimization_types"
    )
