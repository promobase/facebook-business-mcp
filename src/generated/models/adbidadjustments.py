"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdBidAdjustmentsField = Literal["age_range", "page_types", "user_groups"]


class AdBidAdjustmentsFields(BaseModel):
    """Pydantic model for AdBidAdjustments fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    age_range: dict[str, float] = Field(None, alias="age_range")
    page_types: dict[str, Any] = Field(None, alias="page_types")
    user_groups: str = Field(None, alias="user_groups")
