"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AgeRangeField = Literal["max", "min"]


class AgeRangeFields(BaseModel):
    """Pydantic model for AgeRange fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    max: int = Field(None, alias="max")
    min: int = Field(None, alias="min")
