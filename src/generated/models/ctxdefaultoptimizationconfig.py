"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CTXDefaultOptimizationConfigField = Literal["destination_type", "objective", "optimization_goal"]


class CTXDefaultOptimizationConfigFields(BaseModel):
    """Pydantic model for CTXDefaultOptimizationConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    destination_type: str = Field(None, alias="destination_type")
    objective: str = Field(None, alias="objective")
    optimization_goal: str = Field(None, alias="optimization_goal")
