"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignConversionValueExpressionSpecField = Literal[
    "adjustment_sign", "adjustment_weight", "destination_type"
]


class AdCampaignConversionValueExpressionSpecFields(BaseModel):
    """Pydantic model for AdCampaignConversionValueExpressionSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adjustment_sign: str = Field(None, alias="adjustment_sign")
    adjustment_weight: int = Field(None, alias="adjustment_weight")
    destination_type: str = Field(None, alias="destination_type")
