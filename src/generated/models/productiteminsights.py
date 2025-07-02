"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductItemInsightsField = Literal[
    "ad_click_count",
    "ad_impression_count",
    "add_to_cart_count",
    "purchase_count",
    "view_content_count",
]


class ProductItemInsightsFields(BaseModel):
    """Pydantic model for ProductItemInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_click_count: int = Field(None, alias="ad_click_count")
    ad_impression_count: int = Field(None, alias="ad_impression_count")
    add_to_cart_count: int = Field(None, alias="add_to_cart_count")
    purchase_count: int = Field(None, alias="purchase_count")
    view_content_count: int = Field(None, alias="view_content_count")
