"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductItemShippingField = Literal[
    "shipping_country",
    "shipping_price_currency",
    "shipping_price_value",
    "shipping_region",
    "shipping_service",
]


class ProductItemShippingFields(BaseModel):
    """Pydantic model for ProductItemShipping fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    shipping_country: str = Field(None, alias="shipping_country")
    shipping_price_currency: str = Field(None, alias="shipping_price_currency")
    shipping_price_value: float = Field(None, alias="shipping_price_value")
    shipping_region: str = Field(None, alias="shipping_region")
    shipping_service: str = Field(None, alias="shipping_service")
