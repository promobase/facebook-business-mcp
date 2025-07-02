"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelEventPredictionField = Literal["dismissed", "event_type", "rule"]


class AdsPixelEventPredictionFields(BaseModel):
    """Pydantic model for AdsPixelEventPrediction fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    dismissed: bool = Field(None, alias="dismissed")
    event_type: str = Field(None, alias="event_type")
    rule: str = Field(None, alias="rule")
