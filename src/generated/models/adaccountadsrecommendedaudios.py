"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountAdsRecommendedAudiosField = Literal["audio_assets"]


class AdAccountAdsRecommendedAudiosFields(BaseModel):
    """Pydantic model for AdAccountAdsRecommendedAudios fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audio_assets: list[int] = Field(None, alias="audio_assets")
