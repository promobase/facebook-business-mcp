"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TimezoneOffsetField = Literal["abbr", "isdst", "offset", "time", "ts"]


class TimezoneOffsetFields(BaseModel):
    """Pydantic model for TimezoneOffset fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    abbr: str = Field(None, alias="abbr")
    isdst: bool = Field(None, alias="isdst")
    offset: int = Field(None, alias="offset")
    time: str = Field(None, alias="time")
    ts: int = Field(None, alias="ts")
