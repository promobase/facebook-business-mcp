"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenURLEntityAtRangesField = Literal["length", "offset", "url"]


class LeadGenURLEntityAtRangesFields(BaseModel):
    """Pydantic model for LeadGenURLEntityAtRanges fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    length: int = Field(None, alias="length")
    offset: int = Field(None, alias="offset")
    url: str = Field(None, alias="url")
