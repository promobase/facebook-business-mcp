"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsEligibilityField = Literal["live_shopping"]


class AdsEligibilityFields(BaseModel):
    """Pydantic model for AdsEligibility fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    live_shopping: dict[str, Any] = Field(None, alias="live_shopping")
