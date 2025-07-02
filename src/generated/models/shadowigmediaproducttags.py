"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ShadowIGMediaProductTagsField = Literal[
    "image_url",
    "is_checkout",
    "merchant_id",
    "name",
    "price_string",
    "product_id",
    "review_status",
    "stripped_price_string",
    "stripped_sale_price_string",
    "x",
    "y",
]


class ShadowIGMediaProductTagsFields(BaseModel):
    """Pydantic model for ShadowIGMediaProductTags fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    image_url: str = Field(None, alias="image_url")
    is_checkout: bool = Field(None, alias="is_checkout")
    merchant_id: int = Field(None, alias="merchant_id")
    name: str = Field(None, alias="name")
    price_string: str = Field(None, alias="price_string")
    product_id: int = Field(None, alias="product_id")
    review_status: str = Field(None, alias="review_status")
    stripped_price_string: str = Field(None, alias="stripped_price_string")
    stripped_sale_price_string: str = Field(None, alias="stripped_sale_price_string")
    x: float = Field(None, alias="x")
    y: float = Field(None, alias="y")
