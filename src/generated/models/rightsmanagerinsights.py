"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
RightsManagerInsightsField = Literal[
    "error", "error_message", "metadata", "totals", "x_axis_breakdown"
]


class RightsManagerInsightsFields(BaseModel):
    """Pydantic model for RightsManagerInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    error: str = Field(None, alias="error")
    error_message: str = Field(None, alias="error_message")
    metadata: list[dict[str, dict[str, Any]]] = Field(None, alias="metadata")
    totals: list[dict[str, dict[str, Any]]] = Field(None, alias="totals")
    x_axis_breakdown: list[list[dict[str, dict[str, Any]]]] = Field(None, alias="x_axis_breakdown")
