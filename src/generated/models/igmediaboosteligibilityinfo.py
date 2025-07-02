"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGMediaBoostEligibilityInfoField = Literal["boost_ineligible_reason", "eligible_to_boost"]


class IGMediaBoostEligibilityInfoFields(BaseModel):
    """Pydantic model for IGMediaBoostEligibilityInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    boost_ineligible_reason: str = Field(None, alias="boost_ineligible_reason")
    eligible_to_boost: bool = Field(None, alias="eligible_to_boost")
