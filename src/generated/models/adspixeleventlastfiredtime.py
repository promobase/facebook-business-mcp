"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelEventLastFiredTimeField = Literal["event", "last_fired_time"]


class AdsPixelEventLastFiredTimeFields(BaseModel):
    """Pydantic model for AdsPixelEventLastFiredTime fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    event: str = Field(None, alias="event")
    last_fired_time: int = Field(None, alias="last_fired_time")
