"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
InstagramInsightsValueField = Literal["end_time", "value"]


class InstagramInsightsValueFields(BaseModel):
    """Pydantic model for InstagramInsightsValue fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    end_time: datetime = Field(None, alias="end_time")
    value: dict[str, Any] = Field(None, alias="value")
