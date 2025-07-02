"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AttributionSpecField = Literal["event_type", "window_days"]


class AttributionSpecFields(BaseModel):
    """Pydantic model for AttributionSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    event_type: str = Field(None, alias="event_type")
    window_days: int = Field(None, alias="window_days")
