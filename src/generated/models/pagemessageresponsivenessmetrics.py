"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageMessageResponsivenessMetricsField = Literal[
    "is_very_responsive", "response_rate", "response_time"
]


class PageMessageResponsivenessMetricsFields(BaseModel):
    """Pydantic model for PageMessageResponsivenessMetrics fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_very_responsive: bool = Field(None, alias="is_very_responsive")
    response_rate: float = Field(None, alias="response_rate")
    response_time: float = Field(None, alias="response_time")
