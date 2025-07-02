"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelItemPriceField = Literal["date", "item_price_coverage"]


class AdsPixelItemPriceFields(BaseModel):
    """Pydantic model for AdsPixelItemPrice fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    date: str = Field(None, alias="date")
    item_price_coverage: str = Field(None, alias="item_price_coverage")
