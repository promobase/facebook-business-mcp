"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BrandSafetyCampaignConfigField = Literal["comment_moderation_filter"]


class BrandSafetyCampaignConfigFields(BaseModel):
    """Pydantic model for BrandSafetyCampaignConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    comment_moderation_filter: str = Field(None, alias="comment_moderation_filter")
