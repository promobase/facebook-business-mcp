"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelDeliveryRecommendationsField = Literal["custom_event_type", "optimization_goal"]


class AdsPixelDeliveryRecommendationsFields(BaseModel):
    """Pydantic model for AdsPixelDeliveryRecommendations fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    custom_event_type: str = Field(None, alias="custom_event_type")
    optimization_goal: str = Field(None, alias="optimization_goal")
