"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ReachFrequencyAdFormatField = Literal["details", "type"]


class ReachFrequencyAdFormatFields(BaseModel):
    """Pydantic model for ReachFrequencyAdFormat fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    details: dict[str, Any] = Field(None, alias="details")
    type: str = Field(None, alias="type")
