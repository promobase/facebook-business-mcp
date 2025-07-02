"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
McomOnboardingStatusField = Literal["onboarding_status", "page_id"]


class McomOnboardingStatusFields(BaseModel):
    """Pydantic model for McomOnboardingStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    onboarding_status: str = Field(None, alias="onboarding_status")
    page_id: str = Field(None, alias="page_id")
