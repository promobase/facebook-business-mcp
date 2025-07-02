"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CTXOptimizationEligibilityField = Literal["ctm"]


class CTXOptimizationEligibilityFields(BaseModel):
    """Pydantic model for CTXOptimizationEligibility fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ctm: dict[str, Any] = Field(None, alias="ctm")
