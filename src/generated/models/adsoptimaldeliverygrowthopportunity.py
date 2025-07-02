"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsOptimalDeliveryGrowthOpportunityField = Literal[
    "child_metadata", "metadata", "optimization_type"
]


class AdsOptimalDeliveryGrowthOpportunityFields(BaseModel):
    """Pydantic model for AdsOptimalDeliveryGrowthOpportunity fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    child_metadata: list[dict[str, dict[str, Any]]] = Field(None, alias="child_metadata")
    metadata: dict[str, Any] = Field(None, alias="metadata")
    optimization_type: str = Field(None, alias="optimization_type")
