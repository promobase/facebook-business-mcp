"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeContextualMultiAdsField = Literal["enroll_status"]


class AdCreativeContextualMultiAdsFields(BaseModel):
    """Pydantic model for AdCreativeContextualMultiAds fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    enroll_status: str = Field(None, alias="enroll_status")
