"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountDsaRecommendationsField = Literal["recommendations"]


class AdAccountDsaRecommendationsFields(BaseModel):
    """Pydantic model for AdAccountDsaRecommendations fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    recommendations: list[str] = Field(None, alias="recommendations")
