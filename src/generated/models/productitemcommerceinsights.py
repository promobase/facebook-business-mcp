"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductItemCommerceInsightsField = Literal[
    "message_sends", "organic_impressions", "paid_impressions"
]


class ProductItemCommerceInsightsFields(BaseModel):
    """Pydantic model for ProductItemCommerceInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    message_sends: int = Field(None, alias="message_sends")
    organic_impressions: int = Field(None, alias="organic_impressions")
    paid_impressions: int = Field(None, alias="paid_impressions")
