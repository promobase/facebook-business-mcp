"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adset import AdSetFields


# Field literal type
AdKpiShiftField = Literal[
    "ad_set",
    "cost_per_result_shift",
    "enough_effective_days",
    "result_indicator",
    "result_shift",
    "spend_shift",
]


class AdKpiShiftFields(BaseModel):
    """Pydantic model for AdKpiShift fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_set: AdSetFields = Field(None, alias="ad_set")
    cost_per_result_shift: float = Field(None, alias="cost_per_result_shift")
    enough_effective_days: bool = Field(None, alias="enough_effective_days")
    result_indicator: str = Field(None, alias="result_indicator")
    result_shift: float = Field(None, alias="result_shift")
    spend_shift: float = Field(None, alias="spend_shift")
