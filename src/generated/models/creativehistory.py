"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CreativeHistoryField = Literal["creative_fingerprint", "time_ranges"]


class CreativeHistoryFields(BaseModel):
    """Pydantic model for CreativeHistory fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creative_fingerprint: int = Field(None, alias="creative_fingerprint")
    time_ranges: list[dict[str, Any]] = Field(None, alias="time_ranges")
