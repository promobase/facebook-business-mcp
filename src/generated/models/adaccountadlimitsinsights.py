"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountAdLimitsInsightsField = Literal["date_start", "date_stop"]


class AdAccountAdLimitsInsightsFields(BaseModel):
    """Pydantic model for AdAccountAdLimitsInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    date_start: str = Field(None, alias="date_start")
    date_stop: str = Field(None, alias="date_stop")
