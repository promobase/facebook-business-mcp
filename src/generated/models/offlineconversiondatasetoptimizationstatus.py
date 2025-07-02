"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
OfflineConversionDataSetOptimizationStatusField = Literal[
    "event", "last_changed_time", "last_detected_time", "status"
]


class OfflineConversionDataSetOptimizationStatusFields(BaseModel):
    """Pydantic model for OfflineConversionDataSetOptimizationStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    event: str = Field(None, alias="event")
    last_changed_time: int = Field(None, alias="last_changed_time")
    last_detected_time: int = Field(None, alias="last_detected_time")
    status: str = Field(None, alias="status")
