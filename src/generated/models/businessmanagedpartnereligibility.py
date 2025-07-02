"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessManagedPartnerEligibilityField = Literal["is_eligible", "reason_code", "reason_description"]


class BusinessManagedPartnerEligibilityFields(BaseModel):
    """Pydantic model for BusinessManagedPartnerEligibility fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_eligible: bool = Field(None, alias="is_eligible")
    reason_code: str = Field(None, alias="reason_code")
    reason_description: str = Field(None, alias="reason_description")
