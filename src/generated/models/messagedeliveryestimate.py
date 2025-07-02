"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MessageDeliveryEstimateField = Literal[
    "estimate_cost",
    "estimate_cost_lower_bound",
    "estimate_cost_upper_bound",
    "estimate_coverage_lower_bound",
    "estimate_coverage_upper_bound",
    "estimate_delivery",
    "estimate_delivery_lower_bound",
    "estimate_delivery_upper_bound",
    "estimate_status",
]


class MessageDeliveryEstimateFields(BaseModel):
    """Pydantic model for MessageDeliveryEstimate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    estimate_cost: float = Field(None, alias="estimate_cost")
    estimate_cost_lower_bound: float = Field(None, alias="estimate_cost_lower_bound")
    estimate_cost_upper_bound: float = Field(None, alias="estimate_cost_upper_bound")
    estimate_coverage_lower_bound: int = Field(None, alias="estimate_coverage_lower_bound")
    estimate_coverage_upper_bound: int = Field(None, alias="estimate_coverage_upper_bound")
    estimate_delivery: int = Field(None, alias="estimate_delivery")
    estimate_delivery_lower_bound: int = Field(None, alias="estimate_delivery_lower_bound")
    estimate_delivery_upper_bound: int = Field(None, alias="estimate_delivery_upper_bound")
    estimate_status: str = Field(None, alias="estimate_status")
