"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountSmartSuggestedAdsField = Literal[
    "ad_creative_spec", "description", "guidance_spec", "thumbnail_url"
]


class AdAccountSmartSuggestedAdsFields(BaseModel):
    """Pydantic model for AdAccountSmartSuggestedAds fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_creative_spec: str = Field(None, alias="ad_creative_spec")
    description: str = Field(None, alias="description")
    guidance_spec: list[str] = Field(None, alias="guidance_spec")
    thumbnail_url: str = Field(None, alias="thumbnail_url")
