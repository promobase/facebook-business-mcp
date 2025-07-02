"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .shadowigusercatalogproductvariant import ShadowIGUserCatalogProductVariantFields


# Field literal type
ShadowIGUserCatalogProductSearchField = Literal[
    "image_url",
    "is_checkout_flow",
    "merchant_id",
    "product_id",
    "product_name",
    "product_variants",
    "retailer_id",
    "review_status",
]


class ShadowIGUserCatalogProductSearchFields(BaseModel):
    """Pydantic model for ShadowIGUserCatalogProductSearch fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    image_url: str = Field(None, alias="image_url")
    is_checkout_flow: bool = Field(None, alias="is_checkout_flow")
    merchant_id: int = Field(None, alias="merchant_id")
    product_id: int = Field(None, alias="product_id")
    product_name: str = Field(None, alias="product_name")
    product_variants: list[ShadowIGUserCatalogProductVariantFields] = Field(
        None, alias="product_variants"
    )
    retailer_id: str = Field(None, alias="retailer_id")
    review_status: str = Field(None, alias="review_status")
