"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeRecommenderSettingsField = Literal["preferred_events", "product_sales_channel"]


class AdCreativeRecommenderSettingsFields(BaseModel):
    """Pydantic model for AdCreativeRecommenderSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    preferred_events: list[str] = Field(None, alias="preferred_events")
    product_sales_channel: str = Field(None, alias="product_sales_channel")
